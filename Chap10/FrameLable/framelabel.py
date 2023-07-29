import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnFrameLabel(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x220')
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.configure(pady=5,padx=5)
        self.result_size = tkinter.StringVar()
        self.result_gender = tkinter.StringVar()

        self.add_frame1()
        self.add_frame2()
        self.creat_button()
    def creat_button(self):
        self.button  = ttk.Button(text='OK',command=self.submit)
        self.button.grid(column=0,row=1,columnspan=2,sticky=tkinter.EW)
    def add_frame1(self):
        self.frame1 = ttk.Labelframe(text='Chose your size !')
        self.frame1.grid(column=0,row=0,pady=5,padx=5,sticky=tkinter.NSEW)
        size = (
            ('Small','S'),
            ('Medium', 'M'),
            ('Large', 'L'),
            ('Extra Large', 'XL'),
            ('Extra extra Large', 'XXL')
        )
        index = 0
        for s in size:
            self.button1 = ttk.Radiobutton(self.frame1,text=s[0],variable=self.result_size,value=s[1])
            self.button1.grid(column=0,row=index,padx=4,pady=4,sticky=tkinter.W)
            index += 1

    def add_frame2(self):
        self.frame2 = ttk.Labelframe(text='Chose your gender !')
        self.frame2.grid(column=1,row=0,pady=5,padx=5,sticky=tkinter.NSEW)
        size = (
            ('Male','M'),
            ('Female', 'F'),
            ('Lesbian', 'L'),
            ('Bisexual', 'B'),
            ('Transgender', 'T')
        )
        index = 0
        for s in size:
            self.button2 = ttk.Radiobutton(self.frame2,text=s[0],variable=self.result_gender,value=s[1])
            self.button2.grid(column=0,row=index,padx=4,pady=4,sticky=tkinter.W)
            index += 1

    def submit(self):
        str = self.result_size.get() + '\n' + self.result_gender.get()
        showinfo(message=str)
if __name__ == '__main__':
    app = LearnFrameLabel()
    app.mainloop()