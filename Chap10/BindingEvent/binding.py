import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo


class BindingEvent(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x150')
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.configure(padx=16,pady=16)
        self.str_email = tkinter.StringVar()
        self.str_pass = tkinter.StringVar()
        self.confirm = tkinter.IntVar(value=0)
        self.add_widgets()
        self.register_bind()
    def add_widgets(self):

        ttk.Label(text='Email: ').grid(column=0,row=0,sticky=tkinter.W,pady=4,padx=4)
        ttk.Label(text='Passwword: ').grid(column=0, row=1, sticky=tkinter.W, pady=4, padx=4)

        self.entry_email = ttk.Entry(textvariable=self.str_email)
        self.entry_email.grid(column=1,row=0,sticky=tkinter.EW)

        self.entry_pass = ttk.Entry(textvariable=self.str_pass,show='*')
        self.entry_pass.grid(column=1, row=1, sticky=tkinter.EW)

        self.agree_confirm = ttk.Checkbutton(text='Bạn có đồng ý đăng ký ?',variable=self.confirm)
        self.agree_confirm.grid(column=0,row=3,sticky=tkinter.W,pady=32)

        self.btn_ok = ttk.Button(text='OK',command=self.submit)
        self.btn_ok.grid(column=1,row=3,sticky=tkinter.E)


    def register_bind(self):
        self.btn_ok.bind('<Return>',self.submit)
        self.agree_confirm.bind('<Return>',self.confirm_check)
        self.agree_confirm.bind('<d>', self.unconfirm_check)

        self.agree_confirm.bind('<<confirm>>',self.confirm_check)
        self.btn_ok.bind('<a>',self.get_confirm_bind)
        pass

    def get_confirm_bind(self,event):
        self.agree_confirm.event_generate('<<confirm>>')

    # add binding event for root window
    # self.bind('<Return>', self.raised_event)
    # hủy liên kết tới sự kiện nhấn phím enter trên object checkbox_confirm
    # self.checkbox_confirm.unbind('<Return>')
    # self.bind_class('Button', 'Return', callback)

    def confirm_check(self,event):
        if self.confirm.get() == 0:
            self.confirm.set(1)

    def unconfirm_check(self,event):
        if self.confirm.get() == 1:
            self.confirm.set(0)
    def submit(self,*event):
        if self.confirm.get() == 0:
            showinfo(message='Yêu cầu không thành công ')
        else:
            showinfo(message='SUCCESS')

if __name__ == '__main__':
    app = BindingEvent()
    app.mainloop()