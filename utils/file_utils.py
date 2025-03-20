import os

def save_file(file_path, file_data):
    """
    Saves data to a file.
    """
    try:
        with open(file_path, 'wb') as f:
            f.write(file_data)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def load_file(file_path):
    """
    Loads data from a file.
    """
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def delete_file(file_path):
    """
    Deletes a file.
    """
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False