#class EvaluateTSV:

def find_feature_labels(data,
                        comment_character: str,
                        commented_labels: bool,
                        headerless: bool = False,
                        sep: str = '\t'):

    first_data_line = index_of_first_data_line(data,
                                               comment_character,
                                               commented_labels)

    labels = data[first_data_line - 1]
    labels = labels.split(sep)

    # remove comment character
    if commented_labels:
        labels = strip_comment_character(labels=labels,
                                 comment_character=comment_character)

    labels = [label.strip() for label in labels]
    return labels

    # if commented_labels or (not commented_labels and not headerless):
    #     return read_labels(data, first_data_line - 1)
    # else:
    #     ValueError('No feature labels found')

def strip_comment_character(labels: list, comment_character: str):
    labels = [labels[0].lstrip(comment_character)] + labels[1:]
    return labels

def read_labels(data, label_line):
    data_list = list(data)
    print(data_list)
    #return data_list[label_line]
    #i = 0

    #if i == label_line:
    #    return data.readline()
    #else:
    #    i += 1
    #    data.readline()

def index_of_first_data_line(data, comment_character, commented_labels):

    i = 0

    for i, line in enumerate(data, 0):

        if line[0] == comment_character:
            continue

        if commented_labels:
            return i
        else:
            return i + 1
