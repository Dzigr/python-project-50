def stringify(tree):
    result = '{\n'
    if isinstance(tree, list):
        for line in tree:
            result += ' {line}\n'.format(line=line)
        result += '{end}'.format(end='}')
        return result
    return str(tree)
