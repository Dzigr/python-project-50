"""Plain formatter."""
import json


def get_plain_format(diff_file, initial_path=''):
    """Display a description of the changes as text.

    Parameters:
        diff_file: dict with differences.
        initial_path: the path by which the difference is found.

    Returns:
        diff_text: description of the changes.
    """
    messages = {
        'updated': "Property '{path}' was updated. From {old_value} to {new_value}",
        'new': "Property '{path}' was added with value: {value}",
        'removed': "Property '{path}' was removed",
    }
    diff_text = []
    for key, diff_value in diff_file.items():
        status = diff_value.get('status')
        current_value = diff_value.get('value')
        path = build_path(key, initial_path)
        if status == 'inserted':
            diff_text.append(get_plain_format(current_value, path))
        elif status == 'updated':
            diff_text.append(messages.get(status).format(
                path=path,
                old_value=get_converted_value(current_value.get('old')),
                new_value=get_converted_value(current_value.get('new')),
            ),
            )
        elif status == 'new':
            diff_text.append(messages.get(status).format(
                path=path,
                value=get_converted_value(current_value),
            ),
            )
        elif status == 'removed':
            diff_text.append(messages.get(status).format(
                path=path,
            ),
            )
    return '\n'.join(diff_text)


def build_path(new_point, previous_path=''):
    """Build string representation of the path.

    Parameters:
        new_point: point that will be added to path.
        previous_path: the built path.

    Returns:
        path: string representation of the path.
    """
    if previous_path:
        return '.'.join([previous_path, new_point])
    return new_point


def get_converted_value(initial_value):
    """Convert the value to required form.

    Parameters:
        initial_value: value for converting.

    Returns:
        value: value after conversion.
    """
    if isinstance(initial_value, (bool, type(None))):
        return json.dumps(initial_value)
    elif isinstance(initial_value, dict):
        return '[complex value]'
    elif isinstance(initial_value, str):
        return "'{value}'".format(value=initial_value)
    return initial_value
