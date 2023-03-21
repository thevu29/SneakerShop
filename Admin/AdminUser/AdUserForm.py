from tkinter import Tk, BOTH, LEFT, VERTICAL, E, W, S, NO, CENTER, X
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, LabelFrame, Button

try:
    from .AdUserData import *
except:
    from AdUserData import *

class AdUserForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.main_title()
        self.create_form()

    def main_title(self):
        main_frame = Label(self, text="Quản lý khách hàng", font=("Time News Roman", 22), foreground="black")
        main_frame.pack()

    def create_form(self):
        # Tạo form bên trái
        form_left = LabelFrame(self, text="Thông tin khách hàng")
        form_left.pack(fill=BOTH, pady=12)
        form_left.configure(borderwidth=10, relief='solid')

        # Mã khách hàng và entry
        label1 = Label(form_left, text="Mã khách hàng:")
        label1.grid(row=0, column=0, sticky='w')
        first_entry = Entry(form_left, font=('Time new roman', 10))
        first_entry.grid(row=0, column=1, sticky='w', padx=(8, 16), pady=12)

        # Tên khách hàng và entry
        label2 = Label(form_left, text="Tên khách hàng:")
        label2.grid(row=0, column=2, sticky='w')
        second_entry = Entry(form_left, font=('Time new roman', 10))
        second_entry.grid(row=0, column=3, sticky='w', padx=(8, 16), pady=12)

        # Giới tính và entry
        label5 = Label(form_left, text="Giới tính:")
        label5.grid(row=0, column=4, sticky='w')
        fifth_entry = Combobox(form_left, font=('Time new roman', 10), state='readonly')
        fifth_entry['values'] = ('Nam', 'Nữ')
        fifth_entry.grid(row=0, column=5, sticky='w', padx=(8, 16), pady=12)
        
        # Địa chỉ và entry
        label3 = Label(form_left, text="Địa chỉ:")
        label3.grid(row=1, column=0, sticky='w')
        third_entry = Entry(form_left, font=('Time new roman', 10))
        third_entry.grid(row=1, column=1, sticky='w', padx=(8, 16), pady=12)

        # Số điện thoại và entry
        label4 = Label(form_left, text="Số điện thoại:")
        label4.grid(row=1, column=2, sticky='w')
        fourth_entry = Entry(form_left, font=('Time new roman', 10))
        fourth_entry.grid(row=1, column=3, sticky='w', padx=(8, 16), pady=12)

        # Điểm thành viên và entry
        label6 = Label(form_left, text="Điểm thành viên:")
        label6.grid(row=1, column=4, sticky='w')
        six_entry = Entry(form_left, font=('Time new roman', 10))
        six_entry.grid(row=1, column=5, sticky='w', padx=(8, 16), pady=12)

        # Tạo form bên phải
        list_info_frame = LabelFrame(self, text="Danh sách khách hàng")
        list_info_frame.pack(fill=BOTH)
        list_info_frame.config(borderwidth=10, relief='solid')

        # Tạo Tree view
        my_tree = Treeview(list_info_frame, show='headings')
        my_tree.grid(row=0, column=0, sticky='EW')

        # Create scroll in list_info_frame
        scrollbar = Scrollbar(list_info_frame, orient=VERTICAL, command=my_tree.yview)
        my_tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='NS')
        
        my_tree['columns'] = ("Mã khách hàng", "Tên khách hàng", "Địa chỉ", "Số điện thoại", "Giới tính", "Điểm thành viên")
        for column in ("Mã khách hàng", "Tên khách hàng", "Địa chỉ", "Số điện thoại", "Giới tính", "Điểm thành viên"):
            if (column != 'Tên khách hàng' and column != 'Địa chỉ'):
                my_tree.column(column, anchor='c')
            my_tree.column(column, width=150)
            
        my_tree.heading("Mã khách hàng", text="Mã khách hàng", anchor=CENTER)
        my_tree.heading("Tên khách hàng", text="Tên khách hàng", anchor=CENTER)
        my_tree.heading("Địa chỉ", text="Địa chỉ", anchor=CENTER)
        my_tree.heading("Số điện thoại", text="Số điện thoại", anchor=CENTER)
        my_tree.heading("Giới tính", text="Giới tính", anchor=CENTER)
        my_tree.heading("Điểm thành viên", text="Điểm thành viên", anchor=CENTER)

        self.initUserData(my_tree)

        # Tạo form bên phải, dưới là chức năng
        function_frame = LabelFrame(self, text="Chức năng")
        function_frame.pack(pady=12)
        function_frame.config(borderwidth=10, relief='solid')

        # Tạo button
        btnAdd = Button(function_frame, text="Thêm khách hàng", width=20)
        btnAdd.grid(row=0, column=0, pady=6, padx=10, ipady=3)
        
        btnSave = Button(function_frame, text="Lưu thông tin", width=20)
        btnSave.grid(row=0, column=1, pady=6, padx=10, ipady=3)
        
        btnDelete = Button(function_frame, text="Xóa khách hàng", width=20)
        btnDelete.grid(row=0, column=2, pady=6, padx=10, ipady=3)

        btnReset = Button(function_frame, text="Reset", width=20)
        btnReset.grid(row=0, column=5, pady=6, padx=10, ipady=3)
        
    def initUserData(self, userList):
        user = AdUserData()
        userDataList = user.getUserList()
        for data in userDataList:
            userList.insert('', 'end', values=data)