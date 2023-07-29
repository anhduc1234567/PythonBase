from tkinter import ttk
from tkinter.colorchooser import askcolor
import tkinter

class LearnColor(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.add_button()

    def add_button(self):
        ttk.Button(text='Charge color',command=self.charge_color).grid(column=0,row=0)

    def charge_color(self):
        c = askcolor()
        self.configure(background=f'{c[1]}')

if __name__ == '__main__':
    app = LearnColor()
    app.mainloop()