import json


def generate_diff(file_path1, file_path2):
    result_diff = []
    file_1 = json.load(open(file_path1))
    file_2 = json.load(open(file_path2))
    sorted_keys = sorted(set.union(set(file_1), set(file_2)))
    for key in sorted_keys:
        if key not in file_1: #data added
            result_diff.append(f"+ {key}: {file_2[key]}")
        elif key not in file_2: #data deleted
            result_diff.append(f"- {key}: {file_1[key]}")
        elif file_1[key] == file_2[key]: #data in both files
            result_diff.append(f"  {key}: {file_1[key]}")
        else:
            result_diff.append(f"- {key}: {file_1[key]}")
            result_diff.append(f"+ {key}: {file_2[key]}")
    return stringify(result_diff)


def stringify(tree, replacer=' ', spaces_count=1):
    def inner(values, lvl=1):
        result = "{\n"
        if isinstance(values, list):
            for i in values:
                result += f'{replacer * spaces_count * lvl}{i}' + "\n"
            result += '}'
            return result
        else:
            return str(values)

    return inner(tree)
