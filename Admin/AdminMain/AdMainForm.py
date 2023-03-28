from tkinter import Tk, BOTH, LEFT, VERTICAL, Toplevel
from tkinter.ttk import Label, Frame, Entry, Treeview, Scrollbar, Button, LabelFrame, Combobox, Style
from PIL import Image, ImageTk
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from AdminAccount import AdAccountForm
from AdminUser import AdUserForm
from AdminOrder import AdOrderForm
from AdminProduct import AdProductForm

class AdMainForm(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        
        self.protocol('WM_DELETE_WINDOW', self.closeAll)
        
        frame1 = Frame(self, style='taskbar.TFrame')
        frame1.grid(row=0, column=0, sticky='nsew', ipadx=4)

        frame2 = Frame(self)
        frame2.grid(row=0, column=1, sticky='nsew', ipadx=4)
                
        self.frames = {}
        for frame in (AdAccountForm.AdAccountForm, AdUserForm.AdUserForm, AdOrderForm.AdOrderForm, AdProductForm.AdProductForm):
            frame_name = frame.__name__
            frame = frame(parent=frame2)
            self.frames[frame_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew", padx=20)

        self.initTaskbar(frame1)
        self.showContent('AdProductForm')
        
        self.StyleConfig()
        self.grid_rowconfigure(0, weight=1)
        
    def initTaskbar(self, frame):        
        # header logo
        self.logoImg = ImageTk.PhotoImage(Image.open('./img/shoes_logo.png'))
        logo = Label(frame, image=self.logoImg, style='taskbar.TLabel')
        logo.grid(row=0, column=0, padx=12, pady=(12, 18), columnspan=2)
        
        # product manage
        self.shoesIcon = ImageTk.PhotoImage(Image.open('./img/shoes_icon.png').resize((35, 35), Image.LANCZOS))
        shoesIconImg = Label(frame, image=self.shoesIcon, style='taskbar.TLabel')
        shoesIconImg.grid(row=1, column=0, padx=(12, 0), pady=12, sticky='w')
        
        productManage = Label(frame, text='Quản lý sản phẩm', font=('Helvetica 11'), style='taskbar.TLabel', cursor='hand2')
        productManage.grid(row=1, column=1, pady=12, sticky='w')
        productManage.bind('<Button-1>', lambda x: self.showContent('AdProductForm'))
        productManage.bind('<Enter>', self.onHover)
        productManage.bind('<Leave>', self.outHover)
        
        # order manage
        self.clipboard = ImageTk.PhotoImage(Image.open('./img/clipboard.png').resize((25, 25), Image.LANCZOS))
        clipboardImg = Label(frame, image=self.clipboard, style='taskbar.TLabel')
        clipboardImg.grid(row=2, column=0, padx=(12, 0), pady=12, sticky='w')
        
        orderManage = Label(frame, text='Quản lý đơn hàng', font=('Helvetica 11'), style='taskbar.TLabel', cursor='hand2')
        orderManage.grid(row=2, column=1, pady=12, sticky='w')
        orderManage.bind('<Button-1>', lambda x: self.showContent('AdOrderForm'))
        orderManage.bind('<Enter>', self.onHover)
        orderManage.bind('<Leave>', self.outHover)
        
        # user manage
        self.user = ImageTk.PhotoImage(Image.open('./img/user.png').resize((30, 30), Image.LANCZOS))
        userImg = Label(frame, image=self.user, style='taskbar.TLabel')
        userImg.grid(row=3, column=0, padx=(12, 0), pady=12, sticky='w')
        
        userManage = Label(frame, text='Quản lý khách hàng', font=('Helvetica 11'), style='taskbar.TLabel', cursor='hand2')
        userManage.grid(row=3, column=1, pady=12, sticky='w')
        userManage.bind('<Button-1>', lambda x: self.showContent('AdUserForm'))
        userManage.bind('<Enter>', self.onHover)
        userManage.bind('<Leave>', self.outHover)
        
        # account manage
        self.account = ImageTk.PhotoImage(Image.open('./img/user_account.png').resize((30, 30), Image.LANCZOS))
        accountImg = Label(frame, image=self.account, style='taskbar.TLabel')
        accountImg.grid(row=4, column=0, padx=(12, 0), pady=12, sticky='w')
        
        accountManage = Label(frame, text='Quản lý tài khoản', font=('Helvetica 11'), style='taskbar.TLabel', cursor='hand2')
        accountManage.grid(row=4, column=1, pady=12, sticky='w')
        accountManage.bind('<Button-1>', lambda x: self.showContent('AdAccountForm'))
        accountManage.bind('<Enter>', self.onHover)
        accountManage.bind('<Leave>', self.outHover)
        
        # logout  
        frame.grid_rowconfigure(5, weight=1)
        
        self.logoutImage = ImageTk.PhotoImage(Image.open('./img/logout_icon.png').resize((30, 30)))
        logoutImg = Label(frame, image=self.logoutImage, cursor='hand2', style='taskbar.TLabel')
        logoutImg.grid(row=5, column=0, padx=(12, 0), pady=32, sticky='ws')
        
        lblLogout = Label(frame, text='Đăng xuất', font=('Arial 11'), cursor='hand2', style='taskbar.TLabel')
        lblLogout.grid(row=5, column=1, pady=(12, 40), sticky='ws')
        lblLogout.bind('<Button-1>', lambda x: self.Logout())
        lblLogout.bind('<Enter>', self.onHover)
        lblLogout.bind('<Leave>', self.outHover)

    def onHover(self, e):
        e.widget['foreground'] = '#fd6032'
    
    def outHover(self, e):
        e.widget['foreground'] = 'black'
    
    def showContent(self, content):
        frame = self.frames[content]
        frame.tkraise()
    
    def StyleConfig(self):
        style = Style()
        style.configure('taskbar.TFrame', background='#fff')
        style.configure('taskbar.TLabel', background='#fff')
    
    def closeAll(self):
        self.parent.destroy()

    def Logout(self):
        self.parent.page.destroy()
        self.parent.deiconify()
    
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Trang quản trị')
#     app = AdMainForm(root)
#     app.geometry('1200x600+180+100')
#     root.withdraw()
#     root.mainloop()