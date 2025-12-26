import json
import random

def load_from_json(file_name):
    """
    Loads data (list or dict) from a JSON file.
    
    Args:
        file_name (str): The name of the JSON file (with or without .json extension).
    
    Returns:
        list | dict: The data loaded from the JSON file.
    """
    # Ensure filename ends with .json
    if not file_name.endswith(".json"):
        file_name += ".json"
    
    try:
        # Read JSON file
        with open(file_name, "r") as f:
            data = json.load(f)
        print(f"✅ Data successfully loaded from '{file_name}'")
        return data
    except FileNotFoundError:
        print(f"❌ File '{file_name}' not found.")
    except json.JSONDecodeError:
        print(f"❌ File '{file_name}' is not a valid JSON file.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")


def calculate_prob(student_info):
    # In this function, you should return an int number between 0 to 100 as the probability of student getting High mark in the exam
    # TODO: You should change this function code:
    # YOU CODE HERE
    return random.randint(0, 100)
