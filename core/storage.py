import os
import json
import csv
from .data_model import DocumentModel, GraphModel, KeyValueModel, RelationalModel
from utils.file_utils import save_file, load_file, delete_file  # Import file utils
from vector_integration.vector_db_interface import VectorDBInterface  # Import VectorDBInterface

class Storage:
    """
    Handles storage and retrieval of data.
    """
    def __init__(self, base_path="data", vector_db_enabled=False):
        self.base_path = base_path
        self.models = {
            'document': DocumentModel("document"),
            'graph': GraphModel("graph"),
            'keyvalue': KeyValueModel("keyvalue"),
            'relational': RelationalModel("relational")
        }
        self._create_directories()

        self.vector_db_enabled = vector_db_enabled
        if self.vector_db_enabled:
            self.vector_db = VectorDBInterface()

    def _create_directories(self):
        """
        Creates necessary directories for storage.
        """
        os.makedirs(os.path.join(self.base_path, "structured"), exist_ok=True)
        os.makedirs(os.path.join(self.base_path, "unstructured"), exist_ok=True)
        os.makedirs(os.path.join(self.base_path, "multimedia"), exist_ok=True)

    def save_data(self, model_type, data, filename, embed_data=None):
        """
        Saves data using the specified data model.
        If embed_data is provided and vector_db_enabled, it also saves vector embeddings.
        """
        if model_type not in self.models:
            raise ValueError(f"Invalid model type: {model_type}")

        filepath = os.path.join(self.base_path, self._get_data_path(model_type), filename)
        self.models[model_type].save(data, filepath)

        # Handle vector embeddings
        if self.vector_db_enabled and embed_data is not None:
            data_id = filename  # Using filename as a simple ID
            self.vector_db.add_embedding(data_id, embed_data)

    def load_data(self, model_type, filename):
        """
        Loads data using the specified data model.
        """
        if model_type not in self.models:
            raise ValueError(f"Invalid model type: {model_type}")

        filepath = os.path.join(self.base_path, self._get_data_path(model_type), filename)
        return self.models[model_type].load(filepath)

    def save_multimedia_file(self, file_path, file_data):
        """
        Saves a multimedia file to the specified path.
        """
        save_file(file_path, file_data)

    def load_multimedia_file(self, file_path):
        """
        Loads a multimedia file from the specified path.
        """
        return load_file(file_path)

    def delete_multimedia_file(self, file_path):
        """
        Deletes a multimedia file from the specified path.
        """
        delete_file(file_path)

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