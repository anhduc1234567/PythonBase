import tkinter
from tkinter import ttk
import tkinter.messagebox as msg

class ConFirmDialog(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.configure(padx=8,pady=8)
        self.add_messagebox()
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def add_messagebox(self):
        frameLable = ttk.Labelframe(text='Confirm-dialog',labelanchor='n')
        frameLable.grid_columnconfigure(0,weight=1)
        frameLable.grid(column=0,row=0,sticky=tkinter.NSEW)

        button1 = ttk.Button(frameLable,text='Ok/Cancel',command=self.ok_cancel)
        button1.grid(column=0,row=1,sticky=tkinter.N,pady=4)

        button2 = ttk.Button(frameLable, text='Retry/Cancel',command=self.retry_cancel)
        button2.grid(column=0, row=2, sticky=tkinter.N, pady=4)

        button3 = ttk.Button(frameLable, text='Yes/No',command=self.ask_question)
        button3.grid(column=0, row=3, sticky=tkinter.N, pady=4)

        button4 = ttk.Button(frameLable, text='Yess/No')
        button4.grid(column=0, row=4, sticky=tkinter.N, pady=4)

    def ok_cancel(self):
        mess = msg.askokcancel(message='Bạn chắc muốn xóa chứ !')
        if mess is True:
            msg.showinfo(message='Xóa Thành công')

    def retry_cancel(self):
        mess = msg.askretrycancel(message='Tải thất bại vui lòng thử lại: ')
        if mess is True:
            msg.showinfo(message='Đang tải lại..')

    def ask_question(self):
        mess = msg.askyesnocancel(message='Nhập câu hỏi của bạn: ')
        if mess is True:
            msg.showinfo(message='You TRUE')
        elif mess is False:
            msg.showinfo(message='You FALSE')



if __name__ == '__main__':
    app = ConFirmDialog()
    app.mainloop()