import re

def check_msv(msv):
    pattern = r'^HS\d{4}$'
    if re.match(pattern,msv):
        if int(msv[2:]) > 1000:
            return True
    return False
def check_name(name):
    pattern = r'\W+|.*[0-9_]+.*>'
    if re.match(r'\W+|.*[0-9_]+.*', name, re.UNICODE):
        return False
    return True
def check_grade(grade):
    pattern = r'^(\d{1,2}.\d{1,2})|(\d{1,2})$'
    if re.match(pattern,grade):
        # if float(grade) < 10.0:
        return True
    return False
def check_age(age):
    pattern = r'^(\d{1,3})$'
    if re.match(pattern,age):
        if int(age) <= 100 and int(age) >=4:
            return True
    return False
def check_credit(cre):
    pattern = r'^\d{1,2}$'
    if re.match(pattern,cre):
         if int(cre) > 15 or int(cre) < 1:
             return False
         return True
    return False
def check_id_sub(id):
    if re.match('^\\d{4}$',id):
        if int(id) > 1000:
            return True
    return False
def check_number_bank(num):
    if re.match('^\\d{10,14}$',num):
        return True
    return False
# msv = input('Nhập mã học sinh: ')
# print(check_msv(msv))
# name = input('Nhập ten: ')
# print(check_name(name))
# grade = input('Nhập điểm: ')
# print(check_grade(grade))
# age = input('Nhập tuổi: ')
# print(check_age(age))
# cre = input('Nhập số tín: ')
# # print(check_credit(cre)
# id_sub = input('Nhập id_subjetc: ')
# print(check_id_sub(id_sub))
num = input('Nhap so tk: ')
print(check_number_bank(num))