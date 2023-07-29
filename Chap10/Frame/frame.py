from tkinter import ttk
import tkinter

class LearnFrame(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x150')
        self.grid_columnconfigure(0,weight=4)
        self.grid_columnconfigure(1,weight=1)
        self.add_frame1()
        self.app_frame2()
    def add_frame1(self):
        self.frame1 = ttk.Frame()
        self.frame1.grid(column=0, row=0)

        self.frame1.grid_columnconfigure(0,weight=1)
        self.frame1.grid_columnconfigure(1,weight=3)

        self.lable1 = ttk.Label(self.frame1,text='Find what:',background='#999999')
        self.lable1.grid(column=0,row=0,sticky=tkinter.W,pady=5)

        self.entry1 = ttk.Entry(self.frame1,width=30)
        self.entry1.grid(column=1,row=0,sticky=tkinter.EW,pady=5)

        self.lable2 = ttk.Label(self.frame1, text='Replace with:',background='#999999')
        self.lable2.grid(column=0, row=1, sticky=tkinter.W, pady=5)

        self.entry2 = ttk.Entry(self.frame1,width=30)
        self.entry2.grid(column=1, row=1, sticky=tkinter.EW, pady=5)

        self.match_case = ttk.Checkbutton(self.frame1,text='Match_case')
        self.match_case.grid(column=0,row=2,pady=5,sticky=tkinter.W)

        self.wrap = ttk.Checkbutton(self.frame1, text='Wrap around')
        self.wrap.grid(column=0, row=3,pady=5,sticky=tkinter.W)
    def app_frame2(self):
        self.frame2 = ttk.Frame()
        self.frame2.grid(column=1,row=0)

        self.button1 = ttk.Button(self.frame2,text='Find Next')
        self.button1.grid(column=0,row=0)

        self.button1 = ttk.Button(self.frame2, text='Replace')
        self.button1.grid(column=0, row=1)

        self.button1 = ttk.Button(self.frame2, text='Replace All')
        self.button1.grid(column=0, row=2)

        self.button1 = ttk.Button(self.frame2, text='Cancel')
        self.button1.grid(column=0, row=3)

        for i in self.frame2.winfo_children():
            i.grid(pady=3)

app = LearnFrame()
app.mainloop()