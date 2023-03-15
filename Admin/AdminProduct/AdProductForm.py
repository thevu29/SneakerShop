from PIL import Image, ImageTk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, StringVar
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button

try:
    from .AdProduct import *
except:
    from AdProduct import *

class AdProductForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        # Tạo frame1
        self.frame1 = Frame(self)
        self.frame1.pack(fill=BOTH)
        self.title = Label(self.frame1, text="Quản lý sản phẩm", font=("Time News Roman", 22), foreground="black")
        self.title.pack()

        # Tạo frame layout kiểu grid để chứa các widget
        self.frameGrid2 = LabelFrame(self, text='Thông tin sản phẩm')
        self.frameGrid2.pack(fill=BOTH, pady=12)
        self.frameGrid2.configure(border=10, borderwidth=20, relief="solid")

        self.lb1 = Label(self.frameGrid2, text="Mã sản phẩm: ")
        self.lb1.grid(row=0, column=0, sticky='w')
        self.input1 = Entry(self.frameGrid2, width=30)
        self.input1.grid(row=0, column=1, padx=10)

        self.lb2 = Label(self.frameGrid2, text="Số lượng: ")
        self.lb2.grid(row=0, column=2, sticky='w', padx=(20, 0))
        self.input2 = Entry(self.frameGrid2, width=23)
        self.input2.grid(row=0, column=3, padx=10)

        self.lb3 = Label(self.frameGrid2, text="Hình ảnh: ")
        self.lb3.grid(row=0, column=4, padx=(20, 0), sticky='w')
        self.input3 = Entry(self.frameGrid2)
        self.input3.grid(row=0, column=5, padx=10)

        self.lb4 = Label(self.frameGrid2, text="Tên sản phẩm: ")
        self.lb4.grid(row=1, column=0, pady=(25, 0), sticky='w')
        self.input4 = Entry(self.frameGrid2, width=30)
        self.input4.grid(row=1, column=1, padx=10, pady=(25, 0))
        
        self.lb5 = Label(self.frameGrid2, text="Mã loại sản phẩm: ")
        self.lb5.grid(row=2, column=0, pady=(25, 0), sticky='w')
        self.input5 = Entry(self.frameGrid2, width=30)
        self.input5.grid(row=2, column=1, padx=10, pady=(25, 0))
        
        self.lb6 = Label(self.frameGrid2, text="Mã nhà cung cấp: ")
        self.lb6.grid(row=1, column=2, sticky='w', padx=(20, 0), pady=(25, 0))
        self.input6 = Entry(self.frameGrid2, width=23)
        self.input6.grid(row=1, column=3, padx=10, pady=(25, 0))

        # Tạo frame3
        self.labelFrame3 = LabelFrame(self, text="Danh sách sản phẩm")
        self.labelFrame3.pack(fill=BOTH)

        self.frame3 = Frame(self.labelFrame3, padding=4)
        self.frame3.pack()

        self.framePack3 = Frame(self.frame3)
        self.framePack3.pack(fill=BOTH)

        self.tree = Treeview(self.framePack3, selectmode='browse')
        self.tree.pack(side=LEFT)

        self.vsb = Scrollbar(self.framePack3, orient="vertical", command=self.tree.yview)

        # self.vsb.pack(side=RIGHT,fill='y')
        self.vsb.pack(side=RIGHT, fill='y')

        self.tree.configure(yscrollcommand=self.vsb.set)

        self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7")
        self.tree['show'] = 'headings'

        for column in ("1", "2", "3", "4", "5", "6", "7"):
            self.tree.column(column, anchor='c', width=130)

        self.tree.heading("1", text="Mã sản phẩm")
        self.tree.heading("2", text="Tên sản phẩm")
        self.tree.heading("3", text="Đơn giá")
        self.tree.heading("4", text="Số lượng")
        self.tree.heading("5", text="Mã nhà cung cấp")
        self.tree.heading("6", text="Mã loại sản phẩm")
        self.tree.heading("7", text="Hình ảnh")

        self.initProductData(self.tree)
        
        # Tạo frame4
        self.labelFrame4 = LabelFrame(self, text="Chức năng", padding=10)
        self.labelFrame4.pack(pady=12)

        self.frame4 = Frame(self.labelFrame4)
        self.frame4.pack()

        self.frameGrid4 = Frame(self.frame4)
        self.frameGrid4.grid(column=6, row=1)

        self.btn1 = Button(self.frameGrid4, text="Add new", width=12)
        self.btn1.grid(row=0, column=0, padx=10)

        self.btn2 = Button(self.frameGrid4, text="Save", width=12)
        self.btn2.grid(row=0, column=1, padx=10)

        self.btn3 = Button(self.frameGrid4, text="Delete", width=12)
        self.btn3.grid(row=0, column=2, padx=10)

        self.btn4 = Button(self.frameGrid4, text="Update", width=12)
        self.btn4.grid(row=0, column=3, padx=10)

        self.btn5 = Button(self.frameGrid4, text="View data", width=12)
        self.btn5.grid(row=0, column=4, padx=10)

        self.btn6 = Button(self.frameGrid4, text="Refresh", width=12)
        self.btn6.grid(row=0, column=5, padx=10)

    def initProductData(self, productList):
        product = AdProductData()
        productDataList = product.getProductList()
        for data in productDataList:
            productList.insert('', 'end', values=data)