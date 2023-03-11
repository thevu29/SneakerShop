from tkinter import Tk, N, E, W, S, NSEW, BOTH, LEFT, VERTICAL
from tkinter.ttk import Label, Frame, Entry, Treeview, Scrollbar, Button, LabelFrame

class AdOrderDetailForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(fill=BOTH)
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
        
        # frame 4
        frame4 = LabelFrame(self, text='Chức năng')
        frame4.pack(padx=24, pady=10)
        frame4.configure(border=10, relief='solid')
        
        self.initFrame2Component(frame2)
        self.initFrame3Component(frame3)
        self.initFrame4Component(frame4)
    
    def initFrame2Component(self, frame2):
        # Row 0
        txtOrderID = Label(frame2, text='Mã hóa đơn:')
        txtOrderID.grid(row=0, column=0, padx=(20, 0), sticky=W)
        orderID = Entry(frame2)
        orderID.grid(row=0, column=1, padx=10, pady=10)
        
        txtOrderDate = Label(frame2, text='Ngày mua hàng:')
        txtOrderDate.grid(row=0, column=2, padx=(20, 0), sticky=W)
        orderDate = Entry(frame2)
        orderDate.grid(row=0, column=3, padx=10, pady=10)
        
        txtEmployeeID = Label(frame2, text='Mã nhân viên:')
        txtEmployeeID.grid(row=0, column=4, padx=(20, 0), sticky=W)
        employeeID = Entry(frame2)
        employeeID.grid(row=0, column=5, padx=10, pady=10)
        
        txtEmployeeName = Label(frame2, text='Tên nhân viên:')
        txtEmployeeName.grid(row=0, column=6, padx=(20, 0), sticky=W)
        employeeName = Entry(frame2)
        employeeName.grid(row=0, column=7, padx=10, pady=10)
        
        # Row 1
        txtUserID = Label(frame2, text='Mã khách hàng:')
        txtUserID.grid(row=1, column=0, padx=(20, 0), sticky=W)
        userID = Entry(frame2)
        userID.grid(row=1, column=1, padx=10, pady=10)
        
        txtUserName = Label(frame2, text='Tên khách hàng:')
        txtUserName.grid(row=1, column=2, padx=(20, 0), sticky=W)
        userName = Entry(frame2)
        userName.grid(row=1, column=3, padx=10, pady=10)
        
        txtAddress = Label(frame2, text='Địa chỉ:')
        txtAddress.grid(row=1, column=4, padx=(20, 0), sticky=W)
        address = Entry(frame2)
        address.grid(row=1, column=5, padx=10, pady=10)
        
        txtUserPhone = Label(frame2, text='Số điện thoại:')
        txtUserPhone.grid(row=1, column=6, padx=(20, 0), sticky=W)
        userPhone = Entry(frame2)
        userPhone.grid(row=1, column=7, padx=10, pady=10)
        
        for i in range(0, 8):
            frame2.grid_columnconfigure(i, weight=1)
        
    def initFrame3Component(self, frame3):
        columns = ('productID', 'productName', 'quantity', 'productPrice', 'discount', 'discountPrice')
        orderProductList = Treeview(frame3, columns=columns, show='headings')
        orderProductList.grid(row=0, column=0)
        orderProductList.column('productID', width=100)
        
        orderProductList.heading('productID', text='Mã sản phẩm')
        orderProductList.heading('productName', text='Tên sản phẩm')
        orderProductList.heading('quantity', text='Số lượng')
        orderProductList.heading('productPrice', text='Đơn giá')
        orderProductList.heading('discount', text='Giảm giá(%)')
        orderProductList.heading('discountPrice', text='Tổng tiền')
        
        self.initOrderProductData(orderProductList, columns)
        
        scrollbar = Scrollbar(frame3, orient=VERTICAL, command=orderProductList.yview)
        orderProductList.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        totalPriceContainer = Frame(frame3)
        totalPriceContainer.grid(row=1, column=0, sticky=E, pady=(10, 0))
        
        txtTotalPrice = Label(totalPriceContainer, text='Tổng tiền:', font=('', 10, 'bold'))
        txtTotalPrice.grid(row=0, column=0, sticky=E, padx=(0, 10))
        
        totalPrice = Entry(totalPriceContainer)
        totalPrice.grid(row=0, column=1, sticky=E, ipady=2)
        totalPrice.insert(0, '3000000')
        
        for i in range(0, 2):
            frame3.grid_columnconfigure(i, weight=1)
    
    def initFrame4Component(self, frame4):
        btnUpdate = Button(frame4, text='Lưu thông tin')
        btnUpdate.grid(row=0, column=0, ipadx=6, ipady=2, padx=12)
        
        btnReset = Button(frame4, text='Reset')
        btnReset.grid(row=0, column=1, ipadx=6, ipady=2)
        
        for i in range(0, 2):
            frame4.grid_columnconfigure(i, weight=1)
    
    def initOrderProductData(self, orderProductList, columns):            
        for column in columns:
            orderProductList.column(column, anchor='c')
                
        testData = []
        for n in range(1, 15):
            testData.append((f'{n}', f'Air force {n}', f'{n}', '200000', '10', '300000'))
        for data in testData:
            orderProductList.insert('', 'end', values=data)
          
if __name__ == '__main__':
    root = Tk()
    mainFrame = AdOrderDetailForm(root) 
    root.geometry('1200x600+180+100')
    root.title('Chi tiết đơn hàng')
    root.mainloop()