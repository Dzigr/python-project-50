"""Module for compare two files and identify the diff."""


def identify_diff(data1, data2):
    """Find the different between two files.

    Parameters:
        data1: data from first file.
        data2: data from second file.

    Returns:
        result_diff: identified diff.
    """
    result_diff = {}
    sorted_keys = sorted(set.union(set(data1), set(data2)))
    for key in sorted_keys:
        if key not in data1:
            status = 'new'
            ident_value = data2.get(key)
        elif key not in data2:
            status = 'removed'
            ident_value = data1.get(key)
        elif data1.get(key) == data2.get(key):
            status = 'equal'
            ident_value = data2.get(key)
        elif isinstance((data1.get(key) and data2.get(key)), dict):
            status, ident_value = 'inserted', identify_diff(
                data1.get(key),
                data2.get(key),
            )
        else:
            status = 'updated'
            ident_value = {
                'old': data1.get(key),
                'new': data2.get(key),
            }
        result_diff[key] = {
            'status': '{status}'.format(status=status),
            'value': ident_value,
        }
    return result_diff
