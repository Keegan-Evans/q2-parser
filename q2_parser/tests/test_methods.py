import os
import unittest

from .. import _method
from qiime2.plugin.testing import TestPluginBase

class TestUtils(TestPluginBase):
    package = 'q2_parser.tests'

    def test_first_data_line(self):
        cases = {
            'pound_commented_labels': ('#', True, 3),
            'pound_uncommented_labels': ('#', False, 3),
        }

        for filename, params in cases.items():

            filepath = self.get_data_path(filename=filename)
            with open(filepath, 'r') as fh:
                first_data_line = _method.index_of_first_data_line(fh,
                                                                   params[0],
                                                                   params[1]
                                                                   )
                self.assertEqual(first_data_line, params[2])


if __name__ == '__main__':
    unittest.main()
