"""Stylish formatter."""
import json
from itertools import chain

STATE = {  # noqa: 407
    'new': '  + ',
    'removed': '  - ',
    'equal': '    ',
}

REPLACER = ' '
SPACES_COUNT = 4
INDENT = REPLACER * SPACES_COUNT


def stringify_value(checked_value, depth):
    """Check value and convert value if it's dict.

    Parameters:
        checked_value: stringify the value.
        depth: indent depth.


    Returns:
        string_list: string with right indent.
    """
    if not isinstance(checked_value, dict):
        return checked_value
    string_list = ['{']
    spaces = INDENT * depth
    for key, current_value in checked_value.items():
        if isinstance(checked_value, dict):
            current_value = stringify_value(current_value, depth + 1)
        string = '{spaces}{indent}{key}: {value}'.format(
            spaces=spaces,
            indent=INDENT,
            key=key,
            value=current_value,
        )
        string_list.append(string)
    string_list.append('{spaces}}}'.format(spaces=spaces))
    return '\n'.join(string_list)


def get_stylish_format(diff_file):
    """Generate list of strings with highlighted differences.

    Parameters:
        diff_file: dict with differences.

    Returns:
        apply_formatter(difference, formatter):
        output of the resulting difference in the selected format.
    """

    def inner(diff_dict, depth):  # noqa: WPS430
        result_list = []
        space = INDENT * depth
        for key, diff_val in diff_dict.items():
            status = diff_val.get('status')
            current_value = diff_val.get('value')
            if status == 'inserted':
                result_list.append(
                    '{space}{indent}{key}: {inserted_value}'.format(
                        space=space,
                        indent=INDENT,
                        key=key,
                        inserted_value=inner(current_value, depth + 1),
                    ),
                )
            elif status == 'updated':
                result_list.append('{space}{flag}{key}: {old_value}'.format(
                    space=space,
                    flag=STATE.get('removed'),
                    key=key,
                    old_value=stringify_value(
                        current_value.get('old'),
                        depth + 1,
                    ),
                ),
                )
                result_list.append('{space}{flag}{key}: {new_value}'.format(
                    space=space,
                    flag=STATE.get('new'),
                    key=key,
                    new_value=stringify_value(
                        current_value.get('new'),
                        depth + 1,
                    ),
                ),
                )
            else:
                result_list.append('{space}{flag}{key}: {value}'.format(
                    space=space,
                    flag=STATE.get(status),
                    key=key,
                    value=stringify_value(current_value, depth + 1),
                ),
                )
        return '\n'.join(chain('{', result_list, [space + '}']))  # noqa: WPS336

    converted_file = get_converted_value(diff_file)
    return inner(converted_file, depth=0)


def get_converted_value(diff_file):
    """Convert the bool & None values to string.

    Parameters:
        diff_file: dict with differences.

    Returns:
        diff_file: file after conversion of bool values.
    """
    for key, diff_value in diff_file.items():
        if isinstance(diff_value, (bool, type(None))):
            diff_file[key] = json.dumps(diff_value)
        elif isinstance(diff_value, dict):
            get_converted_value(diff_value)
    return diff_file
