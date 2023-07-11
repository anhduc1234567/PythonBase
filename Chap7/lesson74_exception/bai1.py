import re
from exception1 import StudentIdError,AgeError,GradeError,FullNameError

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
    if id.isalnum() is False:
            raise StudentIdError(id,'ID không hợp lệ')
    return True
def check_name(name):
    if len(name.strip()) == 0:  # nếu chuỗi rỗng -> tên k hợp lệ
        raise FullNameError(name,'Tên không được rỗng')
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            raise FullNameError(name,'Tên không hợp lệ')
    return True
def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    pattern = "\\d*.\\d{1,3}"
    if not re.match(pattern, grade):
        raise GradeError(grade,'Điểm phải là số thực')
    return True

def is_age_valid(age_str):
    """
        Phương thức kiểm tra xem age_str có phải tuổi hợp lệ không.
        Tuổi hợp lệ chỉ chứa các kí tự số.
    """
    if age_str.isdigit() is False:
         raise AgeError(age_str,'Điểm phải là chữ số')
    return True
def create_student():
    try:
        id = input('Nhap id student ')
        check_id(id)
        name = input('Nhap ten:')
        check_name(name)
        age = input('age ')
        is_age_valid(age)
        agee = int(age)
        math_str = input('Điểm toán(hệ 10): ')
        physic_str = input('Điểm lý(hệ 10): ')
        english_str = input('Điểm tiếng Anh(hệ 10): ')
        is_grade_valid(math_str)
        is_grade_valid(physic_str)
        is_grade_valid(english_str)
        math = float(math_str)
        physic = float(physic_str)
        english = float(english_str)
        return Student(id, name, agee, math, physic, english)
    except (StudentIdError,AgeError,GradeError,FullNameError,ValueError) as e:
        print(e)

student = create_student()
print('Thông tin sinh viên:')
print(student)





