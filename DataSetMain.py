#########################################################################################
# File Name: DataSetMain.py
# Purpose: The class is responsible for running the program
# Course Name: Computer Engineering Technology - Computing Science
# Author: Fleming Patel
# Professor: Stanley Pieda
# Since: 3.6
#########################################################################################

from DataSetView import DataSetView
import sys


class DataSetMain:

    def __init__(self):
        """
        Initial constructor
        """
        self.data_set_view = DataSetView()
        self.data_set_view.title("Fleming Patel")
        self.data_set_view.minsize("500","150")
        self.data_set_view.mainloop()


if __name__ == "__main__":
    # Main Method:- if python version is less then 3 than it will give you an error.
    # If python version is appropriate then it is responsible for running program.
    if sys.version_info[0] < 3:
        print("Python 3 or Greater version required to launch the application")
    else:
        app = DataSetMain()