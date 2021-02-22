import ast
from model.resources.default_locations import DEFAULT_CONFIG_PATH
from model.encoding.charIds import CharIdsConfig

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


def remove_nikud(text):
    # text_processor = TextProcessor(DEFAULT_CONFIG_PATH)
#     # model2text = ModelInputToSentence(DEFAULT_CONFIG_PATH)
#     # inputs, labels = text_processor.prepare_text(text)
#     # empty_labels = [[]*len(labels)]
#     # result = model2text.input_and_labels_to_sentence(inputs, empty_labels)
#     # return result

    cid = CharIdsConfig(DEFAULT_CONFIG_PATH)
    result = ""
    for c in text:
        if not cid.is_nikud(c):
            result += c
    return result

def remove_backslash_n(text):
    result = ""
    for c in text:
        if c != "\n":
            result += c
    return result

