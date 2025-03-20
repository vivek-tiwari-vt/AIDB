import os
import json
import csv

class Query:
    """
    Handles querying across different data models.
    """
    def __init__(self, base_path="data"):
        self.base_path = base_path

    def search(self, query_terms, model_type=None):
        """
        Searches for data based on query terms.
        """
        results = []  # Initialize results as an empty list
        if model_type:
            results.extend(self._search_in_model(model_type, query_terms))
        else:
            for model in ['document', 'graph', 'keyvalue', 'relational']:
                results.extend(self._search_in_model(model, query_terms))
        return results

    def _search_in_model(self, model_type, query_terms):
        """
        Searches for data within a specific data model.
        """
        results = []  # Initialize results as an empty list
        data_path = os.path.join(self.base_path, self._get_data_path(model_type))
        try:
            for filename in os.listdir(data_path):
                filepath = os.path.join(data_path, filename)
                if not filepath.endswith(('.json', '.csv')):
                    continue  # Skip non-data files

                with open(filepath, 'r') as f:
                    if filename.endswith('.json'):
                        data = json.load(f)
                    elif filename.endswith('.csv'):
                        data = list(csv.reader(f))
                    else:
                        continue

                if self._matches_query(data, query_terms):
                    results.append({"model": model_type, "filename": filename})
        except FileNotFoundError:
            pass  # Handle cases where directories might be missing
        return results

    def _matches_query(self, data, query_terms):
        """
        Checks if the data matches the query terms.
        Returns True if query_terms is empty (equivalent to SELECT *).
        """
        # Return True for empty query_terms (SELECT * case)
        if not query_terms:
            return True
            
        if isinstance(data, dict):
            return any(term.lower() in str(value).lower() for term in query_terms for value in data.values())
        elif isinstance(data, list):
            return any(term.lower() in str(item).lower() for term in query_terms for item in data)
        else:
            return False

    def _get_data_path(self, model_type):
        """
        Returns the appropriate data path for the model type.
        """
        if model_type == 'relational':
            return "structured"
        elif model_type in ['document', 'keyvalue', 'graph']:
            return "unstructured"
        else:
            return "multimedia"