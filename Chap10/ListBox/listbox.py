import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnListBox(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x350")
        self.configure(pady=8,padx=8)
        self.list_menu = tkinter.StringVar(value=str(self.getMenu()))
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.result = []
        self.add_listbox()
    def getMenu(self):
        menu = (
            'Coca',
            'Pepsi',
            'Tea',
            'Water',
            'Chick',
            'Milk',
            'Milk-Tea',
            'Ice-cream',
            'sadss',
            'asdsd'
        )
        return menu
    def add_listbox(self):
        frame = ttk.LabelFrame(text='Menu')

        frame.grid(column=0,row=0,sticky=tkinter.NSEW)
        frame.grid_columnconfigure(0,weight=1)
        frame.grid_rowconfigure(0,weight=1)
        frame.grid_rowconfigure(1, weight=1)

        self.list_box = tkinter.Listbox(frame,height=8,listvariable=self.list_menu,selectmode='extended',activestyle='none')
        self.list_box.grid(column=0,row=0,sticky=tkinter.NSEW)
        self.list_box.bind('<<ListboxSelect>>',self.list_select)

        button = ttk.Button(frame,text='OK',command=self.show_menu).grid(column=0,row=1)
    def list_select(self,event):
        self.result.clear()
        for i  in self.list_box.curselection():
            self.result.append(self.list_box.get(i))
        print(self.result)
    def show_menu(self):
        str = 'Danh sách menu của bạn là: \n'
        for i in self.result:
            str = str + i + '\n'
        showinfo(message=str)


if __name__ == '__main__':
    app  = LearnListBox()
    app.mainloop()
