import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

class LearnRadioButton(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x200')
        self.result = tkinter.StringVar()
        self.icon = tkinter.PhotoImage(file='icon.png')
        self.add_radiobutton()
        self.grid_columnconfigure(0,weight=1)
    def add_radiobutton(self):
        index = 0
        sizes = (
            ('A', 'A is Fail'),
            ('B', 'Chính xác'),
            ('C', 'B is Fail'),
            ('D', 'C is Fail'),
        )
        frame = tkinter.Frame()
        frame.grid(column=0,row=0,pady=5,padx=5)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)

        self.lable = ttk.Label(frame,text='Chọn đáp án chính xác: ')

        self.lable.grid(column=0,row=0,columnspan=4)

        for i in sizes:
            self.choose1 = ttk.Radiobutton(frame,text=i[0],variable=self.result,value=i[1],image=self.icon,compound=tkinter.TOP)
            self.choose1.grid(column=index,row=1,pady=5,sticky=tkinter.W,padx=5)
            index += 1

        button = ttk.Button(frame,text='Submit',command=self.submit)
        button.grid(column = 0,row=2,columnspan=4,pady=10)

    def submit(self):
        str = self.result.get()
        showinfo(message=str)

if __name__ == '__main__':
    app = LearnRadioButton()
    app.mainloop()