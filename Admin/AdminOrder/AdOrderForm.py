from tkinter import Tk, BOTH, LEFT, VERTICAL
from tkinter.ttk import Label, Frame, Entry, Treeview, Scrollbar, Button, LabelFrame, Combobox
from PIL import Image, ImageTk
try:
    from .GetAdOrderData import *
except:
    from GetAdOrderData import *
    
class AdOrderForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        # header
        frame1 = Frame(self)
        frame1.pack()
        
        header = Label(frame1, text='Quản lý đơn hàng', font=("Time News Roman", 22), foreground="black")
        header.pack(fill=BOTH)
        
        frame2 = LabelFrame(self, text='Chức năng')
        frame2.pack(fill=BOTH, pady=10)
        frame2.config(borderwidth=10, relief='solid')
        
        frame3 = LabelFrame(self, text='Danh sách đơn hàng')
        frame3.pack(fill=BOTH, pady=10)
        frame3.config(borderwidth=10, relief='solid')
        
        self.initFilter(frame2)
        self.initOrderList(frame3)

    def initFilter(self, frame2):
        search = Label(frame2, text='Tìm kiếm:')
        search.grid(row=0, column=0)
        
        def FocIn(entry):   
            print(entry['foreground'])
            if entry['foreground'] == 'gray':
                entry.configure(foreground='black')
                entry.delete(0, 'end')

        def FocOut(entry, placeholder):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.configure(foreground='gray')
        
        searchText = Entry(frame2, width=30)
        searchText.insert(0, 'Nhập mã đơn hàng')
        searchText.grid(row=0, column=1, padx=(5, 10), ipady=2)  
        searchText.config(foreground='gray')
        searchText.bind('<Button-1>', lambda x: FocIn(searchText))
        searchText.bind('<FocusOut>', lambda x: FocOut(searchText, 'Nhập mã đơn hàng'))
        
        self.searchIcon = ImageTk.PhotoImage(Image.open('./Admin/AdminOrder/img/search_icon.png').resize((20, 20)))
        searchIconBtn = Button(frame2, image=self.searchIcon)
        searchIconBtn.grid(row=0, column=2)
        
        months = Combobox(frame2, state='readonly')
        months['values'] = ('Tháng đặt hàng', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        months.current(0)
        months.grid(row=0, column=3, ipady=2, padx=24)
        
        status = Combobox(frame2, state='readonly')
        status['values'] = ('Tình trạng', 'Đã xử lý', 'Chưa xử lý')
        status.current(0)
        status.grid(row=0, column=4, pady=2)
        
        self.addIcon = ImageTk.PhotoImage(Image.open('./Admin/AdminOrder/img/add_icon.png').resize((20, 20)))
        addIconBtn = Button(frame2, image=self.addIcon, text='Thêm đơn hàng', compound=LEFT, width=15)
        addIconBtn.grid(row=0, column=5, ipady=2, padx=24)
        
        changeStatus = Button(frame2, text='Xử lý đơn hàng')
        changeStatus.grid(row=0, column=6, ipady=4)
        
        # for i in range(0, 7):
        #     frame2.grid_columnconfigure(i, weight = 1)
        
    def initOrderList(self, frame3):
        columns = ('orderID', 'customerID', 'orderDate', 'totalPrice', 'status')
        orderList = Treeview(frame3, columns=columns, show='headings')
        orderList.grid(row=0, column=0, sticky='EW')
        
        orderList.heading('orderID', text='Mã đơn hàng')
        orderList.heading('customerID', text='Mã khách hàng')
        orderList.heading('status', text='Tình trạng')
        orderList.heading('orderDate', text='Ngày đặt hàng')
        orderList.heading('totalPrice', text='Tổng tiền')
        
        orderList.column('orderID', width=150)
        orderList.column('customerID', width=150)
        for column in columns:
            orderList.column(column, anchor='c')
    
        self.initOrderData(orderList)
        
        scrollbar = Scrollbar(frame3, orient=VERTICAL, command=orderList.yview)
        orderList.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        for i in range(0, 3):
            frame3.grid_columnconfigure(i, weight = 1)
        
    def initOrderData(self, orderList):        
        order = AdOrderData()
        orderDataList = order.getOrderList()
        for data in orderDataList:
            orderList.insert('', 'end', values=data)