import tkinter as tk
from tkinter import Tk, PhotoImage, TOP, BOTH, LEFT, N, E, W, S, Toplevel
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Labelframe, Style, Button
from PIL import Image, ImageTk

class StartForm(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack(fill=BOTH)
        self['style'] ='loginform.TFrame'
        self.parent.config(bg='#fff')
               
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

class LoginForm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self['style'] ='loginform.TFrame'
                        
        self.header = Label(self, style='loginform.TLabel', text='Đăng nhập', font='Arial 18 bold')
        self.header.grid(row=0, column=0, pady=40, sticky=N)
        self.header.config(foreground='#fd6032')
        
        self.txtUserName = Label(self, style='loginform.TLabel', text='Tên đăng nhập:', font='Arial 10')
        self.txtUserName.grid(row=1, column=0, sticky=W)
        
        self.userName = Entry(self, width=40)
        self.userName.grid(row=2, column=0, pady=10, ipady=6)
        
        self.txtPassword = Label(self, style='loginform.TLabel', text='Mật khẩu:', font='Arial 10')
        self.txtPassword.grid(row=3, column=0, sticky=W)
        
        password = Entry(self, width=40, style='loginform.TEntry')
        password.grid(row=4, column=0, pady=10, ipady=5)
        
        self.btnLogin = tk.Button(self, text='Đăng nhập', width=33, bg='#fd6032', fg='white', borderwidth=0)
        self.btnLogin.grid(row=5, column=0, pady=20, ipady=5)
        self.btnLogin.config(cursor='hand2')
        
        self.signUpBox = Frame(self, style='loginform.TFrame')
        self.signUpBox.grid(row=6, column=0)
        
        self.txtSignUp = Label(self.signUpBox, style='loginform.TLabel', text='Chưa có tài khoản?')
        self.txtSignUp.grid(row=0, column=0)
        
        self.signUp = Label(self.signUpBox, style='loginform.TLabel', text='Đăng ký')
        self.signUp.grid(row=0, column=1)
        self.signUp.config(foreground='#fd6032', cursor='hand2')
        
        self.signUp.bind('<Button-1>', lambda x: controller.showFrame('SignUpForm'))

class SignUpForm(Frame):  
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self['style'] ='loginform.TFrame'
         
        self.header = Label(self, style='loginform.TLabel', text='Đăng ký', font='Arial 18 bold')
        self.header.grid(row=0, column=0, pady=40, sticky=N)
        self.header.config(foreground='#fd6032')
        
        self.txtUserName = Label(self, style='loginform.TLabel', text='Tên đăng nhập:', font='Arial 10')
        self.txtUserName.grid(row=1, column=0, sticky=W)
        
        self.userName = Entry(self, width=40, style='loginform.TEntry')
        self.userName.grid(row=2, column=0, pady=10, ipady=6)
        
        self.txtPassword = Label(self, style='loginform.TLabel', text='Mật khẩu:', font='Arial 10')
        self.txtPassword.grid(row=3, column=0, sticky=W)
        
        self.password = Entry(self, width=40, style='loginform.TEntry')
        self.password.grid(row=4, column=0, pady=10, ipady=5)
        
        self.txtRePassword = Label(self, text='Nhập lại mật khẩu:', font='Arial 10', style='loginform.TLabel')
        self.txtRePassword.grid(row=5, column=0, sticky=W)
        
        self.rePassword = Entry(self, width=40, style='loginform.TEntry')
        self.rePassword.grid(row=6, column=0, pady=10, ipady=5)
        
        self.btnSignUp = tk.Button(self, text='Đăng ký', width=33, bg='#fd6032', fg='white', borderwidth=0)
        self.btnSignUp.grid(row=7, column=0, pady=20, ipady=5)
        self.btnSignUp.config(cursor='hand2')
        
        self.loginBox = Frame(self, style='loginform.TFrame')
        self.loginBox.grid(row=8, column=0)
        
        self.txtlogin = Label(self.loginBox, style='loginform.TLabel', text='Đã có tài khoản?')
        self.txtlogin.grid(row=0, column=0)
        
        self.login = Label(self.loginBox, style='loginform.TLabel', text='Đăng nhập')
        self.login.grid(row=0, column=1)
        self.login.config(foreground='#fd6032', cursor='hand2')
        
        self.login.bind('<Button-1>', lambda x: controller.showFrame('LoginForm'))
                                     
# if __name__ == '__main__':
#     root = Tk()
#     app = StartForm(root)
    
#     root.mainloop()