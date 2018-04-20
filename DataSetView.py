#########################################################################################
# File Name: DataSetView.py
# Purpose: This class is responsible for generating GUI that user faces.
# Course Name: Computer Engineering Technology - Computing Science
# Author: Fleming Patel
# Professor: Stanley Pieda
# Since: 3.6
#########################################################################################

from DataSetProcess import DataSetProcess
from collections import defaultdict

try:
    import matplotlib
    matplotlib.use("TkAgg")
except ImportError:
    sys.exit("matplotlib library installation required")

try:
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit("matplotlib library installation required")

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas library installation required")

try:
    import numpy as np
except ImportError:
    sys.exit("numpy library installation required")

try:
    import tkinter as tk
except ImportError:
    sys.exit("tkinter library installation required")

from tkinter import filedialog
from tkinter import ttk
from tkinter import StringVar


class DataSetView(tk.Tk):  # Inherits Tk class

    def __init__(self):
        """
        Initial constructor:
        """
        self.process = type('DataSetProcess', (object,), {})()
        self.product_analysed_map = defaultdict(list)
        # constructor of TK class
        tk.Tk.__init__(self)
        """
        Toplevel widget of Tk which represents mostly the main window
        of an application. It has an associated Tcl interpreter.
        """
        container = tk.Frame(self)  # main container (Parent Frame)
        container.pack()
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)
        """
        In dictionary data structure we adds the frame according to it's Class Name as key
        """
        self.frames = {}  # dictionaries of frames
        """
        By default the start page is out default page.
        Here i am passing main window as a container in the start page constructor,
        Start Page class inherits frame class and that frame would be placed on main window
        """
        frame = StartPage(container,self)
        # storing StartPage frame on key of StartPage
        self.frames[StartPage] = frame
        # Placing the frame on main window
        frame.grid(row=0, column=0, sticky="nsew")
        # Opening StartPage as default view
        self.show_frame(StartPage)

    def append_frame_to_map(self,F,container):
        """
        This method is responsible to add Frame in dictionary
        :param F: The Frame which you want to add
        :param container: The main window where you want to place
        :return: None
        """
        frame = F(container,self)
        self.frames[F] = frame
        frame.grid(row=0,column=0,sticky="nsew")

    def show_frame(self, cont):
        """
        This method is responsible for opening specific frame
        :param cont: The name of the Class
        :return: None
        """
        frame = self.frames[cont]
        frame.tkraise()

    def error_popup(self,error_message):
        """
        This is a abstract method that represent error popup windows and some information messages according,
        to specific frames i.e., StartPage frame and SecondPage frame
        :param error_message: The String containing the error message
        :return:
        """
        raise NotImplementedError("Subclass must implement abstract method")


class StartPage(tk.Frame,DataSetView):  # Inherits Frame class

    # Constructor of StartPage Class
    def __init__(self,parent,controller):
        # constructor of TK class
        tk.Frame.__init__(self,parent)
        # creating label
        center_label = tk.Label(self, text="Please select csv file to analysis")
        # creating a button and assigning a function call to button click
        center_button = tk.Button(self, text="Select csv File", command=lambda: self._open_file(controller,parent))
        center_label.pack(pady=10)
        center_button.pack()

    def _open_file(self,controller,parent):
        """
        This method executes when user select a button for selecting a csv file.
        This function only allows to select a csv file and a Excel file.
        When user select the file, the file name will be passed to DataSetProcess Class where file is read and all file
        data is stored in custom data structure.
        This function is also responsible for printing all data that stored in data structure and changing current
        frame to next level frame.
        :param controller: Instance of DataSetView Class object itself
        :param parent: Parent frame which is called container in DataSetView Class
        :return: None
        """
        try:
            file_name = filedialog.askopenfilename(filetypes=[("Excel file", "*csv")])
            controller.process = DataSetProcess(file_name)
            # reading and printing data as well as total number of data to the console and also generating global list
            controller.process.read_file()
            controller.process.print_data_list()
            # switching frame
            controller.append_frame_to_map(SecondPage, parent)
            controller.show_frame(SecondPage)
        except Exception as ex:
            self.error_popup(str(ex))

    def error_popup(self,error_message):
        """
        This method is overrides DataSetView Class method. This method evokes when the _open_file method found any
        exception. When it founds any exception this method is responsible for creating a popup frame where the error
        is human readable.
        :param error_message: The String containing the error message
        :return: None
        """
        # creating top level Tk main window
        popup = tk.Tk()
        # creating a title for window
        popup.title("Error Occurred")
        # setting width and height
        popup.minsize("300", "80")
        # creating a label which represent error
        label = tk.Label(popup, text=error_message)
        # placing a label with padding on y axes
        label.pack(pady=10)
        # creating a button
        button = tk.Button(popup, text="Okay", command=lambda: popup.destroy())
        # placing a button
        button.pack()
        # infinite loop
        popup.mainloop()


