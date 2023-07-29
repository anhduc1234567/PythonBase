import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror
from tkinter.font import Font
accounts = dict()
class LearnEntry(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.resizable(False,False)
        self.email = tkinter.StringVar()
        self.password = tkinter.StringVar()
        self.email_create = tkinter.StringVar()
        self.password_create = tkinter.StringVar()
        self.login = True
        # self.configure(padx=16, pady=8)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)

        self.my_font = Font(size=25)
        self.my_font2 = Font(size=16)
        self.my_font3 = Font(size=14)


        self.interface()
    def interface(self):
        self.frame1 = ttk.Frame()
        self.frame1.grid(column=0,row=0)
        self.welcom = ttk.Label(self.frame1,text='Welcom to my app !!',font=self.my_font,foreground='#4d11ad')
        self.welcom.configure(justify='center')
        self.welcom.grid(column=0,row=0)

        if self.login is True:
            self.frame2 = ttk.Frame()
            self.frame2.grid(column=0,row=1)
            self.frame2.grid_columnconfigure(0,weight=1)
            self.frame2.grid_columnconfigure(1,weight=4)

            self.label_email = ttk.Label(self.frame2,text='Email',justify='left',font=self.my_font2)
            self.label_email.grid(row=0,column=0,ipadx=8,sticky=tkinter.W)

            self.email_entry = ttk.Entry(self.frame2,width=30)
            self.email_entry.grid(row=0,column=1,sticky=tkinter.EW,ipady=5)
            self.email_entry.configure(textvariable=self.email)


            self.password_label = ttk.Label(self.frame2,text='Password', justify='left', font=self.my_font2)
            self.password_label.grid(row=1, column=0, sticky=tkinter.W,ipadx=8)

            self.password_entry = ttk.Entry(self.frame2,width=30)
            self.password_entry.grid(row=1, column=1,ipady=5)
            self.password_entry.configure( textvariable=self.password)

            self.button = ttk.Button(self.frame2,text='Login',command=self.login_button)
            self.button.grid(row=2,column=0,columnspan=2,ipady=4,ipadx=8)

            self.button2 = ttk.Button(self.frame2,text='Creat ACC',command=self.creat_button)
            self.button2.grid(row=3, column=0, columnspan=2, ipady=4, ipadx=8)

            for i in self.frame2.winfo_children():
                i.grid(pady=5)
        else:
            self.label_email_cr = ttk.Label(self.frame2, text='Email creat', justify='left', font=self.my_font2)
            self.label_email_cr.grid(row=0, column=0, ipadx=8, sticky=tkinter.W)

            self.email_entry_cr = ttk.Entry(self.frame2, width=30)
            self.email_entry_cr.grid(row=0, column=1, sticky=tkinter.EW, ipady=5)
            self.email_entry_cr.configure(textvariable=self.email_create)

            self.password_label_cr = ttk.Label(self.frame2, text='Password craet', justify='left', font=self.my_font2)
            self.password_label_cr.grid(row=1, column=0, sticky=tkinter.W, ipadx=8)

            self.password_entry_cr = ttk.Entry(self.frame2, width=30)
            self.password_entry_cr.grid(row=1, column=1, ipady=5)
            self.password_entry_cr.configure(textvariable=self.password_create)

            for i in self.frame2.winfo_children():
                i.grid(pady=5)



    def login_button(self):
        email = self.email.get()
        passw = self.password.get()

        if len(email) == 0 or len(passw) == 0:
            showerror(message='Lỗi không đc bỏ trống')
        else:
            if email in accounts:
                if accounts[email] == passw:
                    showinfo(message='Đăng nhập thành công !')
                else:
                    showerror(message='Lỗi sai thông tin !')
            else:
                showerror(message='Lỗi sai thông tin!')

    def creat_button(self):
        if self.login is True:
            self.login = False
            self.button.configure(state='disabled')
            self.interface()
        else:
            email_cr = self.email_create.get().strip()
            pass_cr = self.password_create.get().strip()
            if len(email_cr) == 0 or len(pass_cr) == 0:
                showinfo(message='Lỗi emali và password không đc để trống')
            elif len(pass_cr) < 8:
                showinfo(message='Lỗi password lớn hơn 8 ký tự')
            else:
                if email_cr in accounts:
                    showinfo(message='Email đã tồn tại')
                else:
                    accounts[email_cr] = pass_cr
                    showinfo(message='Tạo tài khoản thành công')
                    self.label_email_cr.destroy()
                    self.password_label_cr.destroy()
                    self.login = True
                    self.interface()



app = LearnEntry()
app.mainloop()