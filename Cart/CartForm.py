import tkinter as tk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, SOLID, Listbox, END, Canvas, StringVar, Toplevel, messagebox
from tkinter.font import Font
from tkinter.ttk import Frame, Label, Entry, Combobox, Entry, Treeview, Scrollbar, Button, Separator, Style
from PIL import Image, ImageTk

try:
    from .Cart import *
except:
    from Cart import *

class CartForm(Toplevel):
    def __init__(self, parent, accountId):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.accountId = accountId
        
        self.cart = CartData()
        self.cartList = self.cart.getCartList(self.accountId)

        self.protocol('WM_DELETE_WINDOW', self.closeAll)
        
        self.initUI()
    
    def closeAll(self):
        self.parent.destroy()
        exit()
    
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
        
        self.lblHeader = Label(self.header, text='Đơn đặt hàng', font=('Arial', 20, 'bold'), anchor='c', foreground='#0071e3')
        self.lblHeader.pack()
    
    def initUserInfoForm(self):
        self.userInfoForm = Frame(self.contentForm)
        self.userInfoForm.pack(fill=BOTH, side=LEFT, pady=24, padx=(30, 100))
        
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
        
        # back product page
        self.userInfoForm.grid_rowconfigure(5, weight=1)
        
        self.backBox = Frame(self.userInfoForm)
        self.backBox.grid(row=5, column=0, sticky='ws', columnspan=2)
        
        self.leftArrowImg = ImageTk.PhotoImage(Image.open('./img/left_arrow.png').resize((35, 20)))
        self.leftArrow = Label(self.backBox, image=self.leftArrowImg, cursor='hand2')
        self.leftArrow.grid(row=0, column=0)
        
        self.lblproductPage = Label(self.backBox, text='Trở về trang sản phẩm', font=('Arial', 10), cursor='hand2')
        self.lblproductPage.grid(row=0, column=1, padx=4)
        
        self.normalFont = Font(family='Arial', size=10)
        self.underlineFont = Font(family='Arial', size=10, underline=True)
        self.lblproductPage.bind("<Button-1>", lambda x: self.backProductPage())
        self.lblproductPage.bind("<Enter>", self.onHover)
        self.lblproductPage.bind("<Leave>", self.outHover)
    
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
    
    def cartCanvasScroll(self, e):
        self.cartProductCanvas.yview_scroll(int(-1*(e.delta/120)), "units")
    
    def initCartProductForm(self):
        self.cartProductCanvas = Canvas(self.cartForm, highlightthickness=0)
        self.cartProductCanvas.grid(row=2, column=0, sticky='nsew', padx=24)
        
        self.scrollbar = Scrollbar(self.cartForm, command=self.cartProductCanvas.yview, orient='vertical')
        self.scrollbar.grid(row=2, column=1, sticky='ns')
        
        self.cartProductCanvas.config(height=350)
        self.cartProductCanvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.cartProductForm = Frame(self.cartProductCanvas)
        self.cartProductCanvas.create_window((0, 0), window=self.cartProductForm, anchor='nw')
        
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
        
        self.renderCartProduct()
                
        self.cartProductForm.update_idletasks()
        self.cartProductCanvas.configure(scrollregion=self.cartProductCanvas.bbox('all'))
        
        self.cartProductCanvas.bind_all("<MouseWheel>", self.cartCanvasScroll)
        
    def renderCartProduct(self):
        for widget in self.cartProductForm.winfo_children():
            widget.destroy()

        for i in range(0, len(self.cartList)):
            self.productBox = Frame(self.cartProductForm)
            self.productBox.grid(row=i, column=0, sticky='we', pady=(0,24))
            self.cartProductForm.grid_columnconfigure(1, weight=1)
            
            # product image
            self.imageBorder = Frame(self.productBox, borderwidth=1, relief='solid')
            self.imageBorder.grid(row=0, column=0, rowspan=4)
            
            productImg = ImageTk.PhotoImage(Image.open(f'./img/product/{self.cartList[i][0]}.png').resize((100, 100)))
            self.productImage = Label(self.imageBorder, image=productImg)
            self.productImage.image = productImg
            self.productImage.grid(row=0, column=0)
                    
            # product name
            self.producttName = Label(self.productBox, text=f'Tên: {self.cartList[i][1]}')
            self.producttName.grid(row=0, column=1, padx=12, sticky='w')
                
            # product price
            self.producttPrice = Label(self.productBox, text=f'Giá: {self.cartList[i][2]}')
            self.producttPrice.grid(row=1, column=1, padx=12, sticky='w')
                
            # product size
            self.producttSize = Label(self.productBox, text=f'Size: {self.cartList[i][3]}')
            self.producttSize.grid(row=2, column=1, padx=12, sticky='w')
                
            # change quantity box
            self.quantityBox = Frame(self.productBox)
            self.quantityBox.grid(row=3, column=1, padx=12, sticky='w')
                
            self.btnDecrease = Button(self.quantityBox, text='-', width=5, cursor='hand2', command=self.getValueClicked(self.cartList[i][1], self.cartList[i][3], '-'))
            self.btnDecrease.grid(row=0, column=0)
                
            self.quantity = Entry(self.quantityBox, width=5, justify='center')
            self.quantity.grid(row=0, column=1, padx=12)
            self.quantity.insert(0, self.cartList[i][4])
                
            self.btnIncrease = Button(self.quantityBox, text='+', width=5, cursor='hand2', command=self.getValueClicked(self.cartList[i][1], self.cartList[i][3], '+'))
            self.btnIncrease.grid(row=0, column=2)
                
            # delete product
            self.btnDelete = Button(self.productBox, text='Xóa', width=5, cursor='hand2', command=self.getValueClicked(self.cartList[i][1], self.cartList[i][3], 'x'))
            self.btnDelete.grid(row=5, column=0, pady=(6, 0))
            
        total = 0   
        for index, value in enumerate(self.cartList):    
            total += (float(value[2]) * float(value[4]))
            
        self.totalPrice['text'] = '{0:.2f}'.format(total).rstrip('0').rstrip('.')
        self.totalPrice['font'] = ('Arial', 11, 'bold')
        
    def getValueClicked(self, name, size, option):
        def handle_event():
            if option == 'x':
                self.deleteProduct(name, size)
            elif option == '-':
                self.decreaseQuantity(name, size)
            elif option == '+':
                self.increaseQuantity(name, size)
        return handle_event      
        
    def deleteProduct(self, name, size):
        for cart in self.cartList:
            if name == cart[1] and size == cart[3]:
                self.cartList.remove(cart)
                self.cart.deleteCart(cart[0], self.accountId, cart[3])
                break
            
        self.renderCartProduct()
    
    def increaseQuantity(self, name, size):
        for cart in self.cartList:
            if name == cart[1] and size == cart[3]:
                cart[4] = int(cart[4]) + 1
                self.cart.deleteCart(cart[0], self.accountId, cart[3])
                self.cart.addCart(cart[4], cart[3], self.accountId, cart[0])
                break
            
        self.renderCartProduct()
      
    def decreaseQuantity(self, name, size):
        for cart in self.cartList:
            if name == cart[1] and size == cart[3]:
                if int(cart[4]) > 1:
                    cart[4] = int(cart[4]) - 1
                    self.cart.deleteCart(cart[0], self.accountId, cart[3])
                    self.cart.addCart(cart[4], cart[3], self.accountId, cart[0])
                    break
                
        self.renderCartProduct()

    def backProductPage(self):
        self.cartProductCanvas.unbind_all("<MouseWheel>")
        self.parent.cartPage.destroy()
        self.parent.deiconify()
        self.parent.onBackProductPage()
    
    def onHover(self, e):
        e.widget.config(font=self.underlineFont)
        
    def outHover(self, e):
        e.widget.config(font=self.normalFont)
    
# if __name__ == '__main__':
#     root = Tk()
#     app = CartForm(root, 'ACC003')
#     app.geometry('1200x600+180+100')
#     root.withdraw()
#     root.mainloop()