import re
from exception import NameError,SubjectIdError,StudentIdError,GpaError,BirthError,CreditError,RegisterIdError,NameSubjectError,AddressError

def is_name_valid(name):
    if len(name) < 2 or len(name) > 50:
        raise NameError(name,'Tên không được quá dài hoặc ngắn')
    for i in name.lower():
        if i.isalpha() is False and i != ' ':
            raise NameError(name,'Tên không hợp lệ')
    return True
def is_name_subject_valid(name):
    if len(name) < 2 or len(name) > 50:
        raise NameSubjectError(name,'Tên không được quá dài hoặc ngắn')
    for i in name.lower():
        if i.isalpha() is False and i != ' ' and i != '+' \
                and i != '_' and i != '#' and i != '.':
            raise NameSubjectError(name,'Tên không hợp lệ')
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
    if id.isdigit() is False:
        raise SubjectIdError(id,'ID subject không hợp lệ')
    if int(id) < 1000:
        raise SubjectIdError(id,'ID subject không lơn hơn 1000')
    return True
def is_idStudent_valid(id):
    pattern = '^SV\\d{4}$'
    if len(id) == 6  and re.match(pattern,id,re.IGNORECASE):
        if int(id[2:]) >= 1000:
            return True
    raise StudentIdError(id,'Id student không hợp lệ')

def is_idRegister_valid(id):
    if id.isdigit() is False:
        raise RegisterIdError(id,'Mã đăng ký phải là số')
    if int(id) < 100:
        raise RegisterIdError(id,'Id Register không hợp lệ')
    return True

def is_person_id_valid(person_id):
    if len(person_id.strip()) == 0:  # nếu chuỗi rỗng -> id ko hợp lệ
        return False
    if not person_id.isdigit() :  # nếu số cmnd/cccd có kí tự khác số và chữ cái
        return False  # mã k hợp lệ
    return True

def is_address_valid(address):
    for c in address.lower():
        if not c.isalnum() and c != ' ' and c != '+' and c != '-' and c != '.' and c != '/':
            raise AddressError(address, 'Thông tin địa chỉ không hợp lệ')
    return True