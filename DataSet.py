#########################################################################################
# File Name: DataSet.py
# Purpose: Contains getters and setters property for all instance variables
# Course Name: Computer Engineering Technology - Computing Science
# Author: Fleming Patel
# Professor: Stanley Pieda
# Since: 3.6
#########################################################################################


class DataSet:

    def __init__(self):
        self.referenceDate = None
        self.geo_location = None
        self.product_name = None
        self.vector = None
        self.coordinate = None
        self.value = None

    def __str__(self):
        return "#Ref_Date: " + self.get_reference_date() + " #GEO: " + self.get_geo_location() + " #COMMOD: " + \
               self.get_product_name() + " #Vector: " + self.get_vector() + " #Coordinate: " + self.get_coordinate() \
               + " #Value :" + self.get_value()

    def get_reference_date(self):
        """
        :return: self.referenceDate
        """
        return self.referenceDate

    def set_reference_date(self,reference_date):
        """
        :param reference_date: set self.reference_date
        :return:
        """
        self.referenceDate = reference_date

    def get_geo_location(self):
        """
        :return: self.geo_location
        """
        return self.geo_location

    def set_geo_location(self,geo_location):
        """
        :param geo_location: set self.geo_location
        :return:
        """
        self.geo_location = geo_location

    def get_product_name(self):
        """
        :return: self.product_name
        """
        return self.product_name

    def set_product_name(self,product_name):
        """
        :param product_name: set self.product_name
        :return:
        """
        self.product_name = product_name

    def get_vector(self):
        """
        :return: self.vector
        """
        return self.vector

    def set_vector(self,vector):
        """
        :param vector: set self.vector
        :return:
        """
        self.vector = vector

    def get_coordinate(self):
        """
        :return: self.coordinate
        """
        return self.coordinate

    def set_coordinate(self,coordinate):
        """
        :param coordinate: set self.coordinate
        :return:
        """
        self.coordinate = coordinate

    def get_value(self):
        """
        :return: self.value
        """
        return self.value

    def set_value(self,value):
        """
        :param value: set self.value
        :return:
        """
        self.value = value
