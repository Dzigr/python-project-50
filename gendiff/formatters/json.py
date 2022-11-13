"""Json formatter."""
import json


def get_json_format(diff_file):
    """Display a description of the changes as json.

    Parameters:
        diff_file: dict with differences.

    Returns:
        diff_text: with json format applied.
    """
    return json.dumps(diff_file)
