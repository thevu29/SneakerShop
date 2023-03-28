from PIL import Image, ImageTk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, SOLID, Listbox, END, Canvas, StringVar, Toplevel
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Button
import tkinter.messagebox as mbox
import math
from pathlib import Path
from os import listdir
from os.path import isfile, join

try:
    from Product import ProductData
except:
    from Product.Product import ProductData

class ProductForm(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        
        self.protocol('WM_DELETE_WINDOW', self.closeAll)
        
        self.initUI()
    
    def closeAll(self):
        self.parent.destroy()
       
    def initUI(self):
        # Tạo frame1 chứa thanh tìm kiếm
        self.frame1 = Frame(self, padding=15, border=10, borderwidth=5, relief="solid")
        self.frame1.pack(fill=BOTH)

        self.frame1Left = Frame(self.frame1)
        self.frame1Left.pack(side=LEFT, fill=BOTH)

        self.frameGrid1 = Frame(self.frame1Left)
        self.frameGrid1.grid(column=3, row=1)

        self.lbSearch = Label(self.frameGrid1, text="Tìm kiếm: ")
        self.lbSearch.grid(column=0, row=0)

        self.inputSearch = Entry(self.frameGrid1, width=50)
        self.inputSearch.grid(column=1, row=0, padx=(5, 3))
        self.inputSearch.bind('<KeyRelease>', self.handleSearchProduct)

        self.LinkImg = Image.open("./img/search_icon.png")
        self.resize_image = self.LinkImg.resize((35, 35))
        self.photo = ImageTk.PhotoImage(self.resize_image)
        self.imgSearch = Label(self.frameGrid1, image=self.photo)
        self.imgSearch.image = self.photo
        self.imgSearch.grid(column=2, row=0)

        self.frame1Right = Frame(self.frame1)
        self.frame1Right.pack(side=RIGHT, fill=BOTH)

        self.LinkImg = Image.open("./img/icon-order.png")
        self.resize_image = self.LinkImg.resize((40, 35))
        self.photo = ImageTk.PhotoImage(self.resize_image)
        self.imgOrder = Label(self.frame1Right, image=self.photo)
        self.imgOrder.image = self.photo
        self.imgOrder.pack(side=RIGHT)

        # Tạo frame2
        self.frame2 = Frame(self)
        self.frame2.pack()

        # Tạo frame pack() chứa BA label chung
        self.frameLabel = Frame(self.frame2)
        self.frameLabel.pack()

        # Tạo frame label1
        self.frameLabel1 = Frame(self.frameLabel)
        self.frameLabel1.pack(fill=BOTH, side=LEFT, padx=15, pady=15)
        self.lb1 = Label(self.frameLabel1, text="Hãng sản xuất", padding=12, font=("Times New Roman", 16), background="gray")
        self.lb1.pack()
        # Tạo frame label2
        self.frameLabel2 = Frame(self.frameLabel, borderwidth=1, relief=SOLID)
        self.frameLabel2.pack(side=LEFT, padx=15, pady=15)
        self.lb2 = Label(self.frameLabel2, text="Tất cả sản phẩm", padding=12, font=("Times New Roman", 16), background="gray", anchor="c", width=57)
        self.lb2.pack()
        # Tao frame Label3
        self.frameLabel3 = Frame(self.frameLabel)
        self.frameLabel3.pack(side=LEFT, padx=15, pady=15)
        self.lb3 = Label(self.frameLabel3, text="Giỏ hàng", padding=12, font=("Times New Roman", 16), background="gray", anchor="c", width=100)
        self.lb3.pack()

        # Tạo frame pack() chứa list box và phần sản phẩm và giỏ hàng
        self.frameList = Frame(self.frame2)
        self.frameList.pack(fill=BOTH, expand=True)

        # Tạo frame list box
        self.frameListBox = Frame(self.frameList)
        self.frameListBox.pack(fill=BOTH, side=LEFT, pady=22, padx=(15, 5))

        list = ["Tất cả", "Nike", "Balenciaga", "Gucci"]
        lb = Listbox(self.frameListBox, width=24)
        lb.pack()
        for i in list:
            lb.insert(END, i)

        # Tạo frame list sản phẩm
        self.frameListProduct = Frame(self.frameList)
        self.frameListProduct.pack(fill=BOTH, side=LEFT, pady=15, padx=15)

        self.mainFrameGridProduct = Frame(self.frameListProduct)
        self.mainFrameGridProduct.grid()

        self.frame_main = Frame(self.mainFrameGridProduct)
        self.frame_main.grid(sticky='news')

        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvas = Frame(self.frame_main)
        self.frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = Canvas(self.frame_canvas)
        self.canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        self.vsb = Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_buttons = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        self.renderProductList("Tất cả")
        lb.bind('<<ListboxSelect>>', self.on_select)

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.frame_buttons.update_idletasks()
        
        # chuẩn ban đầu
        self.frame_canvas.config(width=652 + self.vsb.winfo_width(), height=400)
        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Tạo frame list cart
        self.frameListCart = Frame(self.frameList)
        self.frameListCart.pack(fill=BOTH, side=LEFT)

        # tạo frame grid chứa toàn bộ item sản phẩm khi thêm vào cart
        self.frame_mainCart = Frame(self.frameListCart)
        self.frame_mainCart.grid(sticky='news')

        # Create a frame for the canvas with non-zero row&column weights
        self.frame_canvasCart = Frame(self.frame_mainCart)
        self.frame_canvasCart.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvasCart.grid_rowconfigure(0, weight=1)
        self.frame_canvasCart.grid_columnconfigure(0, weight=1)
        self.frame_canvasCart.grid_propagate(False)

        # Add a canvas in that frame
        self.canvasCart = Canvas(self.frame_canvasCart)
        self.canvasCart.grid(row=0, column=0, sticky="news", pady=14)

        # Link a scrollbar to the canvas
        self.vsbCart = Scrollbar(self.frame_canvasCart, orient="vertical", command=self.canvasCart.yview)
        self.vsbCart.grid(row=0, column=1, sticky='ns', pady=14)
        self.canvasCart.configure(yscrollcommand=self.vsbCart.set)

        # Create a frame to contain the buttons
        self.frame_buttonsCart = Frame(self.canvasCart)
        self.canvasCart.create_window((0, 0), window=self.frame_buttonsCart, anchor='nw')

        # xử lý cart
        self.listCart = []

        # self.frame_buttonsCart.update_idletasks()
        self.frame_canvasCart.config(width=330 + self.vsbCart.winfo_width(), height=400)

        # Tạo frame show tổng tiền và button đặt hàng
        self.frameTotalGrid = Frame(self.frameListCart)
        self.frameTotalGrid.grid(pady=5)
        self.lbTotal = Label(self.frameTotalGrid, text="Tổng tiền:", font=('TimesNewRoman 12 bold'))
        self.lbTotal.grid(row=0, column=0)
        
        self.lbTotalPrice = Label(self.frameTotalGrid, text="", font=("Times New Roman", 14))
        self.lbTotalPrice.grid(row=0, column=1, padx=10)
        self.btnBuy = Button(self.frameTotalGrid, text="Đặt hàng")
        self.btnBuy.grid(row=0, column=2)

        # Tạo đối tượng để lấy hết dữ liệu về sản phẩm database lưu vào list để tái sử dụng
        objProduct = ProductData()
        self.listAllProduct = objProduct.getProductList("Tất cả")

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
            
        columns = 3
        rows = math.ceil(len(filtered_list) / columns)
        count = 0
        for i in range(0, rows):
            for j in range(0, columns):
                if (count < len(filtered_list)):
                    # tạo item
                    item = Frame(self.frame_buttons)
                    item.grid(column=j, row=i, padx=(5, 40), pady=(0, 25))
                    
                    # xử lý image
                    for f in listdir("img/product"):
                        if (filtered_list[count][0] == f.split(".")[0]):
                            # print(f.split(".")[0])
                            LinkImg = Image.open(f'./img/product/{f}')
                            resize_image = LinkImg.resize((150, 160))
                            photo = ImageTk.PhotoImage(resize_image)
                            img = Label(item, image=photo,
                                        borderwidth=1, relief="solid")
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
                        f"./img/product/{filtered_list[count][0]}.png", filtered_list[count][1], filtered_list[count][2], n), cursor='hand2')

                    btn.grid(row=4, column=0, pady=(0, 10))
                    count = count + 1
                else:
                    break

    # Hàm render các sản phẩm dựa vào điều kiện là hãng nào, hay tất cả luôn
    def renderProductList(self, condition):
        objProduct = ProductData()
        listProduct = objProduct.getProductList(condition)

        columns = 3
        rows = math.ceil(len(listProduct) / columns)
        count = 0
        for i in range(0, rows):
            for j in range(0, columns):
                if (count < len(listProduct)):
                    # # tạo item
                    item = Frame(self.frame_buttons)
                    item.grid(column=j, row=i, padx=(5, 40), pady=(0, 25))
                    
                    # xử lý image
                    for f in listdir("img/product"):
                        if (listProduct[count][0] == f.split(".")[0]):
                            LinkImg = Image.open(f'./img/product/{f}')
                            resize_image = LinkImg.resize((150, 160))
                            photo = ImageTk.PhotoImage(resize_image)
                            img = Label(item, image=photo,
                                        borderwidth=1, relief="solid")
                            img.image = photo
                            img.grid(column=0, row=0)
                            
                    productName = Label(item, text=f'{listProduct[count][1]}', font=("Times New Roman", 12))
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
                    productCombobox['values'] = tupleSize
                    # selected_value = n.get()

                    productCombobox.grid(row=3, column=0, pady=(0, 8))
                    
                    btn = Button(item, text="Add cart", command=self.getValueClicked(
                        f"./img/product/{listProduct[count][0]}.png", listProduct[count][1], listProduct[count][2], n), cursor='hand2')

                    btn.grid(row=4, column=0, pady=(0, 10))
                    count = count + 1
                else:
                    break

    # Hàm xử lý logic lấy tất cả thông tin sản phẩm khi click button add
    def getValueClicked(self, img, name, price, size_var):
        def handle_event():
            size = size_var.get()
            self.handleEventCart(img, name, price, size)
        return handle_event

    # Hàm xử lý logic lấy giá trị khi selected combobox hãng sản xuất và render theo hãng tương ứng
    def on_select(self, event):
        # Lấy index của phần tử được chọn
        index = event.widget.curselection()[0]
        
        # Lấy giá trị của phần tử được chọn
        value = event.widget.get(index)
        
        # destroy các phần tử hiện tại để render
        for widget in self.frame_buttons.winfo_children():
            widget.destroy()
            
        self.renderProductList(value)

    # hàm này để xử lý click button add cart để thêm sản phẩm  vào list cart
    def handleEventCart(self, produtImg, name, price, size):
        flag = False
        if (size == ""):
            mbox.showerror("Error", "Vui lòng chọn size")
            return
        if (len(self.listCart) <= 0):
            product = []
            count = 1
            product.append(produtImg)
            product.append(name)
            product.append(price)
            product.append(size)
            product.append(count)
            self.listCart.append(product)
        else:
            for i in self.listCart:
                if (i[1] == name and i[3] == size):
                    i[4] = i[4] + 1
                    flag = True
                    break
            if (flag == False):
                product = []
                count = 1
                product.append(produtImg)
                product.append(name)
                product.append(price)
                product.append(size)
                product.append(count)
                self.listCart.append(product)

        self.renderListCart()

    # Xử lý render giỏ hàng lấy từ list cart
    def renderListCart(self):
        for widget in self.frame_buttonsCart.winfo_children():
            widget.destroy()

        for index, value in enumerate(self.listCart):
            itemCart = Frame(self.frame_buttonsCart)
            itemCart.grid(row=index, column=0, pady=(0, 30))
            itemDetail = Frame(self.frame_buttonsCart)
            itemDetail.grid(row=index, column=1, padx=(10, 0))
            LinkImg = Image.open(value[0])

            resize_image = LinkImg.resize((140, 140))
            photo = ImageTk.PhotoImage(resize_image)
            img = Label(itemCart, image=photo, borderwidth=1, relief="solid")
            img.image = photo
            img.grid(column=0, row=0, rowspan=3)

            btnDelete = Button(itemCart, text="Xóa", font=("Times New Roman", 10), command=self.getValueDel(value[1], value[3]), cursor='hand2')
            btnDelete.grid(column=0, row=3, pady=(8, 0))

            productName = Label(itemDetail, text=value[1], font=("Times New Roman", 12))
            productName.grid(row=0, column=0)
            
            productPrice = Label(itemDetail, text=f'Giá: {value[2]}', font=("Times New Roman", 12))
            productPrice.grid(row=1, column=0)
            
            productSize = Label(itemDetail, text=f'Size: {value[3]}', font=("Times New Roman", 12))
            productSize.grid(row=2, column=0)
            
            productAmount = Label(itemDetail, text=f'Số lượng: X{value[4]}', font=("Times New Roman", 12))
            productAmount.grid(row=3, column=0)
            
            self.frame_buttonsCart.update_idletasks()
            self.canvasCart.config(scrollregion=self.canvasCart.bbox("all"))

        total = 0
        for index, value in enumerate(self.listCart):
            total = total + (float(value[2])*float(value[4]))

        self.lbTotalPrice['text'] = str(total)

    # Hàm lấy thông tin của sp cần xóa
    def getValueDel(self, name, size):
        def handle_event():
            self.handleDelProduct(name, size)
        return handle_event
    
    # Hàm xóa sp khỏi list cart
    def handleDelProduct(self, name, size):
        for item in self.listCart:
            if (name in item[1] and size in item[3]):
                self.listCart.remove(item)
        self.renderListCart()