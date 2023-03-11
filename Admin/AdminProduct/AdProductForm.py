from PIL import Image, ImageTk
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, StringVar
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button

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
        self.lb4.grid(row=1, column=0, pady=25, sticky='w')
        self.input4 = Entry(self.frameGrid2, width=30)
        self.input4.grid(row=1, column=1, padx=10, pady=25)

        self.lb6 = Label(self.frameGrid2, text="Ghi chú: ")
        self.lb6.grid(row=1, column=2, sticky='w', padx=(20, 0))
        self.n = StringVar()
        self.noteCombobox = Combobox(self.frameGrid2, textvariable=self.n)

        # Adding combobox drop down list
        self.noteCombobox['values'] = ("Hàng mới nhập", "hàng cũ")
        self.noteCombobox.grid(row=1, column=3, padx=10, pady=25)

        self.lb7 = Label(self.frameGrid2, text="Mã loại sản phẩm: ")
        self.lb7.grid(row=2, column=0, sticky='w')
        self.input7 = Entry(self.frameGrid2, width=30)
        self.input7.grid(row=2, column=1, padx=10)

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
        # self.tree.column("1",width=0, anchor='c')
        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=150, anchor='c')
        self.tree.column("3", width=120, anchor='c')
        self.tree.column("4", width=80, anchor='c')
        self.tree.column("5", width=100, anchor='c')
        self.tree.column("6", width=180, anchor='c')
        self.tree.column("7", width=100, anchor='c')

        self.tree.heading("1", text="Mã sản phẩm")
        self.tree.heading("2", text="Tên sản phẩm")
        self.tree.heading("3", text="Mã loại sản phẩm")
        self.tree.heading("4", text="Số lượng")
        self.tree.heading("5", text="Đơn giá nhập")
        self.tree.heading("6", text="Hình ảnh")
        self.tree.heading("7", text="Ghi chú")
        self.tree.insert("", 'end', text="L1", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L2", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L3", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L4", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L5", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L6", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L7", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L8", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L9", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L10", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L11", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))
        self.tree.insert("", 'end', text="L12", values=("SP001", "Apple Macbook Air 13",
                         "ML001", "800", "1500000", "E:\Python\QuanLyBanHang", "Hàng mới nhập"))

        # kết thúc frame3

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

    def getValuesTree(self):
        arr = []
        for parent in self.tree.get_children():
            arr.append(self.tree.item(parent)["values"])
        return arr