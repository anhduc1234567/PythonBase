

import datetime


class Person:
    def __init__(self,id = '',name ='NoName',birth = '01/01/2020'):
        self.id = id
        self.name = name
        self.birth = birth
    def __str__(self):
        return f'ID: {self.id} Name: {self.name}   '\
                f'Birth: {self.birth}'
class Student(Person):
    ID_AUTO = 1000
    def __init__(self,gpa = 0.0,major = '', id = '', name = 'NoName', birth = '01/01/2020'):
        super().__init__(id,name,birth)
        self.msv = f'SV{Student.ID_AUTO}'
        self.gpa = gpa
        self.major = major
        Student.ID_AUTO += 1
    def __str__(self):
        return f'{super().__str__()} MSV: {self.msv} '\
                f'{self.major} Gpa: {self.gpa}'
class Subject:
    ID_AUTO = 1000
    def __init__(self,name = '',sotin = 0):
        self.id = Subject.ID_AUTO
        self.name = name
        self.sotin = sotin
        Subject.ID_AUTO += 1
    def __str__(self):
        return f'{self.id} {self.name} {self.sotin}'

class Register:
    AUTO_ID = 1000
    def __init__(self,subject,student):
        self.id = Register.AUTO_ID
        self.subject = subject
        self.student = student
        Register.AUTO_ID += 1
        self.time = datetime.datetime.now()

    def __str__(self):
        date_str = f'{self.time.day:02}/{self.time.month:02}/' \
                   f'{self.time.year:4} {self.time.hour:02}:' \
                   f'{self.time.minute:02}:{self.time.second:02}'
        return f'{date_str} {self.id} {self.subject.name} {self.student.name}'

def creat_student():
    students = []
    with open("student.dat",'r+',encoding="UTF-8") as inp:
        while True:
            cccd = inp.readline().strip()
            if cccd == '':
                break
            name = inp.readline().strip()
            birth = inp.readline().strip()
            msv = inp.readline().strip()
            gpa = float((inp.readline()).strip())
            major = inp.readline().strip()
            students.append(Student(gpa,major,cccd,name,birth))
    return students
def creat_subject():
    subject = []
    with open('subject.dat','r+',encoding= 'UTF-8') as inp:
        while True:
            subject_id = inp.readline().strip()
            if  subject_id == '':
                break
            name = inp.readline().strip()
            sotin = int(inp.readline().strip())
            subject.append(Subject(name,sotin))
    return subject
def print_arr(arr):
    for i in arr:
        print(i)
def find_student_by_id(stu,id):
    for i in stu:
        if i.msv.lower() == id.lower():
            return i
    return None
def update_student_name(students):
    """Phương thức dùng để cập nhật tên sinh viên theo mã sinh viên cho trước."""
    student_id = input('Mã sinh viên cần cập nhật: ')
    student = find_student_by_id(students, student_id)
    if student is not None:
        full_name = input('Họ và tên mới: ')
        try:
            student.full_name = full_name
            print('==> Cập nhật điểm cho sinh viên thành công! <==')
        except ValueError as e:
            print(e)
    else:
        print("LOI")

students = []
try:
    students = creat_student()
except Exception:
    print("LOi xay ra ngoai le")
subject = creat_subject()
print_arr(students)
print()

print_arr(subject)
update_student_name(students)