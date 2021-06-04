#class EvaluateTSV:

    def find_feature_labels(self, data, comment_character, commented_labels?):
        liminal_line = delineate_data(data, comment_character)

        if commented_labels?:
            return data[liminal_line - 1]
    
    def delineate_data(self, comment_character):
    
        i = 0
    
        with self.open() as fh:
            for i, line in enumerate(fh, 0):
                if line[0] == comment_character:
                    print('intermeadiate line: %s' % i) 
                    continue
                print(i)
                return i
