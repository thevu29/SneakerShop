from tkinter import Tk, TOP, BOTH, LEFT, CENTER, VERTICAL, Toplevel
from tkinter.font import Font
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Labelframe, Style, Button
from PIL import Image, ImageTk
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Admin.AdminOrder import AdOrder

try:
    from OrderDetailForm import *
except:
    from .OrderDetailForm import *

class OrderForm(Toplevel):
    def __init__(self, parent, userId):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.userId = userId
        
        self.order = AdOrder.AdOrderData()
        self.orderList = self.order.getOrderList()
        
        self.protocol('WM_DELETE_WINDOW', self.closeAll)
        
        self.normalFont = Font(family='Arial', size=10)
        self.underlineFont = Font(family='Arial', size=10, underline=True)
        
        self.initUI()
        self.Customize()
    
    def closeAll(self):
        self.parent.destroy()
        exit()
      
    def initUI(self):
        # header
        frame1 = Frame(self)
        frame1.pack(fill=BOTH, padx=24, pady=(12, 24))
        
        header = Label(frame1, text='Đơn hàng đã đặt', font=('Times New Roman', 20, 'bold'), foreground='#0071e3')
        header.pack()
        
        # order table
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, padx=24, pady=10)
        
        self.initOrderTable(frame2)
        
        # back product page
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, padx=24, pady=(24, 12))
        
        self.initBackProductPage(frame3)
    
    def initOrderTable(self, frame2):    
        columns = ('orderID', 'userId', 'orderDate', 'totalPrice', 'status')
        self.tblOrder = Treeview(frame2, columns=columns, show='headings', style='mystyle.Treeview')
        self.tblOrder.grid(row=0, column=0, sticky='EW')
        
        self.tblOrder.heading('orderID', text='Mã đơn hàng')
        self.tblOrder.heading('userId', text='Mã khách hàng')
        self.tblOrder.heading('orderDate', text='Ngày đặt hàng')
        self.tblOrder.heading('totalPrice', text='Thành tiền')
        self.tblOrder.heading('status', text='Tình trạng')
        
        scrollbar = Scrollbar(frame2, orient=VERTICAL, command=self.tblOrder.yview)
        self.tblOrder.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        for column in columns:
            self.tblOrder.column(column, anchor='c', width=220)
            
        self.initOrderData()
        self.tblOrder.bind('<Double-1>', lambda x: self.showOrderDetail())
        
        for i in range(0, 3):
            frame2.grid_columnconfigure(i, weight = 1)
    
    def initOrderData(self):
        for data in self.orderList:
            if data[1] == self.userId:
                self.tblOrder.insert('', 'end', values=data)
    
    def initBackProductPage(self, frame3):
        self.leftArrowImg = ImageTk.PhotoImage(Image.open('./img/left_arrow.png').resize((35, 20)))
        self.leftArrow = Label(frame3, image=self.leftArrowImg, cursor='hand2')
        self.leftArrow.grid(row=0, column=0)
        
        self.lblproductPage = Label(frame3, text='Trở về trang sản phẩm', font=('Arial', 10), cursor='hand2')
        self.lblproductPage.grid(row=0, column=1, padx=4)
        self.lblproductPage.bind("<Button-1>", lambda x: self.backProductPage())
        self.lblproductPage.bind("<Enter>", self.onHover)
        self.lblproductPage.bind("<Leave>", self.outHover)
    
    def Customize(self):
        style = Style()
        style.configure('mystyle.Treeview', highlightthickness=0, rowheight = 40, font=('Arial', 10))
        style.configure('mystyle.Treeview.Heading', font=('Arial', 12, 'bold'))
    
    def showOrderDetail(self):
        selectedOrder = self.tblOrder.focus()
        selectedOrderId = self.tblOrder.item(selectedOrder)['values'][0]
        
        for order in self.orderList:
            if order[0] == selectedOrderId:
                orderDetailForm = OrderDetailForm(self, order[0])
                orderDetailForm.title('Chi tiết đơn hàng')
                orderDetailForm.geometry('1100x600+250+100')
                orderDetailForm.resizable(False, False)
                return
    
    def backProductPage(self):
        self.parent.orderPage.destroy()
        self.parent.deiconify()
    
    def onHover(self, e):
        e.widget.config(font=self.underlineFont)
        
    def outHover(self, e):
        e.widget.config(font=self.normalFont)