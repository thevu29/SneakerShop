from tkinter import Tk, N, E, W, S, NSEW, BOTH, LEFT, VERTICAL, StringVar, Toplevel
from tkinter.ttk import Label, Frame, Entry, Treeview, Scrollbar, Button, LabelFrame
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Admin.AdminOrder import AdOrder

class OrderDetailForm(Toplevel):    
    def __init__(self, parent, orderID):
        Toplevel.__init__(self, parent)
        self.parent = parent
        
        self.orderDetail = AdOrder.AdOrderDetailData()
        self.orderDetailDataList = self.orderDetail.getOrderDetailList()
        
        self.orderID = str(orderID)
        self.orderDate = ''
        self.totalPrice = 0
        
        self.customerID = ''
        self.customerName = ''
        self.customerAddress = ''
        self.customerPhone = ''
        
        self.getDataFromOrder()
        self.initUI()    
       
    def initUI(self):   
        # header
        frame1 = Frame(self)
        frame1.pack(fill=BOTH, padx=24, pady=10)
        
        header = Label(frame1, text='Chi tiết đơn hàng', font=('Times New Roman', 20))
        header.pack(fill=BOTH, side=LEFT)
        
        # frame 2
        frame2 = LabelFrame(self, text='Thông tin chung')
        frame2.pack(fill=BOTH, padx=24, pady=10)
        frame2.configure(borderwidth=10, relief='solid')
        
        # frame 3
        frame3 = LabelFrame(self, text='Thông tin sản phẩm')
        frame3.pack(fill=BOTH, padx=24)
        frame3.configure(borderwidth=10, relief='solid')
        
        self.initFrame2Component(frame2)
        self.initFrame3Component(frame3)
    
    def initFrame2Component(self, frame2):
        # Row 0
        self.lblOrderID = Label(frame2, text='Mã hóa đơn:')
        self.lblOrderID.grid(row=0, column=0, padx=(20, 0), sticky=W)
        self.txtOrderID = Entry(frame2)
        self.txtOrderID.insert('0', self.orderID)
        self.txtOrderID.grid(row=0, column=1, padx=(10, 18), pady=10)
        
        self.lblorderDate = Label(frame2, text='Ngày đặt hàng:')
        self.lblorderDate.grid(row=1, column=0, padx=(20, 0), sticky=W)
        self.txtOrderDate = Entry(frame2)
        self.txtOrderDate.insert('0', self.orderDate)
        self.txtOrderDate.grid(row=1, column=1, padx=(10, 18), pady=10)
        
        # self.employeeID = Label(frame2, text='Mã nhân viên:')
        # self.employeeID.grid(row=0, column=4, padx=(20, 0), sticky=W)
        # self.txtEmployeeID = Entry(frame2)
        # self.txtEmployeeID.grid(row=0, column=5, padx=(10, 18), pady=10)
        
        # self.employeeName = Label(frame2, text='Tên nhân viên:')
        # self.employeeName.grid(row=0, column=6, padx=(20, 0), sticky=W)
        # self.txtEmployeeName = Entry(frame2)
        # self.txtEmployeeName.grid(row=0, column=7, padx=(10, 18), pady=10)
        
        # Row 1
        self.userID = Label(frame2, text='Mã khách hàng:')
        self.userID.grid(row=0, column=2, padx=(20, 0), sticky=W)
        self.txtUserID = Entry(frame2, width=30)
        self.txtUserID.insert('0', self.customerID)
        self.txtUserID.grid(row=0, column=3, padx=(10, 18), pady=10)
        
        self.lblUserName = Label(frame2, text='Tên khách hàng:')
        self.lblUserName.grid(row=1, column=2, padx=(20, 0), sticky=W)
        self.txtUserName = Entry(frame2, width=30)
        self.txtUserName.insert('0', self.customerName)
        self.txtUserName.grid(row=1, column=3, padx=(10, 18), pady=10)
        
        self.lblAddress = Label(frame2, text='Địa chỉ:')
        self.lblAddress.grid(row=0, column=4, padx=(20, 0), sticky=W)
        self.txtAddress = Entry(frame2, width=40)
        self.txtAddress.insert('0', self.customerAddress)
        self.txtAddress.grid(row=0, column=5, padx=(10, 18), pady=10)
        
        self.userPhone = Label(frame2, text='Số điện thoại:')
        self.userPhone.grid(row=1, column=4, padx=(20, 0), sticky=W)
        self.txtUserPhone = Entry(frame2, width=40)
        self.txtUserPhone.insert('0', self.customerPhone)
        self.txtUserPhone.grid(row=1, column=5, padx=(10, 18), pady=10)
        
    def initFrame3Component(self, frame3):
        columns = ('productID', 'productName', 'quantity', 'productPrice', 'productSize', 'discountPrice')
        self.tblOrderDetail = Treeview(frame3, columns=columns, show='headings')
        self.tblOrderDetail.grid(row=0, column=0)
                
        self.tblOrderDetail.heading('productID', text='Mã sản phẩm')
        self.tblOrderDetail.heading('productName', text='Tên sản phẩm')
        self.tblOrderDetail.heading('quantity', text='Số lượng')
        self.tblOrderDetail.heading('productPrice', text='Đơn giá')
        self.tblOrderDetail.heading('productSize', text='Size')
        self.tblOrderDetail.heading('discountPrice', text='Thành tiền')
        
        for column in columns:
            self.tblOrderDetail.column(column, anchor='c', width=170)
        
        self.initOrderDetailData()
        
        scrollbar = Scrollbar(frame3, orient=VERTICAL, command=self.tblOrderDetail.yview)
        self.tblOrderDetail.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        totalPriceContainer = Frame(frame3)
        totalPriceContainer.grid(row=1, column=0, sticky=E, pady=(10, 0))
        
        txtTotalPrice = Label(totalPriceContainer, text='Tổng tiền:', font=('', 10, 'bold'))
        txtTotalPrice.grid(row=0, column=0, sticky=E, padx=(10, 18))
        
        self.totalPriceText = StringVar()
        self.totalPriceText.set('{0:.2f}'.format(self.totalPrice).rstrip('0').rstrip('.'))
        totalPrice = Entry(totalPriceContainer, state='readonly', textvariable=self.totalPriceText)
        totalPrice.grid(row=0, column=1, sticky=E, ipady=2)
           
    def initOrderDetailData(self):                            
        productList = self.orderDetail.getProductData()
         
        for data in self.orderDetailDataList:
            if data[0] == self.orderID:
                newData = [data[i] for i in range(1, 5)]
                quantity = float(data[2])
                price = float(data[3])
                
                productName = ''
                for product in productList:
                    if product[0] == data[1]:
                        productName = str(product[1])
                        break
                
                total = quantity * price
                
                newData.insert(1, productName)
                newData.append('{0:.2f}'.format(total).rstrip('0').rstrip('.'))
                
                self.tblOrderDetail.insert('', 'end', values=newData)
    
    def getDataFromOrder(self):
        order = AdOrder.AdOrderData()
        orderList = order.getOrderList()
        
        for item in orderList:
            if self.orderID == item[0]:
                self.customerID = str(item[1])
                self.orderDate = str(item[2])
                self.customerName = order.getCustomerName(item[0])
                self.customerAddress = item[5]
                self.customerPhone = item[6]
                self.totalPrice = float(item[3])
                break