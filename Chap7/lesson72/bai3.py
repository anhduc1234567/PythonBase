import re

from student import Student,Subject,Teacher,Transcript,Course

def is_name_valid(name):
    if len(name) > 30 or len(name) < 2:
        return False
    for i in name.lower():
        if not  i.isalpha() and i != ' ':
            return False
    return True
def is_gpa_valid(gpa):
    pattern = "\\d*.\\d{1,3}"
    if not re.match(pattern, gpa):
        return False
    if float(gpa) < 0.0 or float(gpa) > 4.0:
        return False
    return True
def is_salary_valid(salary):
    if salary.isnumeric() is False:
        return False
    return True
def is_credit_valid(cre):
    if cre.isnumeric() is False:
        return False
    if isinstance(cre,int) is False:
        return False
    if int(cre) < 1 or int(cre) > 15:
        return False
    return True
def is_CCCD(id):
    if id.isnumeric() is False:
        return False
    if len(id) != 12:
        return False
    return True

def creat_student():
    id = input("Nhập CCCD: ")
    if is_CCCD(id) is False:
        raise ValueError('CCCD KHÔNG HỢP LỆ')
    name = input("Nhập tên: ")
    if is_name_valid(name) is False:
        raise ValueError('Tên không hợp lệ')
    birth = input("Nhập ngày sinh: ")
    major = input("Nhập chuyên ngành: ")
    gpa = input("Nhập gpa: ")
    if is_gpa_valid(gpa) is False:
        return ValueError('Điểm lỗi: ')
    return Student(int(id),name,birth,major=major,gpa= gpa)

def print_arr(arr):
    for i in arr:
        print(i)
students = []
try:
    students.append(creat_student())
except ValueError as e:
    print(e)
else:
    print("Hoàn Thành: ")
print_arr(students)