class SecondPage(tk.Frame,DataSetView):  # Inherits Frame class

    # Constructor of Second Page class
    def __init__(self,parent,controller):
        # constructor of TK class
        tk.Frame.__init__(self,parent)
        """
        This frames shows the button on top for going back to selection of file again and on the bottom of the button
        it shows a drop down menu with containing unique products which we store earlier in custom
        data structure form datafiles
        """
        center_button = tk.Button(self, text="Back to selection of file", command=lambda: controller.show_frame(StartPage))
        center_button.pack(pady=10)
        center_label = tk.Label(self,text="Please select a product from drop down")
        center_label.pack()

        # getting unique product list
        unique_product_list = controller.process.get_product_list()
        # creating a instruction string variable for user
        self.s_product_name = StringVar()
        # creating a drop down menu
        combo_box = ttk.Combobox(self,textvariable = self.s_product_name, state="readonly", width=45)
        # adding all unique product to drop down
        combo_box.config(values=unique_product_list)
        self.s_product_name.set("Please select a product")
        combo_box.pack()
        # assigning an graph generating event with any changes of selection made in drop down.
        combo_box.bind("<<ComboboxSelected>>", lambda event: self._generate_graph(event, controller))

    def _generate_graph(self,event,controller):
        """
        This method is responsible for allowing to show graph for specific product if it's valid and it's contains data
        :param event: drop down menu changing event
        :param controller: Instance of DataSetView Class object itself
        :return: None
        """
        try:
            product_name = self.s_product_name.get()
            if product_name != "Please select a product":
                """
                product name is passed to DataSetProcess Class where it generates custom data frame containing product
                minimum vaue and maximum value for specific year
                """
                controller.product_analysed_map = controller.process.get_product_data(product_name)
                """
                The current course data file have listed some product with "x" data that needs to be removed.
                If return data frame length is empty then it produced a error pop up with appropriate message.
                On the contrary it if data frame is valid then it allows to generating graph for product.
                """
                if len(controller.product_analysed_map) != 0:
                    self.show_graph(controller,product_name)
                else:
                    message = str("No Product Data Found")
                    self.error_popup(message)
        except Exception as ex:
            self.error_popup(str(ex))

    def show_graph(self,controller,product_name):
        """
        This method is responsible for creating a graph and placing graph to user area with the help of API
        :param controller: Instance of DataSetView Class object itself
        :return: None
        """
        data = pd.DataFrame(controller.product_analysed_map["mydataframe"])
        max_price_list = data['max_value'].tolist()
        min_price_list = data['min_value'].tolist()
        year_list = data['year'].tolist()

        # clearing the current axes
        plt.cla()
        # clearing the figure from window
        plt.clf()
        # close the window completely
        plt.close()
        # closes all figure windows
        plt.close('all')
        # plotting the year against max price list graph
        plt.plot(year_list,max_price_list,label='max-price')
        # plotting the year against min price list graph
        plt.plot(year_list, min_price_list,label='min-price')
        # adding x axes label
        plt.xlabel('Year')
        # adding y axes label
        plt.ylabel('Values')
        # adding product name as title on the figure
        plt.title(product_name)
        # adding title to figure window
        current_fig_reference = plt.gcf()
        current_fig_reference.canvas.set_window_title('Fleming Patel - Research Project')
        plt.legend()
        # adding grid lines in the figure
        plt.grid(True)
        # displaying the figure
        plt.show()

    def error_popup(self,error_message):
        """
        This method is overrides DataSetView Class method. This method evokes when the _generate_graph method found any
        exception. When it founds any exception this method is responsible for creating a popup frame where the error
        is human readable.
        :param error_message: The String containing the error message
        :return: None
        """
        popup = tk.Tk()
        popup.title("Error Occurred")
        popup.minsize("300", "80")
        label = tk.Label(popup, text=error_message)
        label.pack(pady=10)
        button = tk.Button(popup, text="Okay", command=lambda: popup.destroy())
        button.pack()
        popup.mainloop()