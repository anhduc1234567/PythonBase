import tkinter
from tkinter import ttk
from tkinter.font import Font
class Spinbox(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.configure(pady=8,padx=8)
        self.grid_rowconfigure(0,weight=5)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.my_font = Font(size=12)
        self.sizes = tkinter.IntVar(value=12)
        self.add_spinbox()
    def add_spinbox(self):
        self.lable = ttk.Label(text='Text spin box',font=self.my_font)
        self.lable.grid(column=0,row=0,sticky=tkinter.N)


        self.spin = ttk.Spinbox(from_=5,to=40,wrap=True,textvariable=self.sizes,command=self.charge_size,\
                                # values=([5,10,15,20,25])
                                )
        self.spin.grid(column=0,row=1)

        self.lable_size = ttk.Label(text=f'Size 12')
        self.lable_size.grid(column=0,row=1,sticky=tkinter.E)

    def charge_size(self):
        size = self.sizes.get()
        self.my_font.configure(size=size)
        self.lable_size.configure(text=f'Size: {size}')

if __name__ == '__main__':
    app = Spinbox()
    app.mainloop()