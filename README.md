# AIDB - Multi-Model Database

## Overview

AIDB is a versatile multi-model database designed to handle various data types, including structured, unstructured, graph, key-value, and multimedia data. It provides a unified interface for storing, querying, and managing diverse datasets, making it ideal for applications requiring flexible data handling.

## Features

-   **Multi-Model Support**: Handles relational, document, graph, key-value, and multimedia data.
-   **Unified Query Interface**: Provides a SQL-like interface for querying across different data models.
-   **Vector Database Integration**: Supports vector embeddings for similarity searches.
-   **Metadata Management**: Manages metadata for multimedia files.
-   **Extensible Architecture**: Easy to extend with new data models and functionalities.
-   **Interactive Command-Line Interface**: Simplifies data management and querying.

## Architecture

The AIDB architecture consists of the following main components:

-   **Core**:
    -   **Data Models**: Defines the structure and behavior of different data models (Document, Graph, KeyValue, Relational).
    -   **Storage**: Handles the storage and retrieval of data using the specified data models.
    -   **Query**: Provides a unified query interface for searching across different data models.
    -   **Metadata**: Manages metadata storage and retrieval, particularly for multimedia files.
-   **Utils**:
    -   **File Utils**: Provides utility functions for file operations (saving, loading, deleting).
-   **Vector Integration**:
    -   **Vector DB Interface**: Defines an interface for interacting with a vector database for similarity searches.
-   **Scripts**:
    -   **Load Data**: Contains scripts for loading example data into the database.
    -   **Query Examples**: Provides example queries for different data models.
    -   **Query Interface**: Offers an interactive command-line interface for querying and managing data.

## Directory Structure

```
AIDB/
├── core/                      # Core components of the database
│   ├── __init__.py
│   ├── data_model.py          # Defines data models (Document, Graph, KeyValue, Relational)
│   ├── storage.py             # Handles data storage and retrieval
│   ├── query.py               # Provides a unified query interface
│   └── metadata.py            # Manages metadata storage and retrieval
├── data/                      # Data storage directory
│   ├── structured/            # Stores structured data (e.g., CSV files)
│   ├── unstructured/          # Stores unstructured data (e.g., JSON files)
│   └── multimedia/            # Stores multimedia files
├── scripts/                   # Scripts for loading data and running queries
│   ├── __init__.py
│   ├── load_data.py           # Loads example data into the database
│   ├── query_examples.py      # Provides example queries
│   └── query_interface.py     # Interactive command-line interface
├── vector_integration/      # Vector database integration components
│   ├── __init__.py
│   └── vector_db_interface.py # Interface for interacting with a vector database
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── file_utils.py          # Utility functions for file operations
├── main.py                    # Main application file
└── README.md                  # Project documentation
```

## Getting Started

### Prerequisites

-   Python 3.6+
-   `numpy`

### Installation

1.  Clone the repository:

```sh
git clone <repository_url>
cd AIDB
```

2.  Install the required dependencies:

```sh
pip install numpy
```

### Usage

1.  **Load Example Data**:

```sh
python3 -m scripts.load_data
```

2.  **Run the Interactive Query Interface**:

```sh
python3 -m scripts.query_interface
```

    This will start an interactive session where you can enter SQL-like commands to interact with your database.

### Example Queries

-   **Select all data from the relational model**:

```sql
SELECT * FROM relational
```

-   **Select all data from the document model**:

```sql
SELECT * FROM document
```

-   **Insert data into the graph model**:

```sql
INSERT INTO graph VALUES {'nodes': [{'id': '10', 'label': 'User'}, {'id': '11', 'label': 'Product'}], 'edges': [{'source': '10', 'target': '11', 'relation': 'viewed'}]}
```

-   **Delete data from the keyvalue model**:

```sql
DELETE FROM keyvalue
```

-   **Drop the relational table**:

```sql
DROP TABLE relational
```

## Extending AIDB

### Adding a New Data Model

1.  **Create a New Data Model Class**:

    Create a new class in `core/data_model.py` that inherits from `DataModel`. Implement the `save` and `load` methods for your data model.

2.  **Update the Storage Class**:

    In `core/storage.py`, update the `__init__` method to include your new data model in the `self.models` dictionary. Also, update the `_get_data_path` method to return the appropriate data path for your model type.

3.  **Update the Query Class**:

    In `core/query.py`, update the `_search_in_model` method to handle your new data model. Also, update the `_matches_query` method to check if the data matches the query terms.

4.  **Update the Query Interface**:

    In `scripts/query_interface.py`, update the `parse_query` method to handle SQL-like commands for your new data model. Also, add functions for querying, adding, deleting, and dropping data for your model.

## License

[MIT](LICENSE)