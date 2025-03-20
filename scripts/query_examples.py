from core.query import Query
from core.metadata import MetadataManager
from core.storage import Storage
import numpy as np  # Import numpy for dummy query embeddings

query_engine = Query()
metadata_manager = MetadataManager()
storage = Storage(vector_db_enabled=True)  # Enable vector DB

# Example queries
print("Searching for 'Alice':", query_engine.search(["Alice"]))
print("Searching for 'Product' in graph:", query_engine.search(["Product"], model_type="graph"))

# Example of loading data after a query
results = query_engine.search(["Laptop"])
if results:
    first_result = results[0]
    if first_result["model"] == "document":
        data = storage.load_data("document", first_result["filename"])
        print("Loaded data:", data)

# Example of querying multimedia metadata
multimedia_results = query_engine.search(["cat"], model_type="multimedia")
print("Multimedia search results:", multimedia_results)
if multimedia_results:
    first_result = multimedia_results[0]
    metadata = metadata_manager.load_metadata(first_result["filename"].replace(".json", ""))
    print("Metadata for first result:", metadata)

# Example of vector search (dummy query embedding)
print("\nVector search example:")
dummy_query_embedding = np.random.rand(128).tolist()  # Dummy query embedding
vector_results = storage.vector_db.search_embedding(dummy_query_embedding, top_k=3)
print("Vector search results:", vector_results)
if vector_results:
    for result in vector_results:
        data_id = result["data_id"]
        # Assuming data_id corresponds to filename for simplicity
        data = storage.load_data("document", data_id)  # Load the data
        print("  - Found data:", data)