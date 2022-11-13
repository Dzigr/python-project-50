"""Apply specified formatter."""
from gendiff.formatters.json import get_json_format
from gendiff.formatters.plain import get_plain_format
from gendiff.formatters.stylish import get_stylish_format


def apply_formatter(difference, formatter):
    """Apply the selected display format.

    Parameters:
        difference: dict with differences.
        formatter: specified format for apply.

    Returns:
        formatted difference.
    """
    if formatter == 'plain':
        return get_plain_format(difference)
    elif formatter == 'stylish':
        return get_stylish_format(difference)
    elif formatter == 'json':
        return get_json_format(difference)
