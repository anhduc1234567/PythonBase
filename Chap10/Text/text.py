import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning
class LearnText(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.configure(pady=8,padx=16)
        self.add_widgets()
    def add_widgets(self):
        self.text = tkinter.Text(background='black',foreground='white',pady=10,padx=8)
        self.text.configure(width=30,height=5)
        self.text.grid(column=0,row=0)
        self.button = ttk.Button(text='Submit',command=self.submit)
        self.button.grid(column=0,row=2)

    def submit(self):
        str = self.text.get('1.7','2.0').strip()
        if len(str) == 0:
            showwarning(message='lỖI TEXT RỖNG')
        else:
            showinfo(message=str)


app = LearnText()
app.mainloop()
