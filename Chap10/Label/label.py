import tkinter
from time import sleep
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import showinfo
class LearnLabel(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.my_image = tkinter.PhotoImage(file=r"C:\Users\My Computer\OneDrive\Pictures\Saved Pictures\Screenshot_115.png")
        self.my_tym = tkinter.PhotoImage(file=r'C:\Users\My Computer\OneDrive\Pictures\Saved Pictures\images.png')
        self.is_click = False
        self.geometry('500x500')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.configure(background='#66FFCC')
        self.my_font = font.Font(family='Arial',size=14,slant='italic')
        self.add_widget()

    def add_widget(self):
        if self.is_click is False:
            self.lable = ttk.Label(text='Hello Huong ly')
            self.lable.configure(font=self.my_font,foreground='#330000',padding=10,
                                 background='#FFCC00')
        else:
            size = self.my_font['size']
            self.my_font.configure(size=size - 2, underline=True)
            self.lable.configure(text='HUONG LY', background='red')

        self.lable.configure(image=self.my_image,compound=tkinter.TOP)
        self.lable.grid(row=0,column=0)

        self.button = ttk.Button(text='Thả tym',compound='top')
        self.button.grid(row=1,column=0,pady=10)
        self.button.configure(image=self.my_tym,command=self.tha_tym)

    def tha_tym(self):
        if self.is_click is False:
            self.is_click = True
            self.add_widget()
        else:
            self.is_click = False
            self.add_widget()





app = LearnLabel()
app.mainloop()