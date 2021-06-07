import os
import unittest

from .. import _method
from qiime2.plugin.testing import TestPluginBase

class TestUtils(TestPluginBase):
    package = 'q2_parser.tests'

    cases = {
        'pound_commented_labels': ('#', True, 3, False),
        'pound_uncommented_labels': ('#', False, 3, False),
    }

    def test_first_data_line(self):

        for filename, params in self.cases.items():

            filepath = self.get_data_path(filename=filename)
            with open(filepath, 'r') as fh:
                first_data_line = _method.index_of_first_data_line(fh,
                                                                   params[0],
                                                                   params[1]
                                                                   )
                self.assertEqual(first_data_line, params[2])

    def test_get_feature_labels(self):
        exp = ['Feature one', 'dos', 'third']

        for filename, params in self.cases.items():
            filepath = self.get_data_path(filename=filename)
            with open(filepath, 'r') as fh:
                data = fh.readlines()

            obs = _method.find_feature_labels(fh,
                                      comment_character=params[0],
                                      commented_labels=params[1],
                                      headerless=params[3])
            self.assertEqual(exp, list(obs))

if __name__ == '__main__':
    unittest.main()
