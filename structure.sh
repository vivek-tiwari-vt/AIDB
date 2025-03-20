
# Create the core directory and its subdirectories
mkdir -p core
touch core/__init__.py
touch core/data_model.py
touch core/storage.py
touch core/query.py
touch core/metadata.py

# Create the data directory and its subdirectories
mkdir -p data/structured
mkdir -p data/unstructured
mkdir -p data/multimedia

# Create the scripts directory
mkdir scripts
touch scripts/__init__.py
touch scripts/load_data.py
touch scripts/query_examples.py

# Create the vector_integration directory
mkdir vector_integration
touch vector_integration/__init__.py
touch vector_integration/vector_db_interface.py

# Create the utils directory
mkdir utils
touch utils/__init__.py
touch utils/file_utils.py

# Create the main application file
touch main.py

# Display the directory tree structure
echo "Directory structure created:"
tree