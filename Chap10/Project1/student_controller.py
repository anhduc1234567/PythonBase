import re
from exception import *
from tkinter.messagebox import showinfo
from student import Student
class StudentController:
    def is_name_vaild(self,name):
        if len(name) < 2 or len(name) > 50:
            raise NameError(name, 'Tên không được quá dài hoặc ngắn')
        for i in name.lower():
            if i.isalpha() is False and i != ' ':
                raise NameError(name, 'Tên không hợp lệ')
        return True
    def is_birth_vaild(self,birth:str):
        pattern = r'^(0[1-9]|[1-2][0-9]|[3][0-1])/(0[1-9]|1[0-2])/\d{4}$'
        # pattern = r'^(0[1-9]|[12][0-9]|[3][0-1])/(0[1-9]|1[0-2])/\d{4}$'
        matcher = re.match(pattern,birth.strip())
        if matcher :
            return True
        else:
            raise BirthError(birth,'Ngày sinh không hợp lệ')

    def is_gpa_vaild(self,grade):
        if len(grade.strip()) == 0:
            raise GpaError(grade, 'Điểm không được trống')
        pattern = '^\\d{1}.\\d{1,2}$'
        if re.match(pattern, grade) and 0.0 < float(grade) < 4.0:
            return True
        raise GpaError(grade, 'Điểm không hợp lệ')
    def is_email_vaild(self,email):
        pattern = '^[a-z_]+[a-z]+[0-9._-]*@[a-z0-9]+.[a-z]{2,4}$'
        matcher = re.match(pattern, email, flags=re.IGNORECASE)
        if matcher:
            return True
        else:
            raise EmailError(email,'Email không hợp lệ')


    def add(self,person_id,name,birth,email,gpa,major):
        try:
            self.is_name_vaild(name)
            self.is_email_vaild(email)
            self.is_gpa_vaild(gpa)
            self.is_birth_vaild(birth)
            return Student(person_id,name,birth,None,email,gpa,major)
        except NameError as e:
            showinfo(message=e.message)
        except EmailError as e:
            showinfo(message=e.message)
        except GpaError as e:
            showinfo(message=e.message)
        except BirthError as e:
            showinfo(message=e.message)

    def read_student(self):
        students = []
        with open('student.dat','r+',encoding='UTF-8') as inp:
            while True:
                person_id = inp.readline()
                if person_id == '':
                    break
                name = inp.readline()
                birth = inp.readline()
                msv = inp.readline()
                email = inp.readline()
                gpa = inp.readline()
                maj = inp.readline()
                students.append(Student(person_id,name,birth,msv,email,gpa,maj))
        max = 1000
        for i in students:
            if int(i.student_id[2:]) > max:
                max = int(i.student_id[2:])
        Student.AUTO_ID = max + 1
        return students

    def sort_by_name(self,students:list[Student]):
        students.sort(key= lambda x:(x.name.first))

    def sort_by_gpa(self,students:list[Student]):
        students.sort(key= lambda x:(x.gpa))

    def sort_by_birth(self,students:list[Student]):
        students.sort(key= lambda x:(x.birth))


# s = StudentController()
#
# s.add(123456,'Nguyen duc anh','08/12/2004','ducanh@gmai.cm','3.45','cnntt')