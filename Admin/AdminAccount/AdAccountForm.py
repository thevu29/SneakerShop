from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT

try:
    from .AdAccount import *
except:
    from AdAccount import *
    
class AdAccountForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        title = Label(self, text='Quản lý tài khoản', font=("Time News Roman", 22), foreground="black")
        title.pack()

        container = Frame(self)
        container.pack(fill=BOTH, padx=5, pady=5)

        Left = Frame(container, width=50)
        Left.pack(fill=BOTH)

        labelFrame1 = LabelFrame(Left, text='Thông tin tài khoản')
        labelFrame1.pack(fill=BOTH, pady=12)
        labelFrame1.config(borderwidth=10, relief='solid')

        FrameGrid1 = Frame(labelFrame1)
        FrameGrid1.grid(column=0, row=0)

        lb1 = Label(FrameGrid1, text='Mã tài khoản:')
        lb1.grid(row=0, column=0, sticky='w')
        entry1 = Entry(FrameGrid1, width=20)
        entry1.grid(row=0, column=1, sticky='w', padx=(8, 16), pady=12)

        lb2 = Label(FrameGrid1, text='Tên đăng nhập:')
        lb2.grid(row=0, column=2, sticky='w')
        entry2 = Entry(FrameGrid1, width=20)
        entry2.grid(row=0, column=3, sticky='w', padx=(8, 16), pady=12)

        txtCusId = Label(FrameGrid1, text='Mã khách hàng:')
        txtCusId.grid(row=0 ,column=4, sticky='w')
        cusIdEntry = Entry(FrameGrid1, width=20)
        cusIdEntry.grid(row=0 ,column=5, padx=(8, 16), pady=12)
        
        lb3 = Label(FrameGrid1, text='Mật khẩu:')
        lb3.grid(row=1, column=0, sticky='w')
        entry3 = Entry(FrameGrid1, width=20)
        entry3.grid(row=1, column=1, sticky='w', padx=(8, 16), pady=12)

        lb4 = Label(FrameGrid1, text='Quyền truy cập:')
        lb4.grid(row=1, column=2, sticky='w')

        cbb = Combobox(FrameGrid1, width=17, state='readonly')
        cbb['values'] = ('Admin', 'Nhân viên')
        cbb.grid(row=1, column=3, sticky='w', padx=(8, 16), pady=12)

        Right = Frame(container)
        Right.pack(fill=BOTH)

        labelFrame2 = LabelFrame(Right, text='Danh sách')
        labelFrame2.pack(fill=BOTH)
        labelFrame2.config(borderwidth=10, relief='solid')

        RightPack = Frame(labelFrame2, padding=4)
        RightPack.pack(fill=BOTH)

        col = ('1', '2', '3', '4', '5')

        tr = Treeview(RightPack, columns=col, show='headings')
        tr.pack(side=LEFT)

        scrollbar = Scrollbar(RightPack, orient='vertical', command=tr.yview)
        scrollbar.pack(side=RIGHT, fill='y')
        tr.configure(yscrollcommand=scrollbar.set)

        for column in col:
            tr.column(column, anchor='c', width=180)
        
        tr.heading('1', text='Mã tài khoản')
        tr.heading('2', text='Tên đăng nhập')
        tr.heading('3', text='Mật khẩu')
        tr.heading('4', text='Mã quyền truy cập')
        tr.heading('5', text='Mã khách hàng')

        self.initAccountData(tr)
    
        # frame 3
        labelFrame3 = LabelFrame(Right, text='Chức năng')
        labelFrame3.pack(pady=12)

        frame3 = Frame(labelFrame3)
        frame3.pack(fill=BOTH)

        FrameGrid3 = Frame(frame3, padding=20)
        FrameGrid3.grid(column=0, row=0, sticky=NSEW)

        FrameGrid3.rowconfigure(0, weight=1)
        FrameGrid3.columnconfigure(0, weight=1)

        btnAdd = Button(FrameGrid3, text='Thêm tài khoản', width=20)
        btnAdd.grid(column=0, row=0, padx=10, ipady=3)

        btnSave = Button(FrameGrid3, text='Lưu thông tin', width=20)
        btnSave.grid(column=1, row=0, padx=10, ipady=3)

        btnDelete = Button(FrameGrid3, text='Xóa tài khoản', width=20)
        btnDelete.grid(column=2, row=0, padx=10, ipady=3)

        btnRefresh = Button(FrameGrid3, text='Reset', width=20)
        btnRefresh.grid(column=5, row=0, padx=10, ipady=3)
        
    def initAccountData(self, accountList):
        account = AdAccountData()
        accountDataList = account.getAccountList()
        for data in accountDataList:
            accountList.insert('', 'end', values=data)