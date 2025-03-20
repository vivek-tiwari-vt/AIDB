import os
import json

class MetadataManager:
    """
    Manages metadata storage and retrieval.
    """
    def __init__(self, base_path="data/multimedia_metadata"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def save_metadata(self, filename, metadata):
        """
        Saves metadata to a JSON file.
        """
        filepath = os.path.join(self.base_path, f"{filename}.json")
        with open(filepath, 'w') as f:
            json.dump(metadata, f, indent=4)

    def load_metadata(self, filename):
        """
        Loads metadata from a JSON file.
        """
        filepath = os.path.join(self.base_path, f"{filename}.json")
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def delete_metadata(self, filename):
        """
        Deletes a metadata file.
        """
        filepath = os.path.join(self.base_path, f"{filename}.json")
        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass