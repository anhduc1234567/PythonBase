import re
from exception2 import *
from student import Student,Teacher,Transcript,Subject,Course

def is_name_valid(name):
    if len(name) < 2 or len(name) > 30:
        raise NameError(name,'Tên không được để trống')
    for i in name.lower():
        if i.isalpha() is False and i != ' ':
            raise NameError(name,'Tên không hợp lệ')
    return True

def is_birth_date_valid(birth_date):
    """Phương thức kiểm tra xem ngày sinh có hợp lệ không."""
    if len(birth_date.strip()) < 10:
        raise BirthError(birth_date,'Ngày sinh không hợp lệ')
    pattern = '^\\d{2}/\\d{2}/\\d{4}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, birth_date.strip()):
        return True
    raise  BirthError(birth_date,'Ngày sinh không hợp lệ')

def is_grade_valid(grade):
    if len(grade.strip()) == 0:
        raise GpaError(grade,'Điểm không được trống')
    pattern = '^\\d{1}.\\d{1,2}$'
    if re.match(pattern,grade) and 0.0 < float(grade) < 4.0:
        return True
    raise GpaError(grade,'Điểm không hợp lệ')
def is_credit_valid(cre):
    if cre.isdigit() is False:
        raise CreditError(cre,'Credit phải là số nguyên')
    if int(cre) < 0 or int(cre) > 15:
        raise CreditError(cre,'Credit không hợp lệ')
    return True
def is_idSubject_vaild(id):
    if id.isdigit is False:
        raise SubjectIdError(id,'ID subject không hợp lệ')
    if int(id) < 1000:
        raise SubjectIdError(id,'ID subject không hợp lệ')
    return True

def is_idTeacher_valid(id):
    pattern = '^GV\\d{4}$'
    if len(id) == 6 and re.match(pattern, id, re.IGNORECASE):
        if int(id[2:]) >= 1001:
            return True
    raise TeacherIdError(id,'Id teacher không hợp lệ')
def is_idStudent_valid(id):
    pattern = '^GV\\d{4}$'
    if len(id) == 6  and re.match(pattern,id,re.IGNORECASE):
        if int(id[2:]) > 1000:
            return True
    raise StudentIdError(id,'Id student không hợp lệ')

def is_idCourse_valid(id):
    pattern = '^C\\d{3}$'
    if len(id) == 4 and re.match(pattern, id, re.IGNORECASE):
        if int(id[1:]) > 100:
            return True
    raise CourseIdError(id,'Id course không hợp lệ')

def is_idTranscript_valid(id):
    if id.isdigit() and int(id) > 100:
        return True
    raise TranscriptIdError(id,'Id Transcript không hợp lệ')
def is_salary_valid(salary):
    if salary.strip().isdigit() and int(salary) > 0:  # nếu là các con số
        return True
    raise SalaryError(salary, 'Mức lương không hợp lệ')
'''==========================================================='''
def addStudent():
    try:
        cccd = input('Nhap cccd: ')
        name = input('Nhap tên: ')
        is_name_valid(name)
        birth = input('Nhap birth: ')
        is_birth_date_valid(birth)
        major = input('Nhap chuyen nganh: ')
        gpa = input('Nhập Gpa: ')
        is_grade_valid(gpa)
        return Student(cccd,name,birth,major=major,gpa=float(gpa))
    except(ValueError,NameError,BirthError,GpaError) as e:
        print(e)
def addTeacher():
    try:
        cccd = input('Nhap cccd: ')
        name = input('Nhap tên: ')
        is_name_valid(name)
        birth = input('Nhap birth: ')
        is_birth_date_valid(birth)
        salary = input('Nhap lương: ')
        is_salary_valid(salary)
        exp = input('Nhập exp: ')
        return Teacher(int(salary),cccd,name,birth,exp=exp)
    except (ValueError,NameError,BirthError,SalaryError) as e:
        print(e)

def find_subject(ids,subject):
    for i in subject:
        if i.ids == ids:
            return i
    return None

def find_teacher(idt,subject):
    for i in subject:
        if i.ids == idt:
            return i
    return None

def add_course(subjects,teachers):
    try:
        name = input('Nham ten khoa hoc: ')
        ids = input('Nhap ids : ')
        subject = find_subject(ids,subjects)
        idt = input('Nhap idt: ')
        teacher = find_teacher(idt,teachers)
        room = input('Nhap phong: ')
        return Course(name=name,subject=subject,teacher=teacher,room = room)
    except ValueError as e:
        print(e)

def addSubject():
    try:
        name = input('Nhao ten: ')
        is_name_valid(name)
        cre = input('Nhap so tin: ')
        is_credit_valid(cre)
        return Subject(name,credit=int(cre))
    except (ValueError,NameError,CreditError) as e:
        print(e)

def print_arr(arr):
    for i in arr:
        print(i)
menu = 0
students = []
teachers = []
subjects = []
while menu != 10:
    menu = int(input('Nhap menu :  '))
    if menu == 1:
        print('===Them student===')
        students.append(addStudent())
    if menu == 2:
        print('===Thêm Teacher ===')
        teachers.append(addTeacher())
    if menu == 3:
        print('===Thêm Subject ===')
        subjects.append(addSubject())
    if menu == 5:
        print('====DANH SACH STUDENT LA====')
        print_arr(students)
    if menu == 6:
        print('===DANH SACH TEACHER LA=====')
        print_arr(teachers)
    if menu == 7:
        print('=== DANH SACH MON HOC LA====')
        print_arr(subjects)