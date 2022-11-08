"""Convert the bool & None values in the file."""
import json


def get_converted_value(file):
    """Convert the bool & None values to string.

    Returns:
        file: file after conversion of bool values.
    """
    for key, value in file.items():
        if isinstance(value, (bool, type(None))):
            file[key] = json.dumps(value)
        elif isinstance(value, dict):
            get_converted_value(value)
    return file
