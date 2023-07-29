import tkinter
from tkinter import ttk
from calendar import month_name, day_name
from tkinter.messagebox import showinfo


class ComboBox(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x250')
        self.configure(padx=8,pady=8)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.day = tkinter.StringVar()
        self.month = tkinter.StringVar()
        self.add_days()
        self.add_month()
    def get_day(self):
        day = []
        for i in day_name:
            day.append(i)
        return day
    def get_month(self):
        month = []
        for i  in month_name:
            month.append(i)
        return month

    def add_days(self):
        frame = ttk.LabelFrame(text='Chose day: ')
        frame.grid(column=0,row=0,sticky=tkinter.W)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)

        days = self.get_day()
        box_day = ttk.Combobox(frame,textvariable=self.day,values=days,height=5,state='readonly')
        box_day.current(0)
        box_day.grid(column=0,row=0,sticky=tkinter.NSEW,pady=16)
    def add_month(self):
        frame = ttk.LabelFrame(text='Chose month: ')
        frame.grid(column=1, row=0, sticky=tkinter.E)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        days = self.get_month()
        days.pop(0)
        box_day = ttk.Combobox(frame, textvariable=self.month, values=days, height=5, state='readonly')
        box_day.current(0)
        box_day.grid(column=0, row=0, sticky=tkinter.NSEW, pady=16)

        button = ttk.Button(text='OK',command=self.showinfoo)
        button.grid(column=0,row=1,columnspan=2,pady=32)

    def showinfoo(self):
        showinfo(message=f'{self.day.get()}\n{self.month.get()}')


if __name__ == '__main__':
    app = ComboBox()
    app.mainloop()