from core.query import Query
from core.metadata import MetadataManager
from core.storage import Storage
import numpy as np  # Import numpy for dummy query embeddings

# Initialize query engine, metadata manager, and storage
query_engine = Query()
metadata_manager = MetadataManager()
storage = Storage(vector_db_enabled=True)  # Enable vector DB

def parse_query(query):
    """
    Parses a simple SQL-like query and executes the corresponding function.
    """
    query = query.strip().lower()
    if query.startswith("select * from"):
        table = query.split("from")[1].strip()
        if table == "relational":
            query_structured_data([])
        elif table == "document":
            query_unstructured_data([])
        elif table == "graph":
            query_graph_data([])
        elif table == "keyvalue":
            query_key_value_data([])
        elif table == "multimedia":
            query_multimedia_metadata([])
        else:
            print(f"Unknown table: {table}")
    elif query.startswith("insert into"):
        table, values = query.split("values")
        table = table.split("into")[1].strip()
        values = eval(values.strip())
        if table == "relational":
            add_structured_data(values)
        elif table == "document":
            add_unstructured_data(values)
        elif table == "graph":
            add_graph_data(values)
        elif table == "keyvalue":
            add_key_value_data(values)
        elif table == "multimedia":
            add_multimedia_metadata(values)
        else:
            print(f"Unknown table: {table}")
    elif query.startswith("delete from"):
        table = query.split("from")[1].strip()
        if table == "relational":
            delete_data("relational")
        elif table == "document":
            delete_data("document")
        elif table == "graph":
            delete_data("graph")
        elif table == "keyvalue":
            delete_data("keyvalue")
        elif table == "multimedia":
            delete_data("multimedia")
        else:
            print(f"Unknown table: {table}")
    elif query.startswith("drop table"):
        table = query.split("table")[1].strip()
        drop_table(table)
    else:
        print(f"Unsupported query: {query}")

# Function to query structured data (CSV)
def query_structured_data(query_terms):
    results = query_engine.search(query_terms, model_type="relational")
    print("Structured data search results:", results)
    if results:
        for result in results:
            data = storage.load_data("relational", result["filename"])
            print(f"Data in {result['filename']}:", data)

# Function to query unstructured data (JSON)
def query_unstructured_data(query_terms):
    results = query_engine.search(query_terms, model_type="document")
    print("Unstructured data search results:", results)
    if results:
        for result in results:
            data = storage.load_data("document", result["filename"])
            print(f"Data in {result['filename']}:", data)

# Function to query graph data (JSON)
def query_graph_data(query_terms):
    results = query_engine.search(query_terms, model_type="graph")
    print("Graph data search results:", results)
    if results:
        for result in results:
            data = storage.load_data("graph", result["filename"])
            print(f"Data in {result['filename']}:", data)

# Function to query key-value data
def query_key_value_data(query_terms):
    results = query_engine.search(query_terms, model_type="keyvalue")
    print("Key-value data search results:", results)
    if results:
        for result in results:
            data = storage.load_data("keyvalue", result["filename"])
            print(f"Data in {result['filename']}:", data)

# Function to query multimedia metadata
def query_multimedia_metadata(query_terms):
    results = query_engine.search(query_terms, model_type="multimedia")
    print("Multimedia metadata search results:", results)
    if results:
        for result in results:
            metadata = metadata_manager.load_metadata(result["filename"].replace(".json", ""))
            print(f"Metadata for {result['filename']}:", metadata)

# Function to perform vector search
def query_vector_data(query_embedding, top_k=3):
    vector_results = storage.vector_db.search_embedding(query_embedding, top_k=top_k)
    print("Vector search results:", vector_results)
    if vector_results:
        for result in vector_results:
            data_id = result["data_id"]
            # Assuming data_id corresponds to filename for simplicity
            data = storage.load_data("document", data_id)  # Load the data
            print(f"Data for {data_id}:", data)

# Function to add structured data (CSV)
def add_structured_data(values):
    storage.save_data("relational", values, "new_users.csv")

# Function to add unstructured data (JSON)
def add_unstructured_data(values):
    storage.save_data("document", values, "new_document.json")

# Function to add graph data (JSON)
def add_graph_data(values):
    storage.save_data("graph", values, "new_graph.json")

# Function to add key-value data
def add_key_value_data(values):
    storage.save_data("keyvalue", values, "new_keyvalue.json")

# Function to add multimedia metadata
def add_multimedia_metadata(values):
    metadata_manager.save_metadata("new_image.jpg", values)

# Function to delete data
def delete_data(model_type):
    # Implement deletion logic here
    print(f"Data deleted from {model_type}")

# Function to drop table
def drop_table(table):
    # Implement drop table logic here
    print(f"Table {table} dropped")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        parse_query(query)
    else:
        print("Please provide a query.")
