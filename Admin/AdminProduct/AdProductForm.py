from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, StringVar, messagebox
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button, Style
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

        self.productName = Label(self.frameGrid2, text="Tên sản phẩm: ")
        self.productName.grid(row=1, column=0, pady=(25, 0), sticky='w')
        self.txtProductName = Entry(self.frameGrid2, width=30)
        self.txtProductName.grid(row=1, column=1, padx=10, pady=(25, 0))
        
        self.productPrice = Label(self.frameGrid2, text="Đơn giá: ")
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

        self.tblProduct = Treeview(self.framePack3, selectmode='browse')
        self.tblProduct.pack(side=LEFT)

        self.vsb = Scrollbar(self.framePack3, orient="vertical", command=self.tblProduct.yview)

        # self.vsb.pack(side=RIGHT,fill='y')
        self.vsb.pack(side=RIGHT, fill='y')

        self.tblProduct.configure(yscrollcommand=self.vsb.set)

        self.tblProduct["columns"] = ("1", "2", "3", "4", "5", "6")
        self.tblProduct['show'] = 'headings'

        for column in ("1", "2", "3", "4", "5", "6"):
            self.tblProduct.column(column, width=180)
            if column != "2":
                self.tblProduct.column(column, anchor='c', width=150)

        self.tblProduct.heading("1", text="Mã sản phẩm")
        self.tblProduct.heading("2", text="Tên sản phẩm")
        self.tblProduct.heading("3", text="Đơn giá")
        self.tblProduct.heading("4", text="Số lượng")
        self.tblProduct.heading("5", text="Mã nhà cung cấp")
        self.tblProduct.heading("6", text="Mã loại sản phẩm")

        self.initProductData()
        self.tblProduct.bind('<<TreeviewSelect>>', lambda x: self.showProductInfo())
        
        # Tạo frame4
        self.labelFrame4 = LabelFrame(self, text="Chức năng", padding=10)
        self.labelFrame4.pack(pady=12)

        self.frame4 = Frame(self.labelFrame4)
        self.frame4.pack()

        self.frameGrid4 = Frame(self.frame4)
        self.frameGrid4.grid(column=6, row=1)

        self.btnAdd = Button(self.frameGrid4, text="Thêm sản phẩm", width=20, command=self.addProduct)
        self.btnAdd.grid(row=0, column=0, padx=10, ipady=3)
        
        self.btnSave = Button(self.frameGrid4, text="Lưu thông tin", width=20, command=self.saveProductInfo)
        self.btnSave.grid(row=0, column=1, padx=10, ipady=3)
        
        self.btnDelete = Button(self.frameGrid4, text="Xóa sản phẩm", width=20, command=self.deleteProduct)
        self.btnDelete.grid(row=0, column=2, padx=10, ipady=3)

        self.btnresetValue = Button(self.frameGrid4, text="Reset", width=20, command=self.reset)
        self.btnresetValue.grid(row=0, column=3, padx=10, ipady=3)
        
    def initProductData(self):          
        for row in self.tblProduct.get_children():
            self.tblProduct.delete(row)
          
        for data in self.productDataList:
            self.tblProduct.insert('', 'end', values=data)
        
    def showProductInfo(self):        
        try:
            selectedRow = self.tblProduct.focus()
            selectedRowId = self.tblProduct.item(selectedRow)['values'][0]
        except:
            return
        
        self.resetValue()
        
        for product in self.productDataList:
            if product[0] == selectedRowId:
                self.txtProductId.insert('0', product[0])   
                self.txtProductName.insert('0', product[1])
                self.txtProductPrice.insert('0', product[2])
                self.txtProductQuantity.insert('0', product[3])
                self.txtProductSupplier.insert('0', product[4])
                self.txtProductCategory.insert('0', product[5])
                
                try:
                    self.imageBorder = Frame(self.frameGrid2, borderwidth=2, relief='solid')
                    self.imageBorder.grid(row=0, column=5, padx=10, rowspan=3)
                    
                    self.productImage = ImageTk.PhotoImage(Image.open(product[6]).resize((100, 100)))
                    self.txtProductImage = Label(self.imageBorder, image=self.productImage)
                    self.txtProductImage.grid(row=0, column=0)
                except:
                    self.productImage = ImageTk.PhotoImage(Image.open('./img/fallback_img.png').resize((100, 100)))
                    self.txtProductImage = Label(self.imageBorder, image=self.productImage)
                    self.txtProductImage.grid(row=0, column=0)
            
    def validate(self):
        productId = self.txtProductId.get()
        productName = self.txtProductName.get()
        productPrice = self.txtProductPrice.get()
        productQuantity = self.txtProductQuantity.get()
        productCategory = self.txtProductCategory.get()
        productSupplier = self.txtProductSupplier.get()
        
        s = ''
        if (productId == ''):
            s += 'Mã sản phẩm không được để trống \n'
        if (productName == ''):
            s += 'Tên sản phẩm không được để trống \n'
        if (productPrice == ''):
            s += 'Giá sản phẩm không được để trống \n'
        if (productQuantity == ''):
            s += 'Số lượng sản phẩm không được để trống \n'
        if (productCategory == ''):
            s += 'Loại sản phẩm không được để trống \n'
        if (productSupplier == ''):
            s += 'Mã nhà cung cấp sản phẩm không được để trống \n' 
            
        if (len(s) > 0):
            messagebox.showwarning('Warning', s)
            return False
        return True
                    
    def addProduct(self):
        if (self.validate() == False):
            return
        
        productId = self.txtProductId.get()
        productName = self.txtProductName.get()
        productPrice = self.txtProductPrice.get()
        productQuantity = self.txtProductQuantity.get()
        productCategory = self.txtProductCategory.get()
        productSupplier = self.txtProductSupplier.get()
        
        for product in self.productDataList:
            if productId == product[0]:
                messagebox.showwarning('Warning', 'Mã sản phẩm đã tồn tại')
                return
        
        newProduct = [productId, productName, productPrice, productQuantity, productSupplier, productCategory]
        
        self.product.addProduct(newProduct)
        messagebox.showinfo('Thành công', 'Thêm sản phẩm thành công')
        self.reset()
    
    def deleteProduct(self):
        if (self.validate() == False):
            return

        productId = self.txtProductId.get()
        
        for product in self.productDataList:
            if productId == product[0]:
                self.product.deleteProduct(product)
                messagebox.showinfo('Thành công', f'Xóa thành công sản phẩm có mã {productId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã sản phẩm không tồn tại')
    
    def saveProductInfo(self):
        if (self.validate() == False):
            return
        
        productId = self.txtProductId.get()
        productName = self.txtProductName.get()
        productPrice = self.txtProductPrice.get()
        productQuantity = self.txtProductQuantity.get()
        productCategory = self.txtProductCategory.get()
        productSupplier = self.txtProductSupplier.get()
        
        newProduct = [productId, productName, productPrice, productQuantity, productSupplier, productCategory]
        
        for product in self.productDataList:
            if productId == product[0]:
                self.product.updateProductInfo(newProduct)
                messagebox.showinfo('Thành công', f'Sửa thành công thông tin sản phẩm có mã {productId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã sản phẩm không tồn tại')
        
    def resetValue(self):
        self.txtProductId.delete('0', 'end')
        self.txtProductName.delete('0', 'end')
        self.txtProductQuantity.delete('0', 'end')
        self.txtProductPrice.delete('0', 'end')
        self.txtProductCategory.delete('0', 'end')
        self.txtProductSupplier.delete('0', 'end')
        
    def reset(self):
        self.resetValue()
        
        self.imageBorder.grid_remove()
        self.txtProductImage.grid_remove()
        
        self.initProductData()