import tkinter
from tkinter import ttk
import tkinter.filedialog as fd

class LearnFileDialog(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('100x100')
        self.btn = ttk.Button(text='Select file:',command=self.open_file).grid(column=0,row=0)
    def open_file(self):
        file_path = fd.askopenfilename()
        with open(file_path,'r+',encoding='UTF-8') as inp:
            print(inp.read())

if __name__ == '__main__':
    app = LearnFileDialog()
    app.mainloop()