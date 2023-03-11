from tkinter import Tk, TOP, BOTH, LEFT, CENTER, VERTICAL
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Labelframe, Style, Button
from PIL import Image, ImageTk

class OrderForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(fill=BOTH)
        
        self.initUI()
        self.Customize()
        
    def initUI(self):
        # header
        frame1 = Frame(self)
        frame1.pack(fill=BOTH, padx=24, pady=10)
        
        header = Label(frame1, text='Đơn hàng đã đặt', font=('Times New Roman', 20))
        header.pack()
        
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, padx=24, pady=10)
        
        # order list
        columns = ('orderID', 'orderDate', 'status', 'totalPrice')
        orderList = Treeview(frame2, columns=columns, show='headings', style='mystyle.Treeview')
        orderList.grid(row=0, column=0, sticky='EW')
        
        orderList.heading('orderID', text='Mã đơn hàng')
        orderList.heading('orderDate', text='Ngày đặt hàng')
        orderList.heading('status', text='Tình trạng')
        orderList.heading('totalPrice', text='Thành tiền')
        
        self.initOrderData(orderList, columns)
        
        scrollbar = Scrollbar(frame2, orient=VERTICAL, command=orderList.yview)
        orderList.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        for i in range(0, 3):
            self.grid_columnconfigure(i, weight = 1)
    
    def initOrderData(self, orderList, columns):
        for column in columns:
            orderList.column(column, anchor='c')
            orderList.column(column, width=270)
        
        testData = []
        for n in range(1, 15):
            testData.append((f'{n}', '3-4-2023', 'Đã xử lý', '200000'))
        for data in testData:
            orderList.insert('', 'end', values=data)
    
    def Customize(self):
        style = Style()
        style.configure('mystyle.Treeview', highlightthickness=0, rowheight = 40)
        style.configure('mystyle.Treeview.Heading', font='Helvatical 12')
        # style.layout('mystyle.Treeview', [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
           
if __name__ == '__main__':
    root = Tk()
    mainFrame = OrderForm(root)
    root.geometry('1200x600+180+100')
    root.title('Đơn hàng đã đặt')
    root.mainloop()