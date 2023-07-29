from tkinter import Menu
from tkinter import ttk
import tkinter
from tkinter.messagebox import showinfo


class LearnMenu(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.configure(padx=8,pady=8)
        self.menuBar = Menu()
        self.configure(menu=self.menuBar)
        self.add_menu()
        # self.blind_event()
    def add_menu(self):
        self.file_menu = Menu(tearoff=False)
        self.menuBar.add_cascade(label='File',menu=self.file_menu,underline=0)
        self.file_menu.add_command(label='Open')
        self.file_menu.add_command(label='Save')
        self.file_menu.add_command(label='Close')


        self.menu_refactor = Menu(tearoff=False)
        self.menu_refactor.add_command(label='Rename',command=self.rename,
                                       accelerator='Shift+R')
        self.menu_refactor.add_command(label='Copy')
        self.file_menu.add_cascade(label='Refactor',menu=self.menu_refactor)

        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',command=self.destroy)

        self.menu_help = Menu(tearoff=False)
        self.menu_help.add_command(label='Welcom')
        self.menu_help.add_command(label='About us')
        self.menu_help.add_command(label='More')
        self.menuBar.add_cascade(label='Help',menu=self.menu_help)

        self.menu_color = Menu(tearoff=False)
        self.selected_color = tkinter.IntVar()
        self.menu_color.add_radiobutton(label='Red',value=1,variable=self.selected_color,
                                        command=lambda: self.change_background_color('red'),
                                        accelerator='Ctr+R')
        self.menu_color.add_radiobutton(label='Yellow', value=2,variable=self.selected_color,command=self.change_color,
                                        accelerator='Ctrl+g')
        self.menu_color.add_radiobutton(label='Green', value=3, variable=self.selected_color,
                                        command=self.change_color)

        self.menuBar.add_cascade(label='Color',menu=self.menu_color,underline=0)
        self.blind_event()
    def blind_event(self):
        self.bind_all('<Control-r>',lambda x: self.change_background_color('red'))
        self.bind_all('<Control-g>', lambda x: self.change_background_color('green'))
        self.bind_all('<Shift-R>', lambda x:self.rename())
    def change_background_color(self,color):
        self.configure(background=color)
    def rename(self):
        str = tkinter.StringVar()
        entry = ttk.Entry(textvariable=str)
        entry.grid(column=0,row=0)
        button = ttk.Button(text='OK',command=lambda :self.rename_button(str,entry,button))
        button.grid(column=1,row=0)
    def rename_button(self,str,entry,button):
        string = str.get()
        self.title(string=string)
        button.destroy()
        entry.destroy()
        showinfo(message='Rename success')


    def change_color(self):
        color = self.selected_color.get()
        if color == 1:
            self.configure(background='red')
        elif color == 2:
            self.configure(background='yellow')
        elif color == 3:
            self.configure(background='green')

if __name__ == '__main__':
    app = LearnMenu()
    app.mainloop()

    