import unittest

import DBUtil, Pipeline


class quickframetestcases(unittest.TestCase):
    def test_data_cleanup(self):
        input_list = [['1979.486.1', 'FALSE', 'FALSE', '1'],
            ['1980.2d64.5', 'FALSE', 'FALSE', '2'],
            ['67.265', 'FALSE', 'FALSE', '3'],
            ['67.265.10', 'FALSE', 'FALSE', '4']]

        output_list = []
        for row in input_list:
            cleaned_row = Pipeline.data_cleanup(row)
            if cleaned_row is not None:
                output_list.append(cleaned_row)

        self.assertEqual(2,len(output_list))

    def test_normalize_row(self):
        input_list = ["1853","1901","1909–27","1800–1900","1867","ca. 1785","1795–1810"]

        output_dict = {}
        for row in input_list:
            date_range = Pipeline.normalize_row(cleaned_row[21])
            self.assertEqual(4, date_range[0])
            self.assertEqual(4, date_range[1])


    def test_classification_total(self):
        input_list = [
            ['1979.486.1', 'FALSE', 'FALSE', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Metal'],
            ['1980.2d64.5', 'FALSE', 'FALSE', '2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Furniture'],
            ['67.265', 'FALSE', 'FALSE', '3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Metal'],
            ['67.265.10', 'FALSE', 'FALSE', '4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Gold']
        ]

        output_dict = {}
        for row in input_list:
            Pipeline.running_total(row, output_dict)

        self.assertEqual(2,output_dict['Metal'])
        self.assertEqual(1, output_dict['Furniture'])
        self.assertEqual(1, output_dict['Gold'])



        def select_table(self):

            DBUtil.select_table("classification_totals")


if __name__ == '__main__':
    unittest.main()