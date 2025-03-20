from core.storage import Storage
from core.query import Query
from core.metadata import MetadataManager
from scripts.load_data import storage, metadata_manager  # Import the instances

def main():
    print("Starting the Multi-Model Database...")

    # Demonstrate loading data
    print("Loading example data:")
    # The load_data script has already loaded the data
    print("Example data loaded.")

    # Demonstrate querying
    query_engine = Query()
    print("\nQuery examples:")
    print("Searching for 'Alice':", query_engine.search(["Alice"]))
    print("Searching for 'Product' in graph:", query_engine.search(["Product"], model_type="graph"))

    # Demonstrate multimedia metadata query
    print("\nMultimedia metadata query:")
    multimedia_results = query_engine.search(["cat"], model_type="multimedia")
    print("Multimedia search results:", multimedia_results)