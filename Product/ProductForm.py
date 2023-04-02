from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, SOLID, Listbox, END, Canvas, StringVar, Toplevel
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Button, Separator
from PIL import Image, ImageTk
from os import listdir
import tkinter.messagebox as mbox
import math
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Order import OrderForm
from Cart import Cart, CartForm
from Admin.AdminAccount import AdAccount

try:
    from .Product import *
except:
    from Product import *

class ProductForm(Toplevel):
    def __init__(self, parent, userId, username):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.userId = userId
        self.username = username
        
        objProduct = ProductData()
        self.listAllProduct = objProduct.getProductList("Tất cả")
        
        self.account = AdAccount.AdAccountData()
        self.accountId = self.account.getAccountId(self.username)
        
        self.protocol('WM_DELETE_WINDOW', self.closeAll)
        
        self.initUI()
    
    def closeAll(self):
        self.parent.destroy()
        exit()
    
    def canvasScroll(self, e):
        self.canvas.yview_scroll(int(-1*(e.delta/120)), "units")
    
    def initUI(self):
        # Tạo frame1 chứa thanh tìm kiếm
        self.frame1 = Frame(self, padding=15)
        self.frame1.pack(fill=BOTH)

        self.frame1Left = Frame(self.frame1)
        self.frame1Left.pack(side=LEFT, fill=BOTH)

        self.frameGrid1 = Frame(self.frame1Left)
        self.frameGrid1.grid(column=0, row=0)

        self.lbSearch = Label(self.frameGrid1, text="Tìm kiếm: ", font=('Arial', 12))
        self.lbSearch.grid(column=0, row=0)

        self.inputSearch = Entry(self.frameGrid1, width=50)
        self.inputSearch.grid(column=1, row=0, padx=(5, 3), ipady=3)
        self.inputSearch.bind('<KeyRelease>', self.handleSearchProduct)

        self.LinkImg = Image.open("./img/search_icon.png")
        self.resize_image = self.LinkImg.resize((35, 35))
        self.photo = ImageTk.PhotoImage(self.resize_image)
        self.imgSearch = Label(self.frameGrid1, image=self.photo)
        self.imgSearch.image = self.photo
        self.imgSearch.grid(column=2, row=0)

        # Right frame
        self.frame1Right = Frame(self.frame1)
        self.frame1Right.pack(side=RIGHT, fill=BOTH)

        # Username
        self.usernameBox = Frame(self.frame1Right)
        self.usernameBox.grid(row=0, column=0)
        
        self.lblHello = Label(self.usernameBox, text='Xin chào, ')
        self.lblHello.grid(row=0, column=0, sticky='s')
        
        self.lblUsername = Label(self.usernameBox, text=self.username, font=('Arial', 10, 'bold'))
        self.lblUsername.grid(row=0, column=1, sticky='s')
        
        # Cart
        self.cartImage = ImageTk.PhotoImage(Image.open('./img/cart_icon.png').resize((40, 40)))
        self.cartImg = Label(self.frame1Right, image=self.cartImage, cursor='hand2')
        self.cartImg.grid(row=0, column=1, padx=16)
        self.cartImg.bind('<Button-1>', lambda x: self.toCartPage())

        # Order
        self.orderImage = ImageTk.PhotoImage(Image.open("./img/order_icon2.png").resize((40, 35)))
        self.orderImg = Label(self.frame1Right, image=self.orderImage, cursor='hand2')
        self.orderImg.grid(row=0, column=2, padx=(0, 16))
        self.orderImg.bind('<Button-1>', lambda x: self.toOrderPage())
        
        # Separator
        self.separatorSearch = Separator(self, orient='horizontal')
        self.separatorSearch.pack(fill=BOTH)
        
        # Tạo frame2
        self.frame2 = Frame(self)
        self.frame2.pack(fill=BOTH, expand=True)

        # Tạo frame pack() chứa BA label chung
        self.frameLabel = Frame(self.frame2)
        self.frameLabel.pack(fill=BOTH)

        # Tạo frame label1
        self.frameLabel1 = Frame(self.frameLabel)
        self.frameLabel1.pack(fill=BOTH, side=LEFT, padx=(3, 13), pady=(15, 0))
        self.lb1 = Label(self.frameLabel1, text="Hãng", font=("Times New Roman", 16, 'bold'), width=15, anchor='c')
        self.lb1.pack(padx=12)
        
        # Separator
        self.separatorCate = Separator(self.frameLabel, orient='vertical')
        self.separatorCate.pack(side=LEFT, fill=BOTH)
        
        # Tạo frame label2
        self.frameLabel2 = Frame(self.frameLabel)
        self.frameLabel2.pack(fill=BOTH, expand=True, side=LEFT, padx=15, pady=(15, 0))
        self.lb2 = Label(self.frameLabel2, text="Tất cả sản phẩm", font=("Times New Roman", 16, 'bold'), anchor="c")
        self.lb2.pack(fill=BOTH)

        # Tạo frame pack() chứa list box và phần sản phẩm và giỏ hàng
        self.frameList = Frame(self.frame2)
        self.frameList.pack(fill=BOTH, expand=True)

        # Tạo frame list box
        self.frameListBox = Frame(self.frameList)
        self.frameListBox.pack(fill=BOTH, side=LEFT, pady=(20, 0), padx=(15, 82))

        self.initFilter()
        
        # Separator
        self.separatorProduct = Separator(self.frameList, orient='vertical')
        self.separatorProduct.pack(side=LEFT, fill=BOTH)
        
        # Tạo frame list sản phẩm
        self.frameListProduct = Frame(self.frameList)
        self.frameListProduct.pack(fill=BOTH, side=LEFT, pady=(15, 0), padx=15)

        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvas = Frame(self.frameListProduct)
        self.frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = Canvas(self.frame_canvas, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="news")
        
        # Link a scrollbar to the canvas
        self.vsb = Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_buttons = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        self.renderProductList("Tất cả")

        self.frame_buttons.update_idletasks()
        self.frame_canvas.config(width=930 + self.vsb.winfo_width(), height=410)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        self.canvas.bind_all('<MouseWheel>', self.canvasScroll)
        self.canvas.focus_set()

    def initFilter(self):
        self.lblAll = Label(self.frameListBox, text='Tất cả', font=('Arial 12'), cursor='hand2')
        self.lblAll.grid(row=0, column=0, sticky='w', pady=(4, 12))
        self.lblAll.bind('<Button-1>', lambda x: self.on_select('Tất cả'))
        self.lblAll.bind('<Enter>', self.onHover)
        self.lblAll.bind('<Leave>', self.outHover)
        
        self.lblNike = Label(self.frameListBox, text='Nike', font=('Arial 12'), cursor='hand2')
        self.lblNike.grid(row=1, column=0, sticky='w', pady=(4, 12))
        self.lblNike.bind('<Button-1>', lambda x: self.on_select('Nike'))
        self.lblNike.bind('<Enter>', self.onHover)
        self.lblNike.bind('<Leave>', self.outHover)
        
        self.lblBalenciaga = Label(self.frameListBox, text='Balenciaga', font=('Arial 12'), cursor='hand2')
        self.lblBalenciaga.grid(row=2, column=0, sticky='w', pady=(4, 12))
        self.lblBalenciaga.bind('<Button-1>', lambda x: self.on_select('Balenciaga'))
        self.lblBalenciaga.bind('<Enter>', self.onHover)
        self.lblBalenciaga.bind('<Leave>', self.outHover)
        
        self.lblAddidas = Label(self.frameListBox, text='Addidas', font=('Arial 12'), cursor='hand2')
        self.lblAddidas.grid(row=3, column=0, sticky='w', pady=(4, 12))
        self.lblAddidas.bind('<Button-1>', lambda x: self.on_select('Addidas'))
        self.lblAddidas.bind('<Enter>', self.onHover)
        self.lblAddidas.bind('<Leave>', self.outHover)
        
        self.lblGucci = Label(self.frameListBox, text='Gucci', font=('Arial 12'), cursor='hand2')
        self.lblGucci.grid(row=4, column=0, sticky='w', pady=(4, 12))
        self.lblGucci.bind('<Button-1>', lambda x: self.on_select('Gucci'))
        self.lblGucci.bind('<Enter>', self.onHover)
        self.lblGucci.bind('<Leave>', self.outHover)
        
        self.lblVans = Label(self.frameListBox, text='Vans', font=('Arial 12'), cursor='hand2')
        self.lblVans.grid(row=5, column=0, sticky='w', pady=(4, 12))
        self.lblVans.bind('<Button-1>', lambda x: self.on_select('Vans'))
        self.lblVans.bind('<Enter>', self.onHover)
        self.lblVans.bind('<Leave>', self.outHover)
        
        self.lblConverse = Label(self.frameListBox, text='Converse', font=('Arial 12'), cursor='hand2')
        self.lblConverse.grid(row=6, column=0, sticky='w', pady=(4, 12))
        self.lblConverse.bind('<Button-1>', lambda x: self.on_select('Converse'))
        self.lblConverse.bind('<Enter>', self.onHover)
        self.lblConverse.bind('<Leave>', self.outHover)
        
        self.lblJordan = Label(self.frameListBox, text='Jordan', font=('Arial 12'), cursor='hand2')
        self.lblJordan.grid(row=7, column=0, sticky='w', pady=(4, 12))
        self.lblJordan.bind('<Button-1>', lambda x: self.on_select('Jordan'))
        self.lblJordan.bind('<Enter>', self.onHover)
        self.lblJordan.bind('<Leave>', self.outHover)
        
        self.lblAsics = Label(self.frameListBox, text='Ascics', font=('Arial 12'), cursor='hand2')
        self.lblAsics.grid(row=8, column=0, sticky='w', pady=(4, 12))
        self.lblAsics.bind('<Button-1>', lambda x: self.on_select('Asics'))
        self.lblAsics.bind('<Enter>', self.onHover)
        self.lblAsics.bind('<Leave>', self.outHover)
        
        self.logoutBox = Frame(self.frameListBox)
        self.logoutBox.grid(row=9, column=0, sticky='ws', pady=(50, 0))
        
        self.logoutImage = ImageTk.PhotoImage(Image.open('./img/logout_icon.png').resize((30, 30)))
        self.logoutImg = Label(self.logoutBox, image=self.logoutImage, cursor='hand2')
        self.logoutImg.grid(row=0, column=0)
        self.logoutImg.bind('<Button-1>', lambda x: self.Logout())
        
        self.lblLogout = Label(self.logoutBox, text='Đăng xuất', font=('Arial 11'), cursor='hand2')
        self.lblLogout.grid(row=0, column=1, padx=(8, 0))
        self.lblLogout.bind('<Button-1>', lambda x: self.Logout())
        self.lblLogout.bind('<Enter>', self.onHover)
        self.lblLogout.bind('<Leave>', self.outHover)
        
    # Xử lý logic tìm kiếm sản phẩm trên thanh search và render theo giá trị nhập từ text field
    def handleSearchProduct(self, event):
        objProduct = ProductData()
        text = event.widget.get()
        filtered_list = []
        
        for item in self.listAllProduct:
            if (text.strip().lower() in item[1].lower()):
                filtered_list.append(item)
                
        for widget in self.frame_buttons.winfo_children():
            widget.destroy()
            
        columns = 5
        rows = math.ceil(len(filtered_list) / columns)
        count = 0
        for i in range(0, rows):
            for j in range(0, columns):
                if (count < len(filtered_list)):
                    # tạo item
                    item = Frame(self.frame_buttons)
                    item.grid(column=j, row=i, padx=(5, 24), pady=(25, 0))
                    
                    # xử lý image
                    for f in listdir("img/product"):
                        if (filtered_list[count][0] == f.split(".")[0]):
                            # print(f.split(".")[0])
                            LinkImg = Image.open(f'./img/product/{f}')
                            resize_image = LinkImg.resize((150, 160))
                            photo = ImageTk.PhotoImage(resize_image)
                            img = Label(item, image=photo, borderwidth=1, relief="solid")
                            img.image = photo
                            img.grid(column=0, row=0)

                    productName = Label(item, text=f'{filtered_list[count][1]}', font=("Times New Roman", 12))
                    productName.grid(row=1, column=0)

                    productPrice = Label(item, text=f'Giá: {filtered_list[count][2]}', font=("Times New Roman", 12))
                    productPrice.grid(row=2, column=0)

                    n = StringVar()
                    productCombobox = Combobox(item, textvariable=n, state='readonly')

                    # Adding combobox drop down list
                    arrSizeOfProduct = objProduct.getSizeAndQuantity(filtered_list[count][1])
                    tupleSize = ()
                    for index, value in enumerate(arrSizeOfProduct):
                        if (int(value[1]) > 0):
                            tupleSize = tupleSize + (value[0],)
                    productCombobox['values'] = tupleSize

                    productCombobox.grid(row=3, column=0, pady=(0, 8))

                    btn = Button(item, text="Add cart", command=self.getValueClicked(
                        filtered_list[count][0], filtered_list[count][1], n), cursor='hand2')

                    btn.grid(row=4, column=0, pady=(0, 10))
                    count = count + 1
                else:
                    break
         
    # Hàm render các sản phẩm dựa vào điều kiện là hãng nào, hay tất cả luôn
    def renderProductList(self, condition):
        objProduct = ProductData()
        listProduct = objProduct.getProductList(condition)

        columns = 5
        rows = math.ceil(len(listProduct) / columns)
        count = 0
        for i in range(0, rows):
            for j in range(0, columns):
                if (count < len(listProduct)):
                    # tạo item
                    item = Frame(self.frame_buttons)
                    item.grid(column=j, row=i, padx=(5, 24), pady=(0, 25))
                    
                    # xử lý image
                    for f in listdir("img/product"):
                        if (listProduct[count][0] == f.split(".")[0]):
                            LinkImg = Image.open(f'./img/product/{f}')
                            resize_image = LinkImg.resize((150, 160))
                            photo = ImageTk.PhotoImage(resize_image)
                            img = Label(item, image=photo, borderwidth=1, relief="solid")
                            img.image = photo
                            img.grid(column=0, row=0)
                    
                    name = listProduct[count][1]
                    name = name[:20] + "..." if len(name) > 20 else name
                            
                    productName = Label(item, text=name, font=("Times New Roman", 12))
                    productName.grid(row=1, column=0)

                    productPrice = Label(item, text=f'Giá: {listProduct[count][2]}', font=("Times New Roman", 12))
                    productPrice.grid(row=2, column=0)
    
                    n = StringVar()
                    productCombobox = Combobox(item, textvariable=n, state='readonly')

                    # Adding combobox drop down list
                    arrSizeOfProduct = objProduct.getSizeAndQuantity(listProduct[count][1])
                    tupleSize = ()
                    for index, value in enumerate(arrSizeOfProduct):
                        if (int(value[1]) > 0):
                            tupleSize = tupleSize + (value[0],)
                    
                    tupleSize = list(tupleSize)
                    tupleSize.insert(0, 'Size')
                    tupleSize = tuple(tupleSize)
                        
                    productCombobox['values'] = tupleSize
                    productCombobox.grid(row=3, column=0, pady=(0, 8))
                    productCombobox.current(0)
                    
                    btn = Button(item, text="Add cart", command=self.getValueClicked(
                        listProduct[count][0], listProduct[count][1], n), cursor='hand2')

                    btn.grid(row=4, column=0, pady=(0, 10))
                    count = count + 1
                else:
                    break
            
    # Hàm xử lý logic lấy tất cả thông tin sản phẩm khi click button add
    def getValueClicked(self, productID, name, size_var):
        def handle_event():
            size = size_var.get()
            self.handleEventCart(productID, name, size)
        return handle_event

    # Hàm xử lý logic lấy giá trị khi selected combobox hãng sản xuất và render theo hãng tương ứng
    def on_select(self, name):
        for widget in self.frame_buttons.winfo_children():
            widget.destroy()
            
        self.renderProductList(name)

    # hàm này để xử lý click button add cart để thêm sản phẩm vào list cart
    def handleEventCart(self, productID, name, size):
        objCart = Cart.CartData()
        cartList = objCart.getCartList(self.accountId)
        
        if size == "" or size == "Size":
            mbox.showerror("Error", "Vui lòng chọn size")
            return
        
        if len(cartList) == 0:
            quantity = 1
            objCart.addCart(quantity, size, self.accountId, productID)
        else:
            flag = False
            for cart in cartList:
                if cart[1] == name and cart[3] == size:
                    cart[4] = int(cart[4]) + 1
                    objCart.deleteCart(cart[0])
                    objCart.addCart(cart[4], cart[3], self.accountId, cart[0])
                    flag = True
                    break
                
            if flag == False:
                count = 1
                objCart.addCart(count, size, self.accountId, productID)          
        
        mbox.showinfo('Success', 'Đã thêm sản phẩm này vào giỏ hàng')
        
    def onHover(self, e):
        e.widget['foreground'] = '#fd6032'
    
    def outHover(self, e):
        e.widget['foreground'] = 'black'
    
    def Logout(self):
        self.parent.page.destroy()
        self.parent.deiconify()

    def toOrderPage(self):
        self.parent.page.orderPage = OrderForm.OrderForm(parent=self.parent.page, userId=self.userId)
        self.parent.page.orderPage.geometry('1200x600+180+100')
        self.parent.page.orderPage.title('Đơn hàng đã đặt')
        self.parent.page.orderPage.resizable(False, False)
        self.parent.page.withdraw()
        
    def toCartPage(self):
        self.parent.page.cartPage = CartForm.CartForm(parent=self.parent.page, accountId=self.accountId)
        self.parent.page.cartPage.geometry('1200x600+180+100')
        self.parent.page.cartPage.title('Đơn đặt hàng')
        self.parent.page.cartPage.resizable(False, False)
        self.parent.page.withdraw()
        
    def onBackProductPage(self):
        self.canvas.bind_all('<MouseWheel>', self.canvasScroll)