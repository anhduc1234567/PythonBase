import tkinter
from tkinter.messagebox import showinfo,showerror
from tkinter import ttk

class Subject:
    def __init__(self,id,name,credit):
        self.id = id
        self.name = name
        self.credit = credit
    def totouple(self):
        return tuple([self.id,self.name,self.credit])
class NoteBook(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # self.geometry('600x400')
        self.configure(padx=8,pady=8)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.add_note_book()
        self.add_students()
        self.add_subject()

    def add_note_book(self):
        self.note1 = ttk.Notebook()
        self.note1.grid(column=0,row=0,sticky=tkinter.NSEW)

        self.frame1 = ttk.Frame(self.note1)
        self.frame1.grid(column=0,row=0,sticky=tkinter.NSEW)
        self.note1.add(self.frame1,text='Student')

        self.frame2 = ttk.Frame(self.note1)
        self.frame2.grid_columnconfigure(0,weight=1)
        self.frame2.grid_rowconfigure(0,weight=1)
        self.frame2.grid_rowconfigure(1,weight=1)
        self.frame2.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.note1.add(self.frame2, text='Subject')

    def add_subject(self):
        column = ('c1','c2','c3')
        self.table_subject = ttk.Treeview(self.frame2,columns=column,show='headings',selectmode='browse',height=5)
        self.table_subject.grid(column = 0,row=0,sticky=tkinter.NSEW)

        self.table_subject.heading('c1',text='Id',anchor=tkinter.CENTER)
        self.table_subject.heading('c2', text='Name',anchor=tkinter.CENTER)
        self.table_subject.heading('c3', text='Credit',anchor=tkinter.CENTER)

        self.table_subject.column('c1',stretch=tkinter.NO,minwidth=100,width=200,anchor=tkinter.CENTER)
        self.table_subject.column('c2', stretch=tkinter.NO, minwidth=100, width=200,anchor=tkinter.CENTER)
        self.table_subject.column('c3',anchor=tkinter.CENTER)


        self.b1 = ttk.Button(self.frame2,text='ADD DATA',command=self.add_data_subject)
        self.b1.grid(column=0,row=1)

    def add_students(self):
        column = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
        self.table = ttk.Treeview(self.frame1,columns=column, height=7, show='headings', selectmode='browse')

        self.table.column(0, stretch=False, width=100, minwidth=100, anchor=tkinter.CENTER)
        self.table.column(1, stretch=False, width=100, minwidth=100)
        self.table.column(2, stretch=False, width=100, minwidth=100)
        self.table.column(3, stretch=False, width=100, minwidth=100)
        self.table.column(4, stretch=False, )
        self.table.column(5, stretch=False, width=100, minwidth=100)

        self.table.heading('c1', text='ID',anchor=tkinter.CENTER)
        self.table.heading("c2", text='Họ')
        self.table.heading('c3', text='Đệm')
        self.table.heading('c4', text='Tên')
        self.table.heading('c5', text='Chuyên Ngành')
        self.table.heading('c6', text='GPA')
        self.table.grid(column=0, row=0, columnspan=2, padx=8, pady=8)

    def add_data_subject(self):
        subjects = []
        with open('input.txt','r+',encoding='UTF-8') as inp:
            while True:
                id = inp.readline()
                if id == '':
                    break
                name = inp.readline()
                cre = inp.readline()
                subjects.append(Subject(id,name,cre))
        for i in subjects:

            self.table_subject.insert('',tkinter.END,values=i.totouple())


if __name__ == '__main__':
    app = NoteBook()
    app.mainloop()


