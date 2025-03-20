import json
import csv

class DataModel:
    """
    Base class for all data models.
    """
    def __init__(self, name):
        self.name = name

    def save(self, data, filepath):
        """
        Saves data to a file.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def load(self, filepath):
        """
        Loads data from a file.
        """
        raise NotImplementedError("Subclasses must implement this method")

class DocumentModel(DataModel):
    """
    Handles JSON documents.
    """
    def save(self, data, filepath):
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load(self, filepath):
        with open(filepath, 'r') as f:
            return json.load(f)

class GraphModel(DataModel):
    """
    Stores data as nodes and edges.
    """
    def save(self, data, filepath):
        # Simplified: Storing graph as a JSON with nodes and edges
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load(self, filepath):
        with open(filepath, 'r') as f:
            return json.load(f)

class KeyValueModel(DataModel):
    """
    Stores data as key-value pairs.
    """
    def save(self, data, filepath):
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load(self, filepath):
        with open(filepath, 'r') as f:
            return json.load(f)

class RelationalModel(DataModel):
    """
    Stores data in CSV files (simplified relational model).
    """
    def save(self, data, filepath):
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)  # Data should be a list of lists

    def load(self, filepath):
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)