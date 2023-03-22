from tkinter import Tk, BOTH, LEFT, VERTICAL, E, W, S, NO, CENTER, X, messagebox
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button

try:
    from .AdUser import *
except:
    from AdUser import *

class AdUserForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.user = AdUserData()
        self.userDataList = self.user.getUserList()
        
        self.main_title()
        self.create_form()

    def main_title(self):
        main_frame = Label(self, text="Quản lý khách hàng", font=("Time News Roman", 22), foreground="black")
        main_frame.pack()

    def create_form(self):
        # Tạo form bên trái
        self.form_left = LabelFrame(self, text="Thông tin khách hàng")
        self.form_left.pack(fill=BOTH, pady=12)
        self.form_left.configure(borderwidth=10, relief='solid')

        # Mã khách hàng và entry
        self.userId = Label(self.form_left, text="Mã khách hàng:")
        self.userId.grid(row=0, column=0, sticky='w')
        self.txtUserId = Entry(self.form_left)
        self.txtUserId.grid(row=0, column=1, sticky='w', padx=(8, 16), pady=12)

        # Tên khách hàng và entry
        self.userName = Label(self.form_left, text="Tên khách hàng:")
        self.userName.grid(row=0, column=2, sticky='w')
        self.txtUserName = Entry(self.form_left, width=40)
        self.txtUserName.grid(row=0, column=3, sticky='w', padx=(8, 16), pady=12)

        # Giới tính và entry
        self.gender = Label(self.form_left, text="Giới tính:")
        self.gender.grid(row=0, column=4, sticky='w')
        self.cbxGender = Combobox(self.form_left, state='readonly', values=('Nam', 'Nữ'))
        self.cbxGender.grid(row=0, column=5, sticky='w', padx=(8, 16), pady=12)
        
        # Số điện thoại và entry
        self.phone = Label(self.form_left, text="Số điện thoại:")
        self.phone.grid(row=1, column=0, sticky='w')
        self.txtPhone = Entry(self.form_left)
        self.txtPhone.grid(row=1, column=1, sticky='w', padx=(8, 16), pady=12)
        
        # Địa chỉ và entry
        self.address = Label(self.form_left, text="Địa chỉ:")
        self.address.grid(row=1, column=2, sticky='w')
        self.txtAddress = Entry(self.form_left, width=40)
        self.txtAddress.grid(row=1, column=3, sticky='w', padx=(8, 16), pady=12)

        # Điểm thành viên và entry
        self.point = Label(self.form_left, text="Điểm thành viên:")
        self.point.grid(row=1, column=4, sticky='w')
        self.txtPoint = Entry(self.form_left)
        self.txtPoint.grid(row=1, column=5, sticky='w', padx=(8, 16), pady=12)

        # Tạo form bên phải
        self.list_info_frame = LabelFrame(self, text="Danh sách khách hàng")
        self.list_info_frame.pack(fill=BOTH)
        self.list_info_frame.config(borderwidth=10, relief='solid')

        # Tạo Tree view
        self.tblUser = Treeview(self.list_info_frame, show='headings')
        self.tblUser.grid(row=0, column=0, sticky='EW')

        # Create scroll in self.list_info_frame
        scrollbar = Scrollbar(self.list_info_frame, orient=VERTICAL, command=self.tblUser.yview)
        self.tblUser.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        self.tblUser['columns'] = ("Mã khách hàng", "Tên khách hàng", "Địa chỉ", "Số điện thoại", "Giới tính", "Điểm thành viên")
        for column in ("Mã khách hàng", "Tên khách hàng", "Địa chỉ", "Số điện thoại", "Giới tính", "Điểm thành viên"):
            if (column != 'Tên khách hàng' and column != 'Địa chỉ'):
                self.tblUser.column(column, anchor='c')
            self.tblUser.column(column, width=150)
            
        self.tblUser.heading("Mã khách hàng", text="Mã khách hàng", anchor=CENTER)
        self.tblUser.heading("Tên khách hàng", text="Tên khách hàng", anchor=CENTER)
        self.tblUser.heading("Địa chỉ", text="Địa chỉ", anchor=CENTER)
        self.tblUser.heading("Số điện thoại", text="Số điện thoại", anchor=CENTER)
        self.tblUser.heading("Giới tính", text="Giới tính", anchor=CENTER)
        self.tblUser.heading("Điểm thành viên", text="Điểm thành viên", anchor=CENTER)

        self.initUserData()

        self.tblUser.bind('<<TreeviewSelect>>', lambda x: self.showUserInfo())
        
        # Tạo form bên phải, dưới là chức năng
        self.function_frame = LabelFrame(self, text="Chức năng")
        self.function_frame.pack(pady=12)
        self.function_frame.config(borderwidth=10, relief='solid')

        # Tạo button
        self.btnAdd = Button(self.function_frame, text="Thêm khách hàng", width=20, command=self.addUser)
        self.btnAdd.grid(row=0, column=0, pady=6, padx=10, ipady=3)
        
        self.btnSave = Button(self.function_frame, text="Lưu thông tin", width=20, command=self.saveUserInfo)
        self.btnSave.grid(row=0, column=1, pady=6, padx=10, ipady=3)
        
        self.btnDelete = Button(self.function_frame, text="Xóa khách hàng", width=20, command=self.deleteUser)
        self.btnDelete.grid(row=0, column=2, pady=6, padx=10, ipady=3)

        self.btnresetValue = Button(self.function_frame, text="Reset", width=20, command=self.reset)
        self.btnresetValue.grid(row=0, column=5, pady=6, padx=10, ipady=3)
        
    def initUserData(self):
        for row in self.tblUser.get_children():
            self.tblUser.delete(row)
        
        for data in self.userDataList:
            self.tblUser.insert('', 'end', values=data)
            
    def showUserInfo(self):
        try:
            selectedRow = self.tblUser.focus()
            selectedRowId = self.tblUser.item(selectedRow)['values'][0]
        except:
            return
        
        self.resetValue()
        
        for user in self.userDataList:
            if user[0] == selectedRowId:
                self.txtUserId.insert('0', user[0])   
                self.txtUserName.insert('0', user[1])
                self.txtAddress.insert('0', user[2])
                self.txtPhone.insert('0', user[3])
                self.txtPoint.insert('0', user[5])
                
                if (user[4] == 'Nam'):
                    self.cbxGender.current(0)
                else:
                    self.cbxGender.current(1)
    
    def validate(self):
        userId = self.txtUserId.get()
        userName = self.txtUserName.get()
        address = self.txtAddress.get()
        phone = self.txtPhone.get()
        point = self.txtPoint.get()
        gender = self.cbxGender.get()
        
        s = ''
        if (userId == ''):
            s += 'Mã khách hàng không được để trống \n'
        if (userName == ''):
            s += 'Tên khách hàng không được để trống \n'
        if (address == ''):
            s += 'Địa chỉ không được để trống \n'
        if (phone == ''):
            s += 'Số điện thoại không được để trống \n'
        if (point == ''):
            s += 'Điểm thành viên không được để trống \n'
        if (gender == ''):
            s += 'Giới tính không được để trống \n' 
            
        if (len(s) > 0):
            messagebox.showwarning('Warning', s)
            return False
        return True
                    
    def addUser(self):
        if (self.validate() == False):
            return
        
        userId = self.txtUserId.get()
        userName = self.txtUserName.get()
        address = self.txtAddress.get()
        phone = self.txtPhone.get()
        gender = self.cbxGender.get()
        point = self.txtPoint.get()
        
        for user in self.userDataList:
            if userId == user[0]:
                messagebox.showwarning('Warning', 'Mã khách hàng đã tồn tại')
                return
            
        newUser = [userId, userName, address, phone, gender, point]
        
        self.user.addUser(newUser)
        messagebox.showinfo('Thành công', 'Thêm khách hàng thành công')
        self.reset()
    
    def deleteUser(self):
        if (self.validate() == False):
            return

        userId = self.txtUserId.get()
        
        for user in self.userDataList:
            if userId == user[0]:
                self.user.deleteUser(user)
                messagebox.showinfo('Thành công', f'Xóa thành công khách hàng có mã {userId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã khách hàng không tồn tại')
    
    def saveUserInfo(self):
        if (self.validate() == False):
            return
        
        userId = self.txtUserId.get()
        userName = self.txtUserName.get()
        address = self.txtAddress.get()
        phone = self.txtPhone.get()
        gender = self.cbxGender.get()
        point = self.txtPoint.get()
        
        newUser = [userId, userName, address, phone, gender, point]
        
        for user in self.userDataList:
            if userId == user[0]:
                self.user.updateUserInfo(newUser)
                messagebox.showinfo('Thành công', f'Sửa thành công thông tin khách hàng có mã {userId}')
                self.reset()
                return
            
        messagebox.showwarning('Warning', 'Mã khách hàng không tồn tại')
       
    def resetValue(self):
        self.txtUserId.delete('0', 'end')
        self.txtUserName.delete('0', 'end')
        self.txtAddress.delete('0', 'end')
        self.txtPhone.delete('0', 'end')
        self.cbxGender.current(0)
        self.txtPoint.delete('0', 'end')
        
    def reset(self):
        self.resetValue()
        self.initUserData()