#########################################################################################
# File Name: test.py
# Purpose: To unit testing in python programming
# Course Name: Computer Engineering Technology - Computing Science
# Author: Fleming Patel
# Professor: Stanley Pieda
# Since: 3.6
#########################################################################################

import unittest
from DataSetProcess import DataSetProcess


class TestCase(unittest.TestCase):  # Inherits TestCase class
    print("Fleming Patel's Demonstration of unittest\n\n")

    def test_read_file(self):
        """
        This method tests the file reading method which exists in the DataSetProcess class.
        It compares the total number of records found in the csv file.
        :return: None
        """
        process = DataSetProcess("datafile.csv")
        process.read_file()
        result = len(process.data_list)
        expected = 100945
        print("Result: {} \tExpected Result: {}".format(result, expected))
        self.assertEqual(result, expected, "read_file function is not working: The length of total records did "
                                           "not match")

    def test_corrupt_product_data(self):
        """
        This method tests the product with value data “x”. If the product’s all value is “x” then,
        the GUI part shows the error popup depending the return map length.
        If map length is zero then all “x” value is discarded that means the error popup will rise.
        :return: None
        """
        process = DataSetProcess("datafile.csv")
        process.read_file()
        product_name = str("Mayonnaise, mustard, dressing, vegetable spreads")
        product_analysed_map = process.get_product_data(product_name)
        result = len(product_analysed_map)
        expected = 0
        print("Result: {} \tExpected Result: {}".format(result, expected))
        self.assertEqual(result, expected, "get_product_data is not working: The product with no data didn't catch by"
                                           "algorithm")


if __name__ == "__main__":
    unittest.main()
