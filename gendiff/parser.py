"""Module for parsing the file."""
import json
from os.path import splitext

import yaml

EXTENSIONS = {  # noqa: 407
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
    '.json': json.load,
}


def get_data(file_path):
    """Parse data from file with extension in EXTENSIONS.

    Parameters:
        file_path: path to the file.

    Returns:
        EXTENSIONS[extension](file):
        data from the file.

    Raises:
         Exception: unsupported file extension.
    """
    _, extension = splitext(file_path)
    if extension in EXTENSIONS:
        with open(file_path) as file_data:
            return EXTENSIONS.get(extension)(file_data)
    raise Exception(
        '"{extension}" is unsupported file extension!'.format(
            extension=extension,
        ),
    )
