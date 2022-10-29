"""Module for compare two files and identify the difference."""


def identify_diff(data1, data2):
    """Find the different between two files.

    Parameters:
        data1, data2
    Returns:
        result_diff
    """
    result_diff = []
    sorted_keys = sorted(set.union(set(data1), set(data2)))
    for key in sorted_keys:
        if key not in data1:
            result_diff.append(f'+ {key}: {data2[key]}')
        elif key not in data2:
            result_diff.append(f'- {key}: {data1[key]}')
        elif data1[key] == data2[key]:
            result_diff.append(f'  {key}: {data1[key]}')
        else:
            result_diff.append(f'- {key}: {data1[key]}')
            result_diff.append(f'+ {key}: {data2[key]}')
    return result_diff



