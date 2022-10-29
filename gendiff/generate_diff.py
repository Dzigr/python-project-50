"""Module for generating diff with formatter."""
from gendiff.diff import identify_diff
from gendiff.formatters import apply_formatter
from gendiff.parser import get_data


def generate_diff(file_path1, file_path2, formatter="stylish"):
    """Generate diff and apply formatter.

    Returns:
        apply_formatter(difference, formatter)
    """
    data_from_file1 = get_data(file_path1)
    data_from_file2 = get_data(file_path2)
    difference = identify_diff(
        data_from_file1,
        data_from_file2,
    )

    return apply_formatter(difference, formatter)
