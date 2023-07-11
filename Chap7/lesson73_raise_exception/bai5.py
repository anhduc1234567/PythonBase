import datetime
import re

class FullName:
    def __init__(self,first,mid,last):
        self.first = first
        self.mid = mid
        self.last = last
    def __str__(self):
        return f'{self.first} {self.mid} {self.last:10}'

class Birth:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

class Student:
    AUTO_ID = 1000
    def __init__(self,id = '',name = '',birth = '',msv = None,gpa = 0.0,major = ''):
        self.id = id
        self.name = name
        self.birth = birth
        self.gpa = gpa
        self.major = major
        if msv == None:
            self.msv = f"SV{Student.AUTO_ID}"
            Student.AUTO_ID += 1
        else:
            self.msv = msv
    def __str__(self):
        return f'{self.id} {self.msv} {self.name} {self.birth} {self.major} {self.gpa}'

class Subject:
    AUTO_ID = 1000
    def __init__(self,id = None,name = '',credit = 0):
        self.name = name
        self.credit = credit
        if id is None:
            self.id = Subject.AUTO_ID
            Subject.AUTO_ID += 1
        else:
            self.id = id
    def __str__(self):
        return f'{self.id} {self.name} {self.credit}'

class Register:
    AUTO_ID = 100
    def __init__(self,id =None ,student = None, subject = None,time =None):
        if id == None:
             self.id = Register.AUTO_ID
             Register.AUTO_ID += 1
        else:
            self.id = id
        self.student = student
        self.subject = subject
        if time == None:
            self.time = datetime.datetime.now()
        else:
            self.time = time

    def __str__(self):
        date_str = f'{self.time.day:02}/{self.time.month:02}/' \
                   f'{self.time.year:4} {self.time.hour:02}:' \
                   f'{self.time.minute:02}:{self.time.second:02}'
        return f'{self.id:<10}{self.student.id:10} {self.student.name}' \
               f'{self.subject.id:10} {self.subject.name}' \
               f'{date_str:25}'

    '''ièmiejf'''
def is_name_valid(name):
    if len(name.strip()) == 0:  # nếu chuỗi rỗng -> tên k hợp lệ
        raise ValueError("Tên không hợp lệ")
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            raise ValueError('Tên không hợp lệ')
    return True

def is_birth_valid(birth_date):
    if len(birth_date.strip()) < 10:
        raise ValueError('Ngày sinh không hợp lệ')
    pattern = '^\\d{2}/\\d{2}/\\d{4}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, birth_date.strip()):
        return True
    raise ValueError('Ngày sinh không hợp lệ')

def is_gpa_valid(gpa_str):
    if len(gpa_str.strip()) == 0:
        return False
    pattern = '^\\d.\\d{1,2}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, gpa_str):
        return True
    else:
        raise ValueError('GPA không hợp lệ')
def is_credit_valid(credit_str):
    """Phương thức kiểm tra số tín chỉ có hợp lệ không."""
    if len(credit_str.strip()) == 0:
        raise ValueError('Credit không hợp lệ')
    if credit_str.isdigit():
        if int(credit_str) > 1 and int(credit_str) < 15:
             return True
    raise ValueError('Credit không hợp lệ')
def is_is_valid(id):
    if id.isalnum() is False:
        raise ValueError('id không hợp lệ')
    return True
def creat_students():
    student = []
    with open('student.dat','r+',encoding='UTF-8') as inp:
        try:
             while True:
                id = inp.readline().strip()
                if id == '':
                    break
                is_is_valid(id)
                name = inp.readline().strip()
                is_name_valid(name)
                birth = inp.readline().strip()
                is_birth_valid(birth)
                msv = inp.readline().strip()
                gpa = inp.readline().strip()
                is_gpa_valid(gpa)
                major = inp.readline().strip()
                student.append(Student(id,name,birth,msv,float(gpa),major))
        except ValueError as e:
                print(e)
    return student
def add_student(students):
    try:
        id = input('Nhap ID: ')
        is_is_valid(id)
        name = input('Nhap ten: ')
        is_name_valid(name)
        birth = input('Nhap ngày sinh: ')
        is_birth_valid(birth)
        gpa = input('Nhap gpa: ')
        is_gpa_valid(gpa)
        major = input('Nhap chuyen nganh: ')
        students.append(Student(id,name,birth,gpa=float(gpa),major=major))
    except ValueError as e:
        print(e)
def creat_subject():
    sub = []
    with open('subject.DAT','r+',encoding='UTF-8') as inp:
        try:
            while True:
                id = inp.readline().strip()
                if id == '':
                    break
                name = inp.readline().strip()
                credit = inp.readline().strip()
                is_credit_valid(credit)
                sub.append(Subject(id,name,int(credit)))
        except ValueError as e:
            print(e)
    return sub


def print_arr(arr):
    for i in arr:
        print(i)

students = creat_students()
subjects = creat_subject()
menu = 0
while menu != 10:
    menu = int(input('Nhap menu: '))

    if menu == 1:
        print("==THEM 1 SINH VIEN VAO DANH SÁCH-===")
        add_student(students)
    if menu == 5:
        print("DANH SACH SINH VIEN LA:")
        print_arr(students)
    if menu == 6:
        print('--DANH SACH MON HOC LA:---')
        print_arr(subjects)
