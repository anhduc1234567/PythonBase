import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

menu = dict()
class LearnCheckButton(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.pepsi = tkinter.IntVar()
        # self.configure(background='#999999')
        self.milk = tkinter.IntVar()
        self.tea = tkinter.IntVar()
        self.coca = tkinter.IntVar()
        self.grid_columnconfigure(0,weight=1)
        # self.grid_columnconfigure(1, weight=1)
        self.add_widget()
    def add_widget(self):

        self.frame =tkinter.Frame()
        self.frame.grid(column=0,row=0)

        self.check_pep = ttk.Checkbutton(self.frame,text='Pepsi',variable=self.pepsi,command=self.add_menu)
        self.check_pep.grid(column=0,row=0,sticky=tkinter.W)

        self.check_coca = ttk.Checkbutton(self.frame,text='Coca',variable=self.coca,command=self.add_menu)
        self.check_coca.grid(column=0, row=1,sticky=tkinter.W)

        self.check_milk = ttk.Checkbutton(self.frame,text='Milk',variable=self.milk,command=self.add_menu)
        self.check_milk.grid(column=0, row=2,sticky=tkinter.W)

        self.check_tea = ttk.Checkbutton(self.frame,text='Tea',variable=self.tea,command=self.add_menu)
        self.check_tea.grid(column=0, row=3,sticky=tkinter.W)

        self.button = ttk.Button(self.frame,text='OK',command=self.submit)
        self.button.grid(column=0,row=4)

        for i in self.frame.winfo_children():
            i.grid(pady=5)
    def add_menu(self):
        if self.pepsi.get() == 1:
           menu['pepsi'] = 'pepsi'
        elif 'pepsi' in menu:
            menu.pop('pepsi')

        if self.tea.get() == 1:
           menu['tea'] = 'tea'
        elif 'tea' in menu:
            menu.pop('tea')

        if self.milk.get() == 1:
           menu['milk'] = 'milk'
        elif 'milk' in menu:
            menu.pop('milk')

        if self.coca.get() == 1:
           menu['coca'] = 'coca'
        elif 'coca' in menu:
            menu.pop('coca')

    def submit(self):
        my_drink = ''
        for item in menu.keys():
            my_drink += menu[item] + '\n'
        showinfo(title='Your drink', message=my_drink)



if __name__ == '__main__':
    app = LearnCheckButton()
    app.mainloop()
