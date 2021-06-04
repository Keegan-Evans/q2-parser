#class EvaluateTSV:

def find_feature_labels(data,
                        comment_character: str,
                        commented_labels: bool,
                        headerless: bool = False):

    first_data_line = index_of_first_data_line(data,
                                               comment_character,
                                               commented_labels)

    if commented_labels or (not commented_labels and not headerless):
        return data[first_data_line - 1]
    else:
        ValueError('No feature labels found')

def index_of_first_data_line(data, comment_character, commented_labels):

    i = 0

    for i, line in enumerate(data, 0):

        if line[0] == comment_character:
            continue
        
        if commented_labels:
            return i
        else:
            return i + 1
