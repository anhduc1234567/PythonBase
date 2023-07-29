import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

from student_controller import StudentController
from exception import GpaError
class EditGpaView(tkinter.Tk):
    def __init__(self,item,table):
        super().__init__()
        self.geometry('300x100')
        self.configure(pady=8,padx=8)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.add_widgets(item,table)

    def add_widgets(self,item,table):
        ttk.Label(self, text='Nhập điểm trung bình mới: ').grid(column=0, row=0, sticky=tkinter.W)
        self.entry_gpa = ttk.Entry(self)
        self.entry_gpa.grid(column=1, row=0,sticky=tkinter.E)

        btn_cancel = ttk.Button(self,text='Cancel',command=self.destroy)
        btn_cancel.grid(column=0,row=1,padx=4,pady=4)
        btn_ok = ttk.Button(self,text='OK',command=lambda :self.com_ok(item,table))
        btn_ok.grid(column=1,row=1,pady=4,padx=4)

    def com_ok(self,item,table):
        gpa = self.entry_gpa.get()
        s = StudentController()
        try:
            s.is_gpa_vaild(gpa)
            table.set(item,'c6',gpa)
            showinfo(message='Sửa thành công')
            self.destroy()
        except GpaError as e:
            showinfo(message=e.message)


if __name__ == '__main__':
    app = EditGpaView()
    app.mainloop()