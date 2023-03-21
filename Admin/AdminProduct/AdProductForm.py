from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, StringVar
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button
from PIL import Image, ImageTk

try:
    from .AdProduct import *
except:
    from AdProduct import *

class AdProductForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.product = AdProductData()
        self.productDataList = self.product.getProductList()

        # Tạo frame1
        self.frame1 = Frame(self)
        self.frame1.pack(fill=BOTH)
        self.title = Label(self.frame1, text="Quản lý sản phẩm", font=("Time News Roman", 22), foreground="black")
        self.title.pack()

        # Tạo frame layout kiểu grid để chứa các widget
        self.frameGrid2 = LabelFrame(self, text='Thông tin sản phẩm')
        self.frameGrid2.pack(fill=BOTH, pady=12)
        self.frameGrid2.configure(border=10, borderwidth=20, relief="solid")

        self.productId = Label(self.frameGrid2, text="Mã sản phẩm: ")
        self.productId.grid(row=0, column=0, sticky='w')
        self.txtProductId = Entry(self.frameGrid2, width=30)
        self.txtProductId.grid(row=0, column=1, padx=10)

        self.productQuantity = Label(self.frameGrid2, text="Số lượng: ")
        self.productQuantity.grid(row=0, column=2, sticky='w', padx=(20, 0))
        self.txtProductQuantity = Entry(self.frameGrid2, width=23)
        self.txtProductQuantity.grid(row=0, column=3, padx=10)

        self.productImage = Label(self.frameGrid2, text="Hình ảnh: ")
        self.productImage.grid(row=0, column=4, padx=(30, 0), sticky='w', rowspan=3)
        # self.txtProductImage = Entry(self.frameGrid2)
        # self.txtProductImage.grid(row=0, column=5, padx=10)

        self.productName = Label(self.frameGrid2, text="Tên sản phẩm: ")
        self.productName.grid(row=1, column=0, pady=(25, 0), sticky='w')
        self.txtProductName = Entry(self.frameGrid2, width=30)
        self.txtProductName.grid(row=1, column=1, padx=10, pady=(25, 0))
        
        self.productPrice = Label(self.frameGrid2, text="Giá: ")
        self.productPrice.grid(row=1, column=2, padx=(20, 0), pady=(25, 0), sticky='w')
        self.txtProductPrice = Entry(self.frameGrid2, width=23)
        self.txtProductPrice.grid(row=1, column=3, padx=10, pady=(25, 0))
        
        self.productCategory = Label(self.frameGrid2, text="Mã loại sản phẩm: ")
        self.productCategory.grid(row=2, column=0, pady=(25, 0), sticky='w')
        self.txtProductCategory = Entry(self.frameGrid2, width=30)
        self.txtProductCategory.grid(row=2, column=1, padx=10, pady=(25, 0))
        
        self.productSupplier = Label(self.frameGrid2, text="Mã nhà cung cấp: ")
        self.productSupplier.grid(row=2, column=2, sticky='w', padx=(20, 0), pady=(25, 0))
        self.txtProductSupplier = Entry(self.frameGrid2, width=23)
        self.txtProductSupplier.grid(row=2, column=3, padx=10, pady=(25, 0))

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

        self.tree["columns"] = ("1", "2", "3", "4", "5", "6")
        self.tree['show'] = 'headings'

        for column in ("1", "2", "3", "4", "5", "6"):
            self.tree.column(column, width=180)
            if column != "2":
                self.tree.column(column, anchor='c', width=150)

        self.tree.heading("1", text="Mã sản phẩm")
        self.tree.heading("2", text="Tên sản phẩm")
        self.tree.heading("3", text="Đơn giá")
        self.tree.heading("4", text="Số lượng")
        self.tree.heading("5", text="Mã nhà cung cấp")
        self.tree.heading("6", text="Mã loại sản phẩm")

        self.initProductData(self.tree)
        self.tree.bind('<<TreeviewSelect>>', lambda x: self.showProductInfo())
        
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
        for data in self.productDataList:
            productList.insert('', 'end', values=data)
        
    def showProductInfo(self):
        selectedRow = self.tree.focus()
        selectedRowId = self.tree.item(selectedRow)['values'][0]
        
        self.txtProductId.delete('0', 'end')
        self.txtProductName.delete('0', 'end')
        self.txtProductQuantity.delete('0', 'end')
        self.txtProductPrice.delete('0', 'end')
        self.txtProductCategory.delete('0', 'end')
        self.txtProductSupplier.delete('0', 'end')
        
        for product in self.productDataList:
            if product[0] == selectedRowId:
                self.txtProductId.insert('0', product[0])   
                self.txtProductName.insert('0', product[1])
                self.txtProductPrice.insert('0', product[2])
                self.txtProductQuantity.insert('0', product[3])
                self.txtProductSupplier.insert('0', product[4])
                self.txtProductCategory.insert('0', product[5])
                
                self.productImage = ImageTk.PhotoImage(Image.open(product[6]).resize((100, 100)))
                self.txtProductImage = Label(self.frameGrid2, image=self.productImage)
                self.txtProductImage.grid(row=0, column=5, padx=10, rowspan=3)