import tkinter
from tkinter import ttk

class EditGpaView(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')
        self.add_widgets()
    def add_widgets(self):

        ttk.Label(self,text='Nhập điểm trung bình mới: ').grid(column=0,row=0,sticky=tkinter.W)
        self.entry_gpa = ttk.Entry(self)
        self.entry_gpa.grid(column=1,row=0)