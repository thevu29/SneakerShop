import tkinter as tk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, SOLID, Listbox, END, Canvas, StringVar, Toplevel
from tkinter.ttk import Frame, Label, Entry, Combobox, Entry, Treeview, Scrollbar, Button, Separator, Style
from PIL import Image, ImageTk

class CartForm(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        
        self.protocol('WM_DELETE_WINDOW', self.closeAll)
        
        self.initUI()
    
    def closeAll(self):
        self.parent.destroy()
    
    def canvasScroll(self, e):
        self.cartProductCanvas.yview_scroll(int(-1*(e.delta/120)), "units")
    
    def initUI(self):
        self.initHeader()
        
        self.headerSeparator = Separator(self, orient='horizontal')
        self.headerSeparator.pack(fill=BOTH)
        
        # Content Form
        self.contentForm = Frame(self)
        self.contentForm.pack(fill=BOTH, expand=True, padx=(24, 0))
        
        self.initUserInfoForm()
        
        self.userFormSeparator = Separator(self.contentForm, orient='vertical')
        self.userFormSeparator.pack(side=LEFT, fill=BOTH, padx=(32, 0))
        
        self.initCartForm()
    
    def initHeader(self):
        self.header = Frame(self)
        self.header.pack(fill=BOTH, pady=24)
        
        self.lblHeader = Label(self.header, text='Đơn đặt hàng', font=('Arial', 20, 'bold'), anchor='c')
        self.lblHeader.pack()
    
    def initUserInfoForm(self):
        self.userInfoForm = Frame(self.contentForm)
        self.userInfoForm.pack(fill=BOTH, side=LEFT, pady=24, padx=(0, 130))
        
        # User name
        self.lblUserName = Label(self.userInfoForm, text='Họ và tên:', font=('Arial', 10))
        self.lblUserName.grid(row=0, column=0, sticky='w')
        
        self.txtUserName = Entry(self.userInfoForm, width=50)
        self.txtUserName.grid(row=0, column=1, padx=10, pady=12, ipady=3, sticky='w')
        
        # Gender
        self.lblGender = Label(self.userInfoForm, text='Giới tính:', font=('Arial', 10))
        self.lblGender.grid(row=1, column=0, sticky='w')
        
        self.cbxGender = Combobox(self.userInfoForm, state='readonly', values=('Nam', 'Nữ'), width=40)
        self.cbxGender.grid(row=1, column=1, padx=10, pady=12, ipady=3, sticky='w')
        self.cbxGender.current(0)
        
        # Phone
        self.lblPhone = Label(self.userInfoForm, text='Số điện thoại:', font=('Arial', 10))
        self.lblPhone.grid(row=2, column=0, sticky='w')
        
        self.txtPhone = Entry(self.userInfoForm, width=50)
        self.txtPhone.grid(row=2, column=1, padx=10, pady=12, ipady=3, sticky='w')
        
        # Address
        self.lblAddress = Label(self.userInfoForm, text='Địa chỉ:', font=('Arial', 10))
        self.lblAddress.grid(row=3, column=0, sticky='w')
        
        self.txtAddress = Entry(self.userInfoForm, width=50)
        self.txtAddress.grid(row=3, column=1, padx=10, pady=12, ipady=3, sticky='w')
        
        # Order Button
        self.btnOrder = tk.Button(self.userInfoForm, text='Đặt hàng', bg='#0071e3', fg='#fff', cursor='hand2', font=('Arial', 10, 'bold'), borderwidth=0)
        self.btnOrder.grid(row=4, column=0, columnspan=2, pady=(32, 12), ipady=6, sticky='we')
    
    def initCartForm(self):
        self.cartForm = Frame(self.contentForm)
        self.cartForm.pack(fill=BOTH, expand=True, pady=24)
        
        self.cartForm.grid_columnconfigure(0, weight=1)
        
        self.lblCartHeader = Label(self.cartForm, text='Giỏ hàng', font=('Arial', 14, 'bold'))
        self.lblCartHeader.grid(row=0, column=0, padx=24, sticky='w')
        
        self.cartHeaderSeparator = Separator(self.cartForm, orient='horizontal')
        self.cartHeaderSeparator.grid(row=1, column=0, columnspan=2, pady=16, sticky='we')
        
        # Cart product
        self.initCartProductForm()
    
    def initCartProductForm(self):
        self.cartProductCanvas = Canvas(self.cartForm)
        self.cartProductCanvas.grid(row=2, column=0, sticky='nsew', padx=24)
        
        self.scrollbar = Scrollbar(self.cartForm, command=self.cartProductCanvas.yview, orient='vertical')
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        
        self.cartProductCanvas.config(height=350)
        self.cartProductCanvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.cartProductForm = Frame(self.cartProductCanvas)
        self.cartProductForm.grid(row=0, column=0, sticky='we')
        self.cartProductCanvas.create_window((0, 0), window=self.cartProductForm, anchor='nw')
        
        self.renderCartProduct()

        self.cartProductForm.update_idletasks()
        self.cartProductCanvas.configure(scrollregion=self.cartProductCanvas.bbox('all'))
        self.cartProductCanvas.bind_all("<MouseWheel>", self.canvasScroll)
        
        self.productFormSeparator = Separator(self.cartForm)
        self.productFormSeparator.grid(row=3, column=0, columnspan=2, pady=16, sticky='we')
        
        # Total price
        self.totalBox = Frame(self.cartForm)
        self.totalBox.grid(row=4, column=0, columnspan=2, sticky='we')
        self.totalBox.grid_columnconfigure(1, weight=1)
        
        self.lblTotal = Label(self.totalBox, text='Tổng tiền:', font=('Arial', 10, 'bold'))
        self.lblTotal.grid(row=0, column=0, sticky='w', padx=24)
        
        self.totalPrice = Label(self.totalBox, text='3000000', font=('Arial', 10))
        self.totalPrice.grid(row=0, column=1, sticky='e', padx=24)
        
    def renderCartProduct(self):
        self.productBox = Frame(self.cartProductForm)
        self.productBox.grid(row=0, column=1, sticky='we')
        self.cartProductForm.grid_columnconfigure(1, weight=1)
        
        # product image
        self.imageBorder = Frame(self.productBox, borderwidth=1, relief='solid')
        self.imageBorder.grid(row=0, column=0, rowspan=4)
        
        self.productImg = ImageTk.PhotoImage(Image.open('./img/product/SP001.png').resize((100, 100)))
        self.productImage = Label(self.imageBorder, image=self.productImg)
        self.productImage.grid(row=0, column=0)
        
        # product name
        self.producttName = Label(self.productBox, text='Tên: Nike Air Force 1')
        self.producttName.grid(row=0, column=1, padx=12, sticky='w')
        
        # product price
        self.producttPrice = Label(self.productBox, text='Giá: 1500000')
        self.producttPrice.grid(row=1, column=1, padx=12, sticky='w')
        
        # product size
        self.producttSize = Label(self.productBox, text='Size: 40')
        self.producttSize.grid(row=2, column=1, padx=12, sticky='w')
        
        # change quantity box
        self.quantityBox = Frame(self.productBox)
        self.quantityBox.grid(row=3, column=1, padx=12, sticky='w')
        
        self.btnDecrease = Button(self.quantityBox, text='-', width=5, cursor='hand2')
        self.btnDecrease.grid(row=0, column=0)
        
        self.quantity = Entry(self.quantityBox, width=5, justify='center')
        self.quantity.grid(row=0, column=1, padx=12)
        self.quantity.insert(0, '1')
        
        self.btnIncrease = Button(self.quantityBox, text='+', width=5, cursor='hand2')
        self.btnIncrease.grid(row=0, column=2)
        
        # delete product
        self.btnDelete = Button(self.productBox, text='Xóa', width=5, cursor='hand2')
        self.btnDelete.grid(row=5, column=0, pady=(6, 0))
        
        # separtor
        self.productSeparator = Separator(self.productBox, orient='horizontal')
        self.productSeparator.grid(row=6, column=0, columnspan=2, sticky='we', pady=(8, 0))
    
if __name__ == '__main__':
    root = Tk()
    app = CartForm(root)
    app.geometry('1200x600+180+100')
    root.withdraw()
    root.mainloop()