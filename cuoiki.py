import sys
import cv2
import matplotlib
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Load(Mainwindow):
    def __init__(self):
        super(Load,self).__init__()
        loadUi('abc.ui',self)
        self.setWindowIcon(QtGui.QIcon("image/py-icon/png"))
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
