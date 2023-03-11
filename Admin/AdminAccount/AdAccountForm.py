from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import *
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT

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

        lb3 = Label(FrameGrid1, text='Mật khẩu:')
        lb3.grid(row=1, column=0, sticky='w')
        entry3 = Entry(FrameGrid1, width=20)
        entry3.grid(row=1, column=1, sticky='w', padx=(8, 16), pady=12)

        lb4 = Label(FrameGrid1, text='Quyền:')
        lb4.grid(row=1, column=2, sticky='w')

        cbb = Combobox(FrameGrid1, width=17)
        cbb['values'] = ('Admin', 'Nhân viên')
        cbb.grid(row=1, column=3, sticky='w', padx=(8, 16), pady=12)

        Right = Frame(container)
        Right.pack(fill=BOTH)

        labelFrame2 = LabelFrame(Right, text='Danh sách')
        labelFrame2.pack(fill=BOTH)
        labelFrame2.config(borderwidth=10, relief='solid')

        RightPack = Frame(labelFrame2, padding=4)
        RightPack.pack(fill=BOTH)

        # FrameGrid2.configure(borderwidth=1,relief='solid')
        col = ('1', '2', '3', '4')

        tr = Treeview(RightPack, columns=col, show='headings')
        tr.pack(side=LEFT)

        scrollbar = Scrollbar(RightPack, orient='vertical', command=tr.yview)
        scrollbar.pack(side=RIGHT, fill='y')
        tr.configure(yscrollcommand=scrollbar.set)

        for column in col:
            tr.column(column, anchor='c')
        
        tr.heading('1', text='ID')
        tr.heading('2', text='Tên đăng nhập')
        tr.heading('3', text='Mật khẩu')
        tr.heading('4', text='Quyền')

        tr.insert('', END, values=('TK001', 'admin', '123', 'Admin'))
        tr.insert('', END, values=('TK002', 'nhanvien1', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK003', 'nhanvien2', '456', 'Nhân Viên'))
        tr.insert('', END, values=('TK004', 'nhanvien3', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK005', 'nhanvien4', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK006', 'nhanvien5', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK007', 'nhanvien6', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK008', 'nhanvien7', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK009', 'nhanvien8', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK010', 'nhanvien9', '456', 'Nhân viên'))
        tr.insert('', END, values=('TK011', 'nhanvien10', '456', 'Nhân viên'))

        labelFrame3 = LabelFrame(Right, text='Chức năng')
        labelFrame3.pack(pady=12)

        frame3 = Frame(labelFrame3)
        frame3.pack(fill=BOTH)

        FrameGrid3 = Frame(frame3, padding=20)
        FrameGrid3.grid(column=0, row=0, sticky=NSEW)

        FrameGrid3.rowconfigure(0, weight=1)
        FrameGrid3.columnconfigure(0, weight=1)

        btnAdd = Button(FrameGrid3, text='Add new')
        btnAdd.grid(column=0, row=0, padx=(30, 50))

        btnSave = Button(FrameGrid3, text='Save')
        btnSave.grid(column=1, row=0, padx=(0, 50))

        btnDelete = Button(FrameGrid3, text='Delete')
        btnDelete.grid(column=2, row=0, padx=(0, 50))

        btnUpdate = Button(FrameGrid3, text='Update')
        btnUpdate.grid(column=3, row=0, padx=(0, 50))

        btnViewData = Button(FrameGrid3, text='View data')
        btnViewData.grid(column=4, row=0, padx=(0, 50))

        btnRefresh = Button(FrameGrid3, text='Refresh')
        btnRefresh.grid(column=5, row=0, padx=(0, 50))