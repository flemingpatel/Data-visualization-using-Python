#########################################################################################
# File Name: DataSetProcess.py
# Purpose: The purpose of this class is to process business logic which includes,
#          separating unique product, getting all products details etc.
# Course Name: Computer Engineering Technology - Computing Science
# Author: Fleming Patel
# Professor: Stanley Pieda
# Since: 3.6
#########################################################################################

from DataSet import DataSet
from collections import defaultdict
import sys

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas library installation required")

try:
    import numpy as np
except ImportError:
    sys.exit("numpy library installation required")

import csv
import sys


class DataSetProcess:
    """
    This are static variables representing column numbers of datafile.csv
    """
    ref_date_column = 0
    geo_location_column = 1
    product_name_column = 2
    vector_column = 3
    coordinate_column = 4
    value_column = 5

    def __init__(self,file_name):
        """
        Parameterized constructor:-
        :param file_name String variable which holds filename
        """
        self.file_name = file_name
        self.data_list = []

    def read_file(self):
        """
        This method is responsible for reading data file
        :return
        """
        try:
            with open(self.file_name, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    self._initialize_data_list(row)
        except csv.Error as ex:
            sys.exit('Error occurred on file {} reading, line {}: {}'.format(self.file_name, reader.line_num, ex))

    def _initialize_data_list(self,row):
        """
        This method is responsible for generating DataSet object and storing in data_list List
        :param row:
        :return:
        """
        if row != None:
            try:
                dataset = DataSet()
                dataset.set_reference_date(row[self.ref_date_column])
                dataset.set_geo_location(row[self.geo_location_column])
                dataset.set_product_name(row[self.product_name_column])
                dataset.set_vector(row[self.vector_column])
                dataset.set_coordinate(row[self.coordinate_column])
                dataset.set_value(row[self.value_column])
                self.data_list.append(dataset)
            except Exception as ex:
                sys.exit("Error occurred while adding data in list: {}".format(ex))
        else:
            print("Empty Data Found")

    def print_data_list(self):
        """
        This method is responsible for printing all data from data_list List
        :return:
        """
        for data in self.data_list:
            print(data)

        print("\nTotal {} records added successfully".format(len(self.data_list)))

    def get_product_list(self):
        """
        This method is responsible for generating unique product list and returning that list to UserInterface
        :return: unique_product_list
        """
        product_name_list = []
        index = 0;
        for data in self.data_list:
            if index == 0:
                index = index + 1
                continue
            else:
                s_product_name = getattr(data,'get_product_name')()
                product_name_list.append(s_product_name)
        # Creating set of all unique product
        product_set = set(product_name_list)
        # Converting unique product set to list
        unique_product_list = list(product_set)
        # Sorting all products alphabetically
        unique_product_list.sort()
        return unique_product_list

    def get_product_data(self,prodcut_name):
        """
        This method is responsible for getting unique product data and returning that list to UserInterface
        :return:
        """
        product_date_to_value_map = defaultdict(list)  # creating dictionaries which contains list of value
        index = 0
        for data in self.data_list:
            if index == 0: # skipping first row from data
                index = index + 1
                continue
            else:
                # comparing selected product name with global list product name
                if prodcut_name == getattr(data,'get_product_name')():
                    s_product_reference_date = getattr(data,'get_reference_date')()  # getting reference date
                    s_product_value = getattr(data,'get_value')()  # getting value
                    """
                    if product value is "x" then skip that product year
                    Here code is not skipping whole product because some year might contains values
                    """
                    if s_product_value == 'x':
                        continue
                    # converting to string
                    s_product_reference_date = str(s_product_reference_date)
                    temp = s_product_reference_date.split("-")  # tokenizing string
                    # getting month and year string from the tokenizing string
                    month = temp[0]
                    year = temp[1]
                    # converting string value to float
                    s_product_value = float(s_product_value)
                    # mapping all specific values to specific year
                    product_date_to_value_map[year].append(s_product_value)  # adding list of values for specific year

                else:
                    continue

        if len(product_date_to_value_map) == 0:
            return product_date_to_value_map
        else:
            product_analysed_map = self.do_mathematical_analysis(product_date_to_value_map)
            return product_analysed_map

    def do_mathematical_analysis(self, product_date_to_value_map):
        """
        This method get the dictionaries as a parameter and creating new dictionaries while mapping max and min values
        to specific year
        :param product_date_to_value_map:
        :return: product_analysed_map
        """
        product_analysed_map = defaultdict(list)
        flag = False
        for key in product_date_to_value_map.keys():
            value_list = product_date_to_value_map.get(key)
            max_value = max(value_list)
            min_value = min(value_list)
            if flag == False and key != "00":
                key = int(key) + int(1900)
            else:
                flag = True
                key = int(key) + int(2000)

            temp_dict = {"max_value":max_value,"min_value":min_value,"year":key}
            product_analysed_map['mydataframe'].append(temp_dict);

        return product_analysed_map









