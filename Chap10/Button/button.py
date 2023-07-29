import tkinter
from tkinter import ttk
from tkinter.messagebox import askyesno,showwarning,showinfo
from functools import partial
class LearnButton(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.photolike = tkinter.PhotoImage(file='like.png')
        self.photodislike = tkinter.PhotoImage(file='dislike.png')
        self.close = tkinter.PhotoImage(file='close.png')
        self.grid_rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.add_widget()
    def add_widget(self):
        frame = ttk.Frame(padding=8)
        frame.grid(row=0,column=0,sticky='')
        # frame.place(anchor=tkinter.CENTER,rely=0.5,relx=0.5)

        button = ttk.Button(frame,text='like')
        button.configure(image=self.photolike,compound=tkinter.LEFT)
        button.grid(row=0,column=0)
        button.configure(command=self.show_like)

        button2 = ttk.Button(frame, text='dislike',compound=tkinter.RIGHT,image=self.photodislike)
        button2.grid(row=1, column=0)
        button2.configure(command=partial(self.show_dislike,button2))


        button3 = ttk.Button(frame,text='EXIT',compound=tkinter.LEFT,image=self.close)
        button3.grid(row=2,column=0)
        button3.configure(command=self.show_yes_no)
    def show_like(self):
        showinfo(title='Information',message='Your click like!')
    def show_dislike(self,but):
        showwarning(title='dislike',message='Your click dislike!')
        but.configure(state='disable')
    def show_yes_no(self):
        rsult = askyesno(message='Bạn có chắc chắn muốn thoát không ?')
        if rsult:
            self.destroy()


app = LearnButton()
app.mainloop()