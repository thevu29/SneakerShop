from tkinter import Tk, PhotoImage, TOP, BOTH, LEFT, N, E, W, S
from tkinter.ttk import Frame, Label, Entry, Combobox, Treeview, Scrollbar, Labelframe, Style, Button
from PIL import Image, ImageTk

class StartForm(Tk):
    def __init__(self):
        Tk.__init__(self)
  
        screen_width = 950
        screen_heigth = 600
        x = int (self.winfo_screenwidth() / 2 - screen_width / 2)
        y = int (self.winfo_screenheight() / 2 - screen_heigth / 2) - 100
        self.geometry(f'{screen_width}x{screen_heigth}+{x}+{y}')
        self.config(bg='#fff')
               
        frame1 = Frame(self)
        frame1.grid(row=0, column=0)
               
        self.banner = ImageTk.PhotoImage(Image.open('./Login/img/banner.png'))
        showBanner = Label(frame1, image=self.banner)
        showBanner.grid(row=0, column=0)
        
        frame2 = Frame(self)
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
        style.theme_use('clam')
        style.configure('TFrame', background='#fff')
        style.configure('TLabel', background='#fff')  
        style.configure('TEntry', lightcolor='#fff') 
        style.configure('TButton', relief='flat', foreground='#000', focuscolor='none', borderwidth=1)            
        style.map('login.TButton', background=[('!active', '#fd6032')], foreground=[('!active', '#fff')])

class LoginForm(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
                        
        header = Label(self, text='Đăng nhập', font='Arial 18 bold')
        header.grid(row=0, column=0, pady=40, sticky=N)
        header.config(foreground='#fd6032')
        
        txtUserName = Label(self, text='Tên đăng nhập:', font='Arial 10')
        txtUserName.grid(row=1, column=0, sticky=W)
        
        userName = Entry(self, width=40)
        userName.grid(row=2, column=0, pady=10, ipady=6)
        
        txtPassword = Label(self, text='Mật khẩu:', font='Arial 10')
        txtPassword.grid(row=3, column=0, sticky=W)
        
        password = Entry(self, width=40)
        password.grid(row=4, column=0, pady=10, ipady=5)
        
        btnLogin = Button(self, text='Đăng nhập', width=39, style="login.TButton")
        btnLogin.grid(row=5, column=0, pady=20, ipady=5)
        btnLogin.config(cursor='hand2')
        
        signUpBox = Frame(self)
        signUpBox.grid(row=6, column=0)
        
        txtSignUp = Label(signUpBox, text='Chưa có tài khoản?')
        txtSignUp.grid(row=0, column=0)
        
        signUp = Label(signUpBox, text='Đăng ký')
        signUp.grid(row=0, column=1)
        signUp.config(foreground='#fd6032', cursor='hand2')
        
        signUp.bind('<Button-1>', lambda x: controller.showFrame('SignUpForm'))

class SignUpForm(Frame):  
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
         
        header = Label(self, text='Đăng ký', font='Arial 18 bold')
        header.grid(row=0, column=0, pady=40, sticky=N)
        header.config(foreground='#fd6032')
        
        txtUserName = Label(self, text='Tên đăng nhập:', font='Arial 10')
        txtUserName.grid(row=1, column=0, sticky=W)
        
        userName = Entry(self, width=40)
        userName.grid(row=2, column=0, pady=10, ipady=6)
        
        txtPassword = Label(self, text='Mật khẩu:', font='Arial 10')
        txtPassword.grid(row=3, column=0, sticky=W)
        
        password = Entry(self, width=40)
        password.grid(row=4, column=0, pady=10, ipady=5)
        
        txtRePassword = Label(self, text='Nhập lại mật khẩu:', font='Arial 10')
        txtRePassword.grid(row=5, column=0, sticky=W)
        
        rePassword = Entry(self, width=40)
        rePassword.grid(row=6, column=0, pady=10, ipady=5)
        
        btnSignUp = Button(self, text='Đăng ký', width=39, style="login.TButton")
        btnSignUp.grid(row=7, column=0, pady=20, ipady=5)
        btnSignUp.config(cursor='hand2')
        
        loginBox = Frame(self)
        loginBox.grid(row=8, column=0)
        
        txtlogin = Label(loginBox, text='Đã có tài khoản?')
        txtlogin.grid(row=0, column=0)
        
        login = Label(loginBox, text='Đăng nhập')
        login.grid(row=0, column=1)
        login.config(foreground='#fd6032', cursor='hand2')
        
        login.bind('<Button-1>', lambda x: controller.showFrame('LoginForm'))
                                     
if __name__ == '__main__':
    root = StartForm()
    root.mainloop()
    