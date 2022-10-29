"""Module for parsing the file."""
import json
import yaml
from os.path import splitext

EXTENSIONS = ('.yaml', '.yml', '.json')


def get_data(file_path):
    """Parse data from file with extension in EXTENSIONS.

    Returns:
        data
    """
    _, extension = splitext(file_path)
    if extension in EXTENSIONS:
        with open(file_path) as file:
            if extension == ".json":
                data = json.load(file)
            else:
                data = yaml.safe_load(file)
            return data
    raise Exception('"{extension}" is unsupported file extension!'.format(
            extension=extension,
        )
    )
