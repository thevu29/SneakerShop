import tkinter as tk
from tkinter import Tk, PhotoImage, TOP, BOTH, LEFT, N, E, W, S, messagebox
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Labelframe, Style, Button
from PIL import Image, ImageTk
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Admin.AdminMain import AdMainForm
from Admin.AdminAccount import AdAccount
from Admin.AdminUser import AdUser
from Product import ProductForm

class StartForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(fill=BOTH)
        self['style'] ='loginform.TFrame'
        
        self.isAdmin = False
                
        self.initUI()
        
    def initUI(self):
        frame1 = Frame(self, style='loginform.TFrame')
        frame1.grid(row=0, column=0)
               
        self.banner = ImageTk.PhotoImage(Image.open('./img/banner.png'))
        showBanner = Label(frame1, image=self.banner, style='loginform.TLabel')
        showBanner.grid(row=0, column=0)
        showBanner.image = self.banner
        
        frame2 = Frame(self, style='loginform.TFrame')
        frame2.grid(row=0, column=1, padx=35)
        
        self.frames = {}
        for f in (LoginForm, SignUpForm):
            frame_name = f.__name__
            frame = f(parent=frame2, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame('LoginForm')
        self.StyleConfig()
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
    def showFrame(self, frameName):
        frame = self.frames[frameName]
        frame.tkraise()
     
    def StyleConfig(self):
        style = Style(self)
        style.configure('loginform.TFrame', background='#fff')
        style.configure('loginform.TLabel', background='#fff')  
        style.configure('loginform.TEntry', lightcolor='#fff')         

    def Admin(self):
        return self.isAdmin
    
class LoginForm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self['style'] ='loginform.TFrame'
        
        self.account = AdAccount.AdAccountData()
        self.accountList = self.account.getAccountList()
    
        self.initUI(controller)

    def initUI(self, controller):                
        self.header = Label(self, style='loginform.TLabel', text='Đăng nhập', font='Arial 18 bold')
        self.header.grid(row=0, column=0, pady=40, sticky=N)
        self.header.config(foreground='#fd6032')
        
        self.username = Label(self, style='loginform.TLabel', text='Tên đăng nhập:', font='Arial 10')
        self.username.grid(row=1, column=0, sticky=W)
        
        self.txtUsername = Entry(self, width=40)
        self.txtUsername.grid(row=2, column=0, pady=10, ipady=6)
        
        self.password = Label(self, style='loginform.TLabel', text='Mật khẩu:', font='Arial 10')
        self.password.grid(row=3, column=0, sticky=W)
        
        self.txtPassword = Entry(self, width=40, style='loginform.TEntry')
        self.txtPassword.grid(row=4, column=0, pady=10, ipady=5)
        
        self.btnLogin = tk.Button(self, text='Đăng nhập', width=33, bg='#fd6032', fg='white', borderwidth=0, cursor='hand2', command=self.Login)
        self.btnLogin.grid(row=5, column=0, pady=20, ipady=5)
        
        self.signUpBox = Frame(self, style='loginform.TFrame')
        self.signUpBox.grid(row=6, column=0)
        
        self.txtSignUp = Label(self.signUpBox, style='loginform.TLabel', text='Chưa có tài khoản?')
        self.txtSignUp.grid(row=0, column=0)
        
        self.signUp = Label(self.signUpBox, style='loginform.TLabel', text='Đăng ký')
        self.signUp.grid(row=0, column=1)
        self.signUp.config(foreground='#fd6032', cursor='hand2')
        
        self.signUp.bind('<Button-1>', lambda x: controller.showFrame('SignUpForm'))

    def validateEmpty(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        
        s = ''
        if username == '':
            s += 'Chưa nhập tên đăng nhập \n'
        if password == '':
            s += 'Chưa nhập mật khẩu \n'
            
        if len(s) > 0:
            messagebox.showwarning('Warning', s)
            return False
        return True
    
    def validatePassword(self):
        if self.validateEmpty() == False:
            return
        
        self.accountList = self.account.getAccountList()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        for accouunt in self.accountList:
            if accouunt[1] == username:
                if password != accouunt[2]:
                    messagebox.showerror('Error', 'Mật khẩu không trùng khớp')
                    return False
                else:
                    return True
                
        messagebox.showerror('Error', 'Tên đăng nhập không tồn tại')
        return False
                    
    def Login(self):
        if self.validatePassword() == True:
            # messagebox.showinfo('Success', 'Đăng nhập thành công')
            
            username = self.txtUsername.get()
            for account in self.accountList:
                if account[1] == username:
                    if account[3] == 'ACS001':
                        self.controller.isAdmin = True
                    else:
                        self.controller.isAdmin = False
            
            if self.controller.isAdmin == True:
                self.controller.parent.page = AdMainForm.AdMainForm(parent=self.controller.parent)
                self.controller.parent.page.geometry('1200x600+180+100')
                self.controller.parent.withdraw()
            else:
                self.controller.parent.page = ProductForm.ProductForm(parent=self.controller.parent)
                self.controller.parent.page.geometry('1200x600+180+100')
                self.controller.parent.withdraw()
            
    def reset(self):
        self.txtUsername.delete('0', 'end')
        self.txtPassword.delete('0', 'end')
    
class SignUpForm(Frame):  
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self['style'] ='loginform.TFrame'
        
        self.account = AdAccount.AdAccountData()
        self.accountList = self.account.getAccountList()
        
        self.user = AdUser.AdUserData()
        self.userList = self.user.getUserList()
        
        self.initUI(controller)
     
    def initUI(self, controller):   
        self.header = Label(self, style='loginform.TLabel', text='Đăng ký', font='Arial 18 bold')
        self.header.grid(row=0, column=0, pady=40, sticky=N)
        self.header.config(foreground='#fd6032')
        
        self.username = Label(self, style='loginform.TLabel', text='Tên đăng nhập:', font='Arial 10')
        self.username.grid(row=1, column=0, sticky=W)
        
        self.txtUsername = Entry(self, width=40, style='loginform.TEntry')
        self.txtUsername.grid(row=2, column=0, pady=10, ipady=6)
        
        self.password = Label(self, style='loginform.TLabel', text='Mật khẩu:', font='Arial 10')
        self.password.grid(row=3, column=0, sticky=W)
        
        self.txtPassword = Entry(self, width=40, style='loginform.TEntry')
        self.txtPassword.grid(row=4, column=0, pady=10, ipady=5)
        
        self.rePassword = Label(self, text='Nhập lại mật khẩu:', font='Arial 10', style='loginform.TLabel')
        self.rePassword.grid(row=5, column=0, sticky=W)
        
        self.txtRePassword = Entry(self, width=40, style='loginform.TEntry')
        self.txtRePassword.grid(row=6, column=0, pady=10, ipady=5)
        
        self.btnSignUp = tk.Button(self, text='Đăng ký', width=33, bg='#fd6032', fg='white', borderwidth=0, cursor='hand2', command=self.signUp)
        self.btnSignUp.grid(row=7, column=0, pady=20, ipady=5)
        
        self.loginBox = Frame(self, style='loginform.TFrame')
        self.loginBox.grid(row=8, column=0)
        
        self.login = Label(self.loginBox, style='loginform.TLabel', text='Đã có tài khoản?')
        self.login.grid(row=0, column=0)
        
        self.lblSwitchLogin = Label(self.loginBox, style='loginform.TLabel', text='Đăng nhập')
        self.lblSwitchLogin.grid(row=0, column=1)
        self.lblSwitchLogin.config(foreground='#fd6032', cursor='hand2')
        self.lblSwitchLogin.bind('<Button-1>', lambda x: controller.showFrame('LoginForm'))
        
    def validateEmpty(self):
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        rePasswrod = self.txtRePassword.get()
        
        s = ''
        if username == '':
            s += 'Chưa nhập tên đăng nhập \n'
        if password == '':
            s += 'Chưa nhập mật khẩu \n'
        if rePasswrod == '':
            s += 'Chưa nhập lại mật khẩu \n'
        else:
            if rePasswrod != password:
                s += 'Mật khẩu nhập không trùng khớp \n'
        
        if len(s) > 0:
            messagebox.showwarning('Warning', s)
            return False
        return True
    
    def validateUsername(self):
        if self.validateEmpty() == False:
            return
        
        username = self.txtUsername.get()
        for account in self.accountList:
            if username == account[1]:
                messagebox.showwarning('Warning', 'Tên đăng nhập đã tồn tại! \nVui lòng tạo tên đăng nhập khác')
                return False
        
        messagebox.showinfo('Success', 'Tạo tài khoản thành công! \nVui lòng đăng nhập để tiếp tục')
        return True
    
    def signUp(self):
        if self.validateUsername() == True: 
            userId = 'CUS' + str(len(self.userList) + 1).zfill(3)
            newUser = [userId, '', '', '', '', 0]
            self.user.addUser(newUser)
  
            accountId = 'ACC' + str(len(self.accountList) + 1).zfill(3)
            username = self.txtUsername.get()
            password = self.txtPassword.get()
            newAccount = [accountId, username, password, 'ACS002', userId]
            self.account.addAccount(newAccount)
            
            self.reset()
            
    def reset(self):
        self.txtUsername.delete('0', 'end')
        self.txtPassword.delete('0', 'end')
        self.txtRePassword.delete('0', 'end')