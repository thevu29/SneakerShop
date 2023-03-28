from tkinter import Tk
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Admin.AdminMain import AdMainForm
from Product import ProductForm
from Login.LoginForm import *

class MainForm(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        self.login = StartForm(self)
     
if __name__ == '__main__':
    main = MainForm()
    main.geometry('950x600+280+100')
    main.mainloop()