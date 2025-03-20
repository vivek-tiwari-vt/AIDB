from core.storage import Storage
from core.metadata import MetadataManager
import numpy as np  # Import numpy for dummy embeddings

storage = Storage(vector_db_enabled=True)  # Enable vector DB
metadata_manager = MetadataManager()

# Load structured data (CSV)
structured_data = [
    ["user_id", "name", "age"],
    ["1", "Alice", "30"],
    ["2", "Bob", "25"]
]
storage.save_data("relational", structured_data, "users.csv")

# Load unstructured data (JSON)
unstructured_data = {
    "product_id": "123",
    "name": "Laptop",
    "price": 999.99
}
# Generate dummy embedding for demonstration
product_embedding = np.random.rand(128).tolist()  # Generate a 128-dimensional vector
storage.save_data("document", unstructured_data, "product.json", embed_data=product_embedding)

# Load graph data (JSON) - simplified
graph_data = {
    "nodes": [{"id": "1", "label": "User"}, {"id": "2", "label": "Product"}],
    "edges": [{"source": "1", "target": "2", "relation": "purchased"}]
}
storage.save_data("graph", graph_data, "purchase_graph.json")

# Load key-value data
key_value_data = {"session_id": "abc123xyz", "user_id": "1"}
storage.save_data("keyvalue", key_value_data, "session.json")

# Load multimedia metadata (assuming multimedia files are stored externally)
multimedia_metadata = {
    "file_path": "path/to/image.jpg",
    "tags": ["cat", "animal", "pet"],
    "description": "Image of a cat"
}
metadata_manager.save_metadata("image.jpg", multimedia_metadata)

# Save a dummy multimedia file (replace with actual file loading)
dummy_image_data = b"Dummy image data"  # Example binary data
storage.save_multimedia_file("data/multimedia/image.jpg", dummy_image_data)

print("Data loaded successfully.")