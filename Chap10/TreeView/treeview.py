import tkinter
from tkinter import ttk
import tkinter.messagebox as msg
class Student:
    def __init__(self,id,name:str,major,gpa,gender):
        self.id = id
        self.name = name
        self.major = major
        self.gpa = gpa
        self.setName(name)
        self.gender = gender
    def setName(self,name:str):
        names = name.strip().split()
        self.ho = names[0]
        self.ten = names[len(names) - 1]
        mid = ''
        for i in range(1,len(names)-1):
            mid += names[i] + ' '
        self.dem = mid.strip()

    def totuple(self):
        return tuple([self.id,self.ho,self.dem,self.ten,self.major,self.gpa])

class TreeView(tkinter.Tk):
    def __init__(self):
        super().__init__()
        # self.geometry('700x400')
        self.configure(pady=8,padx=8)
        self.resizable(False,False)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.msv = tkinter.StringVar()
        self.first = tkinter.StringVar()
        self.mid = tkinter.StringVar()
        self.last = tkinter.StringVar()
        self.major = tkinter.StringVar()
        self.gpa = tkinter.StringVar()
        self.add_widgets()

    def read_data(self):
        with open('input.txt','r+',encoding='UTF-8') as inp:
            students = []
            while True:
                id = inp.readline()
                if id == '':
                    break
                name = inp.readline()
                gender = inp.readline()
                major = inp.readline()
                gpa = inp.readline()
                students.append(Student(id,name,major,gpa,gender))
            return students
    def add_widgets(self):
        column = ('c1','c2','c3','c4','c5','c6')
        self.table = ttk.Treeview(columns=column,height=7,show='headings',selectmode='browse')

        self.table.column(0, stretch=False, width=100,minwidth=100,anchor=tkinter.CENTER)
        self.table.column(1, stretch=False, width=100,minwidth=100)
        self.table.column(2, stretch=False, width=100,minwidth=100)
        self.table.column(3, stretch=False, width=100,minwidth=100)
        self.table.column(4, stretch=False,)
        self.table.column(5, stretch=False, width=100,minwidth=100)

        self.table.heading('c1', text='ID')
        self.table.heading("c2", text='Họ')
        self.table.heading('c3', text='Đệm')
        self.table.heading('c4', text='Tên')
        self.table.heading('c5', text='Chuyên Ngành')
        self.table.heading('c6', text='GPA')
        self.table.grid(column=0,row=0,columnspan=2,padx=8,pady=8)

        self.table.bind('<<TreeviewSelect>>',self.update_data)

        self.button_load = ttk.Button(text='Load Data',command=self.fill_table)
        self.button_load.grid(column=0,row=1,padx=8,pady=8)

        self.button_dete = ttk.Button(text='Delete Data', command=self.remove_data)
        self.button_dete.grid(column=1, row=1, padx=8, pady=8)

        self.button_set = ttk.Button(text='Set Data', command=self.set_data)
        self.button_set.grid(column=0, row=2, padx=8, pady=8)

        self.frame = ttk.LabelFrame(text='Update data: ')
        self.frame.grid(row=3,column=0,columnspan=2)

        self.label_id = ttk.Label(self.frame,text='Id: ')
        self.label_id.grid(row=0,column=0,sticky=tkinter.W,padx=8)
        self.entry_id = ttk.Entry(self.frame,textvariable=self.msv,state='disable')
        self.entry_id.grid(column=1,row=0,sticky=tkinter.E)

        self.label_first = ttk.Label(self.frame, text='First: ').grid(row=1, column=0, sticky=tkinter.W, padx=8)
        self.entry_first = ttk.Entry(self.frame, textvariable=self.first,state='disable')
        self.entry_first.grid(row=1, column=1, sticky=tkinter.E)

        self.label_mid = ttk.Label(self.frame, text='Mid: ').grid(row=2, column=0, sticky=tkinter.W, padx=8)
        self.entry_mid = ttk.Entry(self.frame, textvariable=self.mid,state='disable')
        self.entry_mid.grid(row=2, column=1, sticky=tkinter.E)


        self.label_last = ttk.Label(self.frame, text='Last: ').grid(row=3, column=0, sticky=tkinter.W, padx=8)
        self.entry_last = ttk.Entry(self.frame, textvariable=self.last,state='disable')
        self.entry_last.grid(row=3, column=1, sticky=tkinter.E)

        self.label_major = ttk.Label(self.frame, text='Major: ').grid(row=4, column=0, sticky=tkinter.W, padx=8)
        self.entry_major = ttk.Entry(self.frame, textvariable=self.major,state='disable')
        self.entry_major.grid(row=4, column=1, sticky=tkinter.E)

        self.label_gpa = ttk.Label(self.frame, text='Gpa: ').grid(row=5, column=0, sticky=tkinter.W, padx=8)
        self.entry_gpa = ttk.Entry(self.frame, textvariable=self.gpa,state='disable')
        self.entry_gpa.grid(row=5, column=1, sticky=tkinter.E)

    def update_data(self,event):
        self.entry_id['state'] = 'normal'
        self.entry_gpa['state'] = 'normal'
        self.entry_major['state'] = 'normal'
        self.entry_first['state'] = 'normal'
        self.entry_mid['state'] = 'normal'
        self.entry_last['state'] = 'normal'

    def fill_table(self):
        data = self.read_data()
        for i in data:
            self.table.insert('',tkinter.END,values=i.totuple())


    def remove_data(self):
        data = self.table.selection()
        if len(data) == 0 :
            msg.showinfo(message='Lỗi chưa chọn phần tử nào!')
        else:
            ask = msg.askyesno(message='Are you sure ?')
            if ask:
                for i in data:
                    self.table.delete(i)
    def set_data(self):
        item = self.table.selection()
        id = self.msv.get()
        first = self.first.get()
        mid = self.mid.get()
        major = self.major.get()
        last = self.last.get()
        gpa = self.gpa.get()

        column = ('c1','c2')
        if len(id) != 0 and len(first) != 0 and len(mid) != 0 and len(last) != 0 and len(major) !=0 and len(gpa) != 0:
            for i in item:
                data_id = self.table.set(i,'c1',id)
                data_ho = self.table.set(i, 'c2',first)
                data_dem = self.table.set(i, 'c3',mid)
                data_ten = self.table.set(i, 'c4',last)
                data_major = self.table.set(i, 'c5',major)
                data_gpa = self.table.set(i, 'c6',gpa)
        else:
            msg.showinfo(message='Khong duoc bo trong')


if __name__ == '__main__':
    app = TreeView()
    app.read_data()

    app.mainloop()