import numpy as np
from typing import List, Dict

class VectorDBInterface:
    """
    Interface for interacting with a vector database.
    This is a simplified in-memory implementation for demonstration purposes.
    """
    def __init__(self):
        self.vectors = {}  # In-memory storage for vectors

    def add_embedding(self, data_id: str, embedding: List[float]):
        """
        Adds a vector embedding to the database.
        """
        self.vectors[data_id] = embedding

    def search_embedding(self, query_embedding: List[float], top_k: int = 5) -> List[Dict]:
        """
        Searches for the most similar embeddings.
        Returns a list of dictionaries with data_id and similarity score.
        """
        if not self.vectors:
            return

        query_vector = np.array(query_embedding)
        similarities = {}
        for data_id, vector in self.vectors.items():
            vector = np.array(vector)
            # Calculate cosine similarity
            similarity = np.dot(query_vector, vector) / (np.linalg.norm(query_vector) * np.linalg.norm(vector))
            similarities[data_id] = similarity

        # Get top-k results
        sorted_similarities = sorted(similarities.items(), key=lambda item: item[1], reverse=True)
        top_results = [{"data_id": data_id, "similarity": score} for data_id, score in sorted_similarities[:top_k]]
        return top_results