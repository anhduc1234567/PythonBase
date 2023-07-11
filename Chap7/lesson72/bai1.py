import re


class Student:
    def __init__(self,name = None,id = None,
                 age = 0,math = 0.0,english=0.0,physical=0.0):
        self.id = id
        self.name = name
        self.age = age
        self.math = math
        self.english = english
        self.physical = physical

    def __str__(self):
        return f'{self.id} {self.name} {self.math} {self.age} {self.english} {self.physical}'
def check_id(id):
    for i in id.lower():
        if i < '0' or i > '9'  and ('a' > i or i > 'z'):
            return False
    return True
def check_name(name):
    if len(name.strip()) == 0:  # nếu chuỗi rỗng -> tên k hợp lệ
        return False
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            return False
    return True
def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    pattern = "\\d*.\\d{1,3}"
    if not re.match(pattern, grade):
        return False
    return True

def is_age_valid(age_str):
    """
        Phương thức kiểm tra xem age_str có phải tuổi hợp lệ không.
        Tuổi hợp lệ chỉ chứa các kí tự số.
    """
    for c in age_str:
        if c < '0' or c > '9':
            return False
    return True
def create_student():
    id = input('Nhap id student ')
    if check_id(id) is not True:
        raise ValueError('MA SV K HOP LE ')
    name = input('Nhap ten:')
    if check_name(name) is not True:
        raise ValueError("TEN KHONG HOP LE ")
    age = input('age ')
    if is_age_valid(age) is not True:
        raise ValueError('Nhap sai tuoi ')
    else:
        agee = int(age)
    math_str = input('Điểm toán(hệ 10): ')
    physic_str = input('Điểm lý(hệ 10): ')
    english_str = input('Điểm tiếng Anh(hệ 10): ')
    if is_grade_valid(math_str) is False or is_grade_valid(physic_str) is False  or is_grade_valid(english_str) is False:
        raise ValueError('Điểm không hợp lệ')
    math = float(math_str)
    physic = float(physic_str)
    english = float(english_str)
    return Student(id, name, agee, math, physic, english)


try:
    student = create_student()
    print('Thông tin sinh viên:')
    print(student)
except ValueError as e:
    print(e)

finally:
    print('Done!!')


