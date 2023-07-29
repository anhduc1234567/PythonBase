from tkinter import ttk
from tkinter import Menu
import tkinter
from tkinter.messagebox import showinfo, askyesno

from  student_controller import StudentController
from student import Student
from addstudentview import AddStudentView
from editgpaview import EditGpaView
def clear_treeview(treeview):
    """ Hàm tiện ích dùng để xóa toàn bộ bản ghi trong bảng(treeview)
        trước khi hiển thị thông tin mới vào đó nhằm tránh trùng lặp các bản ghi.
    """
    for item in treeview.get_children():
        treeview.delete(item)
def student_to_tuple(student:Student):
    return tuple([student.id,f'{student.name.first} {student.name.mid} {student.name.last}',
                  student.birth.strftime('%d/%m/%Y'), student.student_id,
                  student.email, f'{float(student.gpa):0.2f}',student.major])

class HomeView(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.menubar = Menu()
        self.resizable(False,False)
        self.configure(menu=self.menubar)
        self.configure(pady=8,padx=8)
        self.add_widgets()
        self.add_treeview_student()
        self.students = []
        # self.add_student_view = AddStudentView()

    def add_widgets(self):
        self.menu_file = Menu(self.menubar,tearoff=False)
        self.menubar.add_cascade(label='File',menu=self.menu_file)
        self.menu_sort = Menu(self.menu_file,tearoff=False)
        self.menu_sort.add_command(label='Sort by Name',command=self.com_sort_by_name)
        self.menu_sort.add_command(label='Sort by Gpa',command=self.com_sort_by_gpa)
        self.menu_sort.add_command(label='Sort by Birth Date',command=self.com_sort_by_birth)


        self.menu_find = Menu(self.menu_file,tearoff=False)
        self.menu_find.add_command(label='By Name')
        self.menu_find.add_command(label='By Gpa')
        self.menu_find.add_command(label='By Birth Day')
        self.menu_find.add_command(label='By Birth Month')
        self.menu_find.add_command(label='By Birth Year')


        self.menu_file.add_command(label='Create New Student',command=self.create_student)
        self.menu_file.add_command(label='Save')
        self.menu_file.add_cascade(label='Find',menu=self.menu_find)
        self.menu_file.add_cascade(label='Sort',menu=self.menu_sort)

        self.menu_file.add_separator()
        self.menu_file.add_command(label='Exit', command=self.destroy)

        self.student_note = ttk.Notebook()
        self.student_note.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.frame_student = ttk.Frame(self.student_note)
        self.frame_student.grid(column=0,row=0,sticky=tkinter.NSEW)
        self.student_note.add(self.frame_student,text='StudentManagerment')
        self.frame_student.grid_columnconfigure(0,weight=1)
        self.frame_student.grid_columnconfigure(1, weight=1)
        self.frame_student.grid_columnconfigure(2, weight=1)
        self.frame_student.grid_rowconfigure(0, weight=5)
        self.frame_student.grid_rowconfigure(1, weight=2)

    def add_treeview_student(self):
        column = ('c1','c2','c3','c4','c5','c6','c7')
        self.student_table = ttk.Treeview(self.frame_student,columns=column,height=9,show='headings',selectmode='browse')
        self.student_table.grid(column=0,row=0,sticky=tkinter.NSEW,columnspan=3)

        self.student_table.heading('c1',text='CCCD')
        self.student_table.heading('c2', text='Họ và tên')
        self.student_table.heading('c3', text='Ngày sinh')
        self.student_table.heading('c4', text='Mã sinh viên')
        self.student_table.heading('c5', text='Email')
        self.student_table.heading('c6', text='Điểm trung bình')
        self.student_table.heading('c7', text='Chuyên ngành')

        self.student_table.column(0,width=100,minwidth=100,stretch=False)
        self.student_table.column(1, width=150,minwidth=150)
        self.student_table.column(2, width=150,minwidth=150)
        self.student_table.column(3, width=150,minwidth=150)
        self.student_table.column(4, width=150,minwidth=150)
        self.student_table.column(5, width=150,minwidth=150)
        self.student_table.column(6, width=200,minwidth=200)

        self.btn_LoadStudent = ttk.Button(self.frame_student,text='LoadStudent',command=self.com_load_student)
        self.btn_LoadStudent.grid(column=0,row=1,pady=16)

        self.btn_Edit_Gpa = ttk.Button(self.frame_student, text='Edit gpa',command=self.com_edit_gpa)
        self.btn_Edit_Gpa.grid(column=1, row=1, pady=16)

        self.btn_remove = ttk.Button(self.frame_student, text='Remove item',command=self.com_remove)
        self.btn_remove.grid(column=2, row=1, pady=16)

    def create_student(self):
        popup = AddStudentView(self,self.students)
        popup.attributes('-topmost', True)  # showing popup alway on top of master frame
        popup.mainloop()

    def com_edit_gpa(self):
        item = self.student_table.selection()
        print(len(item))
        if len(item) != 0:
            edit_view = EditGpaView(item,self.student_table)
            edit_view.mainloop()
        else:
            showinfo(message='Lỗi danh sách rỗng')

    def com_remove(self):
        item = self.student_table.selection()
        if len(item) == 0 :
            showinfo(message='Lỗi danh sách rỗng')
        else:
            ask =  askyesno(message='Bạn có chắc chắn muốn xóa ?')
            if ask :
                for i in item:
                    self.student_table.delete(i)
                showinfo(message='Xóa thành công')



    def com_load_student(self):
        self.students.clear()
        s = StudentController()
        self.students = s.read_student()
        self.show_student_in_table()
    def show_student_in_table(self):
        clear_treeview(self.student_table)
        index = 1
        self.student_table.selection_clear()
        for student in self.students:
            if index % 2 == 0:
                tag = 'even'
            else:
                tag = 'odd'
            self.student_table.insert('', tkinter.END, values=student_to_tuple(student), tags=(tag,))
            index += 1

    def com_sort_by_name(self):
        s = StudentController()
        s.sort_by_name(self.students)
        self.show_student_in_table()

    def com_sort_by_gpa(self):
        s = StudentController()
        s.sort_by_gpa(self.students)
        self.show_student_in_table()

    def com_sort_by_birth(self):
        s = StudentController()
        s.sort_by_birth(self.students)
        self.show_student_in_table()

if __name__ == '__main__':
    app = HomeView()
    app.mainloop()
    # p = AddStudentView()
    # p.mainloop()