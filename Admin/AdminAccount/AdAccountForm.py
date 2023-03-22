from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, NSEW, messagebox
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button

try:
    from .AdAccount import *
except:
    from AdAccount import *
    
class AdAccountForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.account = AdAccountData()
        self.accountDataList = self.account.getAccountList()
        
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

        self.accountId = Label(FrameGrid1, text='Mã tài khoản:')
        self.accountId.grid(row=0, column=0, sticky='w')
        self.txtAccountId = Entry(FrameGrid1, width=20)
        self.txtAccountId.grid(row=0, column=1, sticky='w', padx=(8, 16), pady=12)

        self.userName = Label(FrameGrid1, text='Tên đăng nhập:')
        self.userName.grid(row=0, column=2, sticky='w')
        self.txtUsername = Entry(FrameGrid1, width=20)
        self.txtUsername.grid(row=0, column=3, sticky='w', padx=(8, 16), pady=12)

        self.customerId = Label(FrameGrid1, text='Mã khách hàng:')
        self.customerId.grid(row=0 ,column=4, sticky='w')
        self.txtCustomerId = Entry(FrameGrid1, width=20)
        self.txtCustomerId.grid(row=0 ,column=5, padx=(8, 16), pady=12)
        
        self.password = Label(FrameGrid1, text='Mật khẩu:')
        self.password.grid(row=1, column=0, sticky='w')
        self.txtPassword = Entry(FrameGrid1, width=20)
        self.txtPassword.grid(row=1, column=1, sticky='w', padx=(8, 16), pady=12)

        self.access = Label(FrameGrid1, text='Quyền truy cập:')
        self.access.grid(row=1, column=2, sticky='w')

        self.cbxAccess = Combobox(FrameGrid1, width=17, state='readonly', values=('Admin', 'Nhân viên'))
        self.cbxAccess.grid(row=1, column=3, sticky='w', padx=(8, 16), pady=12)

        Right = Frame(container)
        Right.pack(fill=BOTH)

        labelFrame2 = LabelFrame(Right, text='Danh sách')
        labelFrame2.pack(fill=BOTH)
        labelFrame2.config(borderwidth=10, relief='solid')

        RightPack = Frame(labelFrame2, padding=4)
        RightPack.pack(fill=BOTH)

        col = ('1', '2', '3', '4', '5')

        self.tblAccount = Treeview(RightPack, columns=col, show='headings')
        self.tblAccount.pack(side=LEFT)

        scrollbar = Scrollbar(RightPack, orient='vertical', command=self.tblAccount.yview)
        scrollbar.pack(side=RIGHT, fill='y')
        self.tblAccount.configure(yscrollcommand=scrollbar.set)

        for column in col:
            self.tblAccount.column(column, anchor='c', width=180)
        
        self.tblAccount.heading('1', text='Mã tài khoản')
        self.tblAccount.heading('2', text='Tên đăng nhập')
        self.tblAccount.heading('3', text='Mật khẩu')
        self.tblAccount.heading('4', text='Mã quyền truy cập')
        self.tblAccount.heading('5', text='Mã khách hàng')

        self.tblAccount.bind('<<TreeviewSelect>>', lambda x: self.showUserInfo())
        self.initAccountData()

        # frame 3
        labelFrame3 = LabelFrame(Right, text='Chức năng')
        labelFrame3.pack(pady=12)

        frame3 = Frame(labelFrame3)
        frame3.pack(fill=BOTH)

        FrameGrid3 = Frame(frame3, padding=20)
        FrameGrid3.grid(column=0, row=0, sticky=NSEW)

        FrameGrid3.rowconfigure(0, weight=1)
        FrameGrid3.columnconfigure(0, weight=1)

        btnAdd = Button(FrameGrid3, text='Thêm tài khoản', width=20, command=self.addAccount)
        btnAdd.grid(column=0, row=0, padx=10, ipady=3)

        btnSave = Button(FrameGrid3, text='Lưu thông tin', width=20, command=self.saveUserInfo)
        btnSave.grid(column=1, row=0, padx=10, ipady=3)

        btnDelete = Button(FrameGrid3, text='Xóa tài khoản', width=20, command=self.deleteAccount)
        btnDelete.grid(column=2, row=0, padx=10, ipady=3)

        btnRefresh = Button(FrameGrid3, text='Reset', width=20, command=self.reset)
        btnRefresh.grid(column=5, row=0, padx=10, ipady=3)
        
    def initAccountData(self):
        for row in self.tblAccount.get_children():
            self.tblAccount.delete(row)
        
        for data in self.accountDataList:
            self.tblAccount.insert('', 'end', values=data)
            
    def showUserInfo(self):
        try:
            selectedRow = self.tblAccount.focus()
            selectedRowId = self.tblAccount.item(selectedRow)['values'][0]
        except:
            return
        
        self.resetValue()
        
        for account in self.accountDataList:
            if account[0] == selectedRowId:
                self.txtAccountId.insert('0', account[0])   
                self.txtUsername.insert('0', account[1])
                self.txtPassword.insert('0', account[2])
                self.txtCustomerId.insert('0', account[4])
                
                if account[3] == 'ACS001':
                    self.cbxAccess.current(0)
                else:
                    self.cbxAccess.current(1)
                    
    def validate(self):
        accountId = self.txtAccountId.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        access = self.cbxAccess.get()
        customerId = self.txtCustomerId.get()
        
        s = ''
        if (accountId == ''):
            s += 'Mã tài khoản không được để trống \n'
        if (username == ''):
            s += 'Tên đăng nhập không được để trống \n'
        if (password == ''):
            s += 'Mật khẩu không được để trống \n'
        if (access == ''):
            s += 'Quyền truy cập không được để trống \n'
        if (customerId == ''):
            s += 'Mã khách hàng không được để trống \n'
            
        if (len(s) > 0):
            messagebox.showwarning('Warning', s)
            return False
        return True
    
    def addAccount(self):
        if (self.validate() == False):
            return
        
        accountId = self.txtAccountId.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        access = self.cbxAccess.get()
        customerId = self.txtCustomerId.get()
        
        for account in self.accountDataList:
            if accountId == account[0]:
                messagebox.showwarning('Warning', 'Mã tài khoản đã tồn tại')
                return
        
        accessId = ''
        if access == 'Admin':
            accessId = 'ACS001'
        else:
            accessId = 'ACS002'    
            
        newAccount = [accountId, username, password, accessId, customerId]
        
        self.account.addAccount(newAccount)
        messagebox.showinfo('Thành công', 'Thêm tài khoản thành công')
        self.reset()  
    
    def deleteAccount(self):
        if (self.validate() == False):
            return

        accountId = self.txtAccountId.get()
        
        for account in self.accountDataList:
            if accountId == account[0]:
                self.account.deleteAccount(account)
                messagebox.showinfo('Thành công', f'Xóa thành công tài khoản có mã {accountId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã tài khoản không tồn tại')
    
    def saveUserInfo(self):
        if (self.validate() == False):
            return
        
        accountId = self.txtAccountId.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        access = self.cbxAccess.get()
        customerId = self.txtCustomerId.get()
        
        accessId = ''
        if access == 'Admin':
            accessId = 'ACS001'
        else:
            accessId = 'ACS002'    
            
        newAccount = [accountId, username, password, accessId, customerId]
        
        for account in self.accountDataList:
            if accountId == account[0]:
                self.account.updateAccountInfo(newAccount)
                messagebox.showinfo('Thành công', f'Sửa thành công thông tin tài khoản có mã {accountId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã tài khoản không tồn tại')
                    
    def resetValue(self):
        self.txtAccountId.delete('0', 'end')
        self.txtUsername.delete('0', 'end')
        self.txtPassword.delete('0', 'end')
        self.cbxAccess.current(0)
        self.txtCustomerId.delete('0', 'end')
        
    def reset(self):
        self.resetValue()
        self.initAccountData()