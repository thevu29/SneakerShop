from tkinter import Tk, BOTH, LEFT, VERTICAL, Toplevel, messagebox
from tkinter.ttk import Label, Frame, Entry, Treeview, Scrollbar, Button, LabelFrame, Combobox
from PIL import Image, ImageTk

try:
    from .AdOrder import *
    from .AdOrderDetailForm import *
except:
    from AdOrder import *
    from AdOrderDetailForm import *
    
class AdOrderForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.order = AdOrderData()
        self.orderDataList = self.order.getOrderList()
        
        self.initUI()
        
    def initUI(self):
        # header
        frame1 = Frame(self)
        frame1.pack()
        
        header = Label(frame1, text='Quản lý đơn hàng', font=("Time News Roman", 22), foreground="black")
        header.pack(fill=BOTH)
        
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, pady=30)
        
        frame3 = LabelFrame(self, text='Danh sách đơn hàng')
        frame3.pack(fill=BOTH, pady=10)
        frame3.config(borderwidth=10, relief='solid')
        
        frame4 = LabelFrame(self, text='Chức năng')
        frame4.pack(pady=10)
        frame4.config(borderwidth=10, relief='solid')

        self.initOrderList(frame3)
        self.initFilter(frame2)
        self.initOperation(frame4)

    def initFilter(self, frame2):
        search = Label(frame2, text='Tìm kiếm:', font=('Arial', 12))
        search.grid(row=0, column=0)
        
        def FocIn():   
            print(self.txtSearch['foreground'])
            if self.txtSearch['foreground'] == 'gray':
                self.txtSearch.configure(foreground='black')
                self.txtSearch.delete(0, 'end')

        def FocOut(placeholder):
            if self.txtSearch.get() == '':
                self.txtSearch.insert(0, placeholder)
                self.txtSearch.configure(foreground='gray')
        
        self.txtSearch = Entry(frame2, width=50)
        self.txtSearch.grid(row=0, column=1, padx=(5, 10), ipady=4)  
        
        self.txtSearch.insert(0, 'Nhập mã đơn hàng')
        self.txtSearch.config(foreground='gray')
        self.txtSearch.bind('<Button-1>', lambda x: FocIn())
        self.txtSearch.bind('<FocusOut>', lambda x: FocOut('Nhập mã đơn hàng'))
        
        self.searchIcon = ImageTk.PhotoImage(Image.open('./img/search_icon.png').resize((20, 20)))
        self.btnSearch = Button(frame2, image=self.searchIcon, cursor='hand2', command=self.searchOrderById)
        self.btnSearch.grid(row=0, column=2, padx=(0, 24))
        
        self.cbxMonths = Combobox(frame2, state='readonly')
        self.cbxMonths['values'] = ('Tháng đặt hàng', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        self.cbxMonths.current(0)
        self.cbxMonths.grid(row=0, column=3, ipady=4, padx=24)
        self.cbxMonths.bind('<<ComboboxSelected>>', lambda x: self.filterByMonths())
        
        self.cbxStatus = Combobox(frame2, state='readonly', values=('Tình trạng', 'Đã xử lí', 'Chưa xử lí'))
        self.cbxStatus.current(0)
        self.cbxStatus.grid(row=0, column=4, pady=2, ipady=4, padx=24)
        self.cbxStatus.bind('<<ComboboxSelected>>', lambda x: self.filterByStatus())
        
        # for i in range(0, 7):
        #     frame2.grid_columnconfigure(i, weight = 1)
    
    def initOperation(self, frame4):
        # btnAdd = Button(frame4, text='Thêm đơn hàng', width=20)
        # btnAdd.grid(row=0, column=0, ipady=3, padx=10)
        
        self.btnDelete = Button(frame4, text='Xóa đơn hàng', width=20, cursor='hand2', command=self.deleteOrder)
        self.btnDelete.grid(row=0, column=0, ipady=3, padx=10)
        
        self.btnChangeStatus = Button(frame4, text='Xử lý đơn hàng', width=20, cursor='hand2', command=self.changeOrderStatus)
        self.btnChangeStatus.grid(row=0, column=1, ipady=3, padx=10)
        
        self.btnReset = Button(frame4, text='Reset', width=20, cursor='hand2', command=self.reset)
        self.btnReset.grid(row=0, column=2, ipady=3, padx=10)
        
    def initOrderList(self, frame3):
        columns = ('orderID', 'customerID', 'orderDate', 'totalPrice', 'status')
        self.tblOrder = Treeview(frame3, columns=columns, show='headings')
        self.tblOrder.grid(row=0, column=0, sticky='EW')
        
        self.tblOrder.heading('orderID', text='Mã đơn hàng')
        self.tblOrder.heading('customerID', text='Mã khách hàng')
        self.tblOrder.heading('status', text='Tình trạng')
        self.tblOrder.heading('orderDate', text='Ngày đặt hàng')
        self.tblOrder.heading('totalPrice', text='Tổng tiền')
        
        self.tblOrder.column('orderID', width=150)
        self.tblOrder.column('customerID', width=150)
        for column in columns:
            self.tblOrder.column(column, anchor='c')
    
        self.initOrderData()
        
        scrollbar = Scrollbar(frame3, orient=VERTICAL, command=self.tblOrder.yview)
        self.tblOrder.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        for i in range(0, 3):
            frame3.grid_columnconfigure(i, weight = 1)
        
        self.tblOrder.bind('<Double-1>', lambda x: self.showOrderDetail())
       
    def initOrderData(self):   
        for row in self.tblOrder.get_children():
            self.tblOrder.delete(row)
             
        for data in self.orderDataList:
            self.tblOrder.insert('', 'end', values=data)
            
    def showOrderDetail(self):
        selectedOrder = self.tblOrder.focus()
        selectedOrderId = self.tblOrder.item(selectedOrder)['values'][0]
        
        for order in self.orderDataList:
            if order[0] == selectedOrderId:
                orderDetailForm = AdOrderDetailForm(self, order[0])
                orderDetailForm.title('Chi tiết đơn hàng')
                orderDetailForm.geometry('1100x600+250+100')
                break
            
    def searchOrderById(self):        
        self.initOrderData()
        searchInfo = self.txtSearch.get()
        
        if searchInfo == '' or searchInfo == 'Nhập mã đơn hàng':
            self.initOrderData()
            return
        
        for row in self.tblOrder.get_children():
            if searchInfo.lower() not in self.tblOrder.item(row)['values'][0].lower():
                self.tblOrder.detach(row)
                
    def filterByMonths(self):
        self.initOrderData()
        month = self.cbxMonths.get()
        
        if month == 'Tháng đặt hàng':
            self.initOrderData()
            return
        
        for row in self.tblOrder.get_children():
            monthDate = self.tblOrder.item(row)['values'][2].split('-')[1]
            
            if int(month) != int(monthDate):
                self.tblOrder.detach(row)
                
    def filterByStatus(self):
        self.initOrderData()
        status = self.cbxStatus.get()
        
        if status == 'Tình trạng':
            self.initOrderData()
            return

        for row in self.tblOrder.get_children():
            if str(status).lower() != str(self.tblOrder.item(row)['values'][4]).lower():
                self.tblOrder.detach(row)
                
    def deleteOrder(self):
        selectedRow = self.tblOrder.focus()
        orderId = self.tblOrder.item(selectedRow)['values'][0]
        
        for order in self.orderDataList:
            if orderId == order[0]:
                self.order.deleteOrder(order)
                messagebox.showinfo('Thành công', f'Xóa thành công đơn hàng có mã {orderId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã đơn hàng không tồn tại')
    
    def changeOrderStatus(self):
        selectedRow = self.tblOrder.focus()
        orderId = self.tblOrder.item(selectedRow)['values'][0]
        customerId = self.tblOrder.item(selectedRow)['values'][1]
        orderDate = self.tblOrder.item(selectedRow)['values'][2]
        totalPrice = self.tblOrder.item(selectedRow)['values'][3]
        orderStatus = self.tblOrder.item(selectedRow)['values'][4]
        
        if orderStatus == 'Đã xử lí':
            messagebox.showinfo('Thông báo', f'Đơn hàng {orderId} đã được xử lí')
            return
        
        orderStatus = 'Đã xử lí'
        changeOrder = [orderId, customerId, orderDate, totalPrice, orderStatus]
        
        messagebox.showinfo('Thành công', f'Xử lí đơn hàng {orderId} thành công')
        self.order.changeOrderStatus(changeOrder)
        self.reset()
        
    def reset(self):
        self.initOrderData()