import tkinter
from tkinter import ttk
from tkinter.font import Font
class Slider(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.alpha = 1
        self.geometry('300x300')
        self.configure(background='red')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.configure(pady=8,padx=8)
        self.var = tkinter.DoubleVar()
        self.var_2 = tkinter.DoubleVar()
        # self.attributes('-alpha',self.alpha)
        self.my_font = Font(size=16)
        self.add_wigdet()

    def add_wigdet(self):
        self.lable = ttk.Label(text='Slider ex:',font=self.my_font)
        self.lable.grid(column=0,row=0)

        self.slider = ttk.Scale(from_=0.5,to=1,orient='horizontal',variable=self.var,command=self.chage_alpha)
        self.slider.grid(column=0,row=1,sticky=tkinter.NSEW,padx=16)

        self.slider_2 = ttk.Scale(from_=1, to=40, orient='horizontal', variable=self.var_2, command=self.chage_font)
        self.slider_2.grid(column=0, row=2, sticky=tkinter.NSEW, padx=16)

        self.lable_2 = ttk.Label(text='alpha: 0')
        self.lable_2.grid(column=0,row=3,pady=32)

        self.lable_3 = ttk.Label(text='size: 16')
        self.lable_3.grid(column=0, row=4, pady=16)

    def chage_alpha(self,event):
        alpha = self.var.get()
        self.attributes('-alpha', alpha)
        self.lable_2.configure(text=f'alpha: {alpha}')

    def chage_font(self,event):
        size = int(self.var_2.get())
        self.my_font.configure(size=size)
        self.lable_3.configure(text=f'size :{size}')




if __name__ == '__main__':
    app = Slider()
    app.mainloop()