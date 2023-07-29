import time
import tkinter
from tkinter.messagebox import showinfo
from tkinter import ttk

class Progressbar(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x400')
        self.configure(pady=8,padx=8)
        self.configure(background='#fff')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=5)
        self.image = tkinter.PhotoImage()
        self.add_progressbar()

    def add_progressbar(self):
        self.pro = ttk.Progressbar(mode='determinate',length=250)
        self.pro.grid(column=0,row=0)

        self.button = ttk.Button(text='Load',command=self.load)
        self.button.grid(column=0,row=1,pady=16)

        self.label = ttk.LabelFrame(text='My image')
        self.label.grid(column=0,row=2,sticky=tkinter.NSEW)
        self.label.grid_columnconfigure(0,weight=1)
        self.label.grid_rowconfigure(0,weight=1)
        self.my_image = ttk.Label(self.label,image=self.image)
        self.my_image.grid(column=0,row=0,sticky=tkinter.NSEW)

    def load(self):
        while self.pro['value'] != 100:
            self.update_idletasks()
            self.pro['value'] += 1
            time.sleep(0.005)
        self.pro.stop()
        self.image.configure(file=r"C:\Users\My Computer\OneDrive\Pictures\Saved Pictures\307818631_5813727278661584_8796869151710050675_n.png")
        self.my_image.configure(image=self.image)
        showinfo(message='Success')
        # self.pro.stop()

if __name__ == '__main__':
    app = Progressbar()
    app.mainloop()