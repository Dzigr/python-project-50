"""Get format of file."""
from os.path import splitext


def get_format(filepath):
    """Get the file format.

    Parameters:
        filepath: path to the file.

    Returns:
        extension: string, with specified the file format
    """
    _, extension = splitext(filepath)
    if extension == '.yaml':
        return 'yaml'
    elif extension == '.yml':
        return 'yaml'
    elif extension == '.json':
        return 'json'
