from core.storage import Storage
from core.metadata import MetadataManager  # Import MetadataManager
import numpy as np  # Import numpy for generating embeddings if needed

# Initialize storage with vector DB enabled
storage = Storage(vector_db_enabled=True)
metadata_manager = MetadataManager()  # Initialize MetadataManager

# Example of adding structured data (CSV)
def add_structured_data():
    structured_data = [
        ["user_id", "name", "age"],
        ["3", "Charlie", "28"],
        ["4", "Diana", "22"]
    ]
    storage.save_data("relational", structured_data, "new_users.csv")

# Example of adding unstructured data (JSON)
def add_unstructured_data():
    unstructured_data = {
        "product_id": "456",
        "name": "Smartphone",
        "price": 799.99
    }
    # Generate dummy embedding for demonstration
    product_embedding = np.random.rand(128).tolist()  # Generate a 128-dimensional vector
    storage.save_data("document", unstructured_data, "smartphone.json", embed_data=product_embedding)

# Example of adding graph data (JSON)
def add_graph_data():
    graph_data = {
        "nodes": [{"id": "3", "label": "User"}, {"id": "4", "label": "Product"}],
        "edges": [{"source": "3", "target": "4", "relation": "viewed"}]
    }
    storage.save_data("graph", graph_data, "view_graph.json")

# Example of adding key-value data
def add_key_value_data():
    key_value_data = {"session_id": "xyz789abc", "user_id": "3"}
    storage.save_data("keyvalue", key_value_data, "new_session.json")

# Example of adding multimedia metadata
def add_multimedia_metadata():
    multimedia_metadata = {
        "file_path": "path/to/new_image.jpg",
        "tags": ["dog", "animal", "pet"],
        "description": "Image of a dog"
    }
    metadata_manager.save_metadata("new_image.jpg", multimedia_metadata)  # Use MetadataManager

    # Save a dummy multimedia file (replace with actual file loading)
    dummy_image_data = b"New dummy image data"  # Example binary data
    storage.save_multimedia_file("data/multimedia/new_image.jpg", dummy_image_data)

if __name__ == "__main__":
    add_structured_data()
    add_unstructured_data()
    add_graph_data()
    add_key_value_data()
    add_multimedia_metadata()
    print("Custom data added successfully.")
