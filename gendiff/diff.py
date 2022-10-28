"""Module for finding the difference."""
import json


def generate_diff(file_path1, file_path2):
    """Find the different between two files.

    Parameters:
        file_path1, file_path2
    Returns:
        stringify(result_diff)
    """
    result_diff = []
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    sorted_keys = sorted(set.union(set(file1), set(file2)))
    for key in sorted_keys:
        if key not in file1:
            result_diff.append(f'+ {key}: {file2[key]}')
        elif key not in file2:
            result_diff.append(f'- {key}: {file1[key]}')
        elif file1[key] == file2[key]:
            result_diff.append(f'  {key}: {file1[key]}')
        else:
            result_diff.append(f'- {key}: {file1[key]}')
            result_diff.append(f'+ {key}: {file2[key]}')
    return stringify(result_diff)


def stringify(tree):
    result = '{\n'
    if isinstance(tree, list):
        for line in tree:
            result += ' {line}\n'.format(line=line)
        result += '{end}'.format(end='}')
        return result
    return str(tree)
