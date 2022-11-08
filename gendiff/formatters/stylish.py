"""Stylish formatter."""
from itertools import chain
from convert import get_converted_value

STATE = {
    'new': '  + ',
    'removed': '  - ',
    'equal': '    ',
}

REPLACER = ' '
SPACES_COUNT = 4
INDENT = REPLACER * SPACES_COUNT


def check_value(value, depth):
    if not isinstance(value, dict):
        return value
    string_list = ['{']
    spaces = INDENT * depth
    for key, value_ in value.items():
        if isinstance(value_, dict):
            val = check_value(value_, depth + 1)
        else:
            val = value_
        string = '{spaces}{indent}{key}: {val}'.format(spaces=spaces,
                                                       indent=INDENT,
                                                       key=key,
                                                       value_=value_,
                                                       val=val)
        string_list.append(string)
    string_list.append('{spaces}}}'.format(spaces=spaces))
    return '\n'.join(string_list)


def stylish(diff_file):
    def inner(node, depth):
        result = []
        space = INDENT * depth
        for key, val in node.items():
            status = val.get('status')
            value = val.get('value')
            if status == 'inserted':
                stylish(value)
                result.append(f'{space}{INDENT}{key}: {inner(value, depth + 1)}')
            elif status == 'updated':
                old_value = value.get('old')
                new_value = value.get('new')
                result.append(f'{space}{STATE["removed"]}{key}: {check_value(old_value, depth + 1)}')
                result.append(f'{space}{STATE["new"]}{key}: {check_value(new_value, depth + 1)}')
            else:
                result.append(f'{space}{STATE.get(status)}{key}: {check_value(value, depth + 1)}')
        result_ = chain('{', result, [space + '}'])
        return '\n'.join(result_)
    file = get_converted_value(diff_file)
    return inner(file, depth=0)
