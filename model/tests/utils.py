import ast


def list2file(l, file_name):
    with open(file_name, 'w') as filehandle:
        for elem in l:
            filehandle.write('%s\n' % elem)


def file2list(file_name):
    result = []
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            current_place = line[:-1]
            result.append(ast.literal_eval(current_place))
    return result
