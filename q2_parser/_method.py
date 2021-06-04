#class EvaluateTSV:

def find_feature_labels(data,
                        comment_character: str,
                        commented_labels: bool):

    liminal_line = delineate_data(data, comment_character)

    if commented_labels:
        return data[liminal_line - 1]

def index_of_first_data_line(data, comment_character, commented_labels):

    i = 0

    for i, line in enumerate(data, 0):

        if line[0] == comment_character:
            continue
        
        if commented_labels:
            return i
        else:
            return i + 1
