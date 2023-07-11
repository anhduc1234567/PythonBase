from student import *
from filter import *
from database import *

def print_arr(arr):
    for i in arr:
        print(i)

def create_student():
    '''Thêm một sinh viên vào danh sách'''
    print('======Nhập thông tin sinh viên=========')
    pid = input('Nhập CCCD: ')
    name = input('Nhập họ và tên: ')
    birth = input('Nhập ngày tháng năm sinh theo định dạng:'
                  'dd/mm/yyyy: ')
    address = input('Nhập địa chỉ: VD: (Thụy Huong-Chuong My-Ha Noi)')
    email = input('Email: ')
    major = input('Major: ')
    gpa = input('Nhập điểm TB: ')
    return Student(None,email,gpa,major,pid,name,birth,address)

def find_full_name_by_id(list_name, name_id):
    for name in list_name:
        if name[0] == name_id:
            return name
    return None


def find_address_by_id(list_address, addr_id):
    for addr in list_address:
        if addr[0] == addr_id:
            return addr
    return None


def find_birth_date_by_id(list_dob, dob_id):
    for dob in list_dob:
        if dob[0] == dob_id:
            return dob
    return None
def find_student_by_id(students,id):
    for i in students:
        if i.student_id.lower() == id.lower():
            return i
    return None

def find_subject_by_id(subjects, subject_id):
    """Phương thức tìm môn học theo mã môn học."""
    for s in subjects:
        if s.subject_id == subject_id:
            return s
    return None

def is_register_exists(register,id_student,id_subject):
    for r in register:
        if r.student.student_id == id_student.upper() and r.subject.subject_id == id_subject:
            return True
    return False

def is_register_exist(registers, r):
    """Kiểm tra xem bản đăng ký đã tồn tại trước đó chưa."""
    for item in registers:
        if item == r:
            return True
    return False

def creat_subject():
    '''Tạo 1 môn học thêm vào danh sách'''
    print('=========Nhập thông tin môn học==========')
    name = input('Nhap tên: ')
    credit = input('Nhập số tín: ')
    return Subject(None,name,credit)

def creat_register(registers,students,subjects):
    '''Tạo một bản đăng ký: '''
    student = None
    subject = None
    print('=====Nhập thông tin: ========')
    student_id = input('Nhập mã sinh viên: ')
    try:
         if is_idStudent_valid(student_id):
             student = find_student_by_id(students,student_id)
             if student is None:
                 print('Student không tồn tại:')
                 return None
    except StudentIdError as e:
        print(e)
        return None

    subject_id = input('Nhập mã môn học: ')
    try:
        if is_idSubject_vaild(subject_id):
            subject = find_subject_by_id(subjects,subject_id)
            if subject is None:
                print(f'==> Môn học mã \'{subject_id}\' không tồn tại.')
                return None
    except SubjectIdError as e:
        print(e)
        return None
    if is_register_exists(registers, student_id, subject_id):
        print(f'==> Sinh viên mã {student_id} đã đăng ký môn học {subject_id} trước đó.')
        return None
    else:
        return Register(None, None, student, subject)

def read_student_from_database():
    students = []
    data = get_student()
    list_birth = get_birth_date()
    list_full_name = get_full_name()
    list_address = get_address()
    for i in data:
        name = find_full_name_by_id(list_full_name,i[2]) # là 1 list
        full_name = FullName(name[0],name[1],name[2],name[3])
        birth = find_birth_date_by_id(list_birth,i[4])
        birth_date = BirthDate(int(birth[0]),int(birth[1]),int(birth[2]),int(birth[3]))
        addr = find_address_by_id(list_address, i[3])
        address = Address(addr[0], addr[3], addr[1], addr[2])
        students.append(Student(i[0],i[5],str(i[6]),i[7],i[1],full_name,birth_date,address))
    return students

def read_subject_from_database():
    subjects = []
    data = get_subject()
    for i in data:
        ids = str(i[0])
        name = i[1]
        cre = i[2]
        subjects.append(Subject(ids,name,cre))
    return subjects
def read_register_from_database(students,subjects):
    register = []
    data = get_register()
    for r in data:
        id = r[0]
        student_id = r[1]
        student = find_student_by_id(students,f'{student_id}')
        subject_id = r[2]
        subject = find_subject_by_id(subjects,str(subject_id))
        time = r[3]
        register.append(Register(id,time,student,subject))
    return register

def update_autoid_Student(students):
    max = 1000
    for i in students:
        if int(i.student_id[2:]) > max:
            max = int(i.student_id[2:])
    Student.AUTO_ID = max + 1
def update_autoid_Subject(subject):
    max = 1000
    for i in subject:
        if int(i.subject_id) > max:
            max = int(i.subject_id)
    Subject.AUTO_ID = max + 1
def update_autoid_Register(register):
    max = 100
    for i in register:
        if int(i.register_id) > max:
            max = int(i.register_id)
    Register.AUTO_ID = max + 1

def sort_registers(registers):
    registers.sort(key=lambda x:(x.register_time.year,x.register_time.month,
                                 x.register_time.day,x.register_time.hour,
                                 x.register_time.minute,x.register_time.second
                                 ))
def save_student(student):
    fullname_data = (student.full_name.first,student.full_name.mid,student.full_name.last)
    full_name_id = insert_full_name(fullname_data)
    birth_data = (student.birth.day,student.birth.month,student.birth.year)
    birth_id = insert_birth(birth_data)
    address_data = (student.address.wards,student.address.district,student.address.city)
    address_id = insert_address(address_data)
    student_data = (student.student_id,student.idp,full_name_id,
                    address_id,birth_id,student.email,
                    student.gpa,student.major)
    insert_student(student_data)
def list_subjects_by_id(subjects,registers):
    '''liệt kê danh sách mon học mà sv đã đăng ký theo id'''
    id = input('Nhập mã sinh viên: ')
    try:
        if is_idStudent_valid(id):
            print(f'DANH SACH MÔN HOC MA SINH VIEN {id}')
            for i in registers:
                if i.student.student_id == id:
                    print(i)
    except StudentIdError as e:
        print(e)
def list_students_register_subject(registers,students):
    id_sub = input('Nhập mã môn học: ')
    result = []
    try:
        if is_idSubject_vaild(id_sub):
            for i in registers:
                if i.subject.subject_id == id_sub:
                    result.append(find_student_by_id(students,i.student.student_id))
        if len(result) > 0:
            print(f'===DANH SACH SINH VIEN ĐÃ ĐĂNG KÝ MÔN HỌC {id_sub}')
            print_arr(result)
        else:
            print('CHƯA CO SINH VIEN NÀO ĐĂNG KÝ')
    except SubjectIdError as e:
        print(e)

def save_subjetc(subject):
    subject_data = (subject.subject_id,subject.subject_name,subject.credit)
    insert_subject(subject_data)
def save_registers(register):
    register_data = (register.register_id,register.student.student_id,
                     register.subject.subject_id,register.register_time)
    insert_register(register_data)
def static_number_subject():
    '''Thông kê số lương sinh viên đăng ký theo từng môn học'''
    result = static_subject()
    for i in result:
        print(f'{i[0]} {i[1]} {i[2]}')
def static_number_studentscity():
    '''Thông kê số lương sinh viên đăng ký theo từng môn học'''
    result = static_student_by_city()
    for i in result:
        print(f'{i[0]} {i[1]} ')
def static_number_subject_by_dict(register):
    '''Thông kê số lương sinh viên đăng ký theo từng môn học'''
    dict = {}
    for i in register:
        if i.subject.subject_id in dict:
            dict[i.subject.subject_id] += 1
        else:
            dict[i.subject.subject_id] = 1
    for i in dict.keys():
        print(f'{i} {dict[i]}')
def list_student_good():
    data = students_gpa_good()
    students = []
    list_birth = get_birth_date()
    list_full_name = get_full_name()
    list_address = get_address()
    for i in data:
        name = find_full_name_by_id(list_full_name, i[2])  # là 1 list
        full_name = FullName(name[0], name[1], name[2], name[3])
        birth = find_birth_date_by_id(list_birth, i[4])
        birth_date = BirthDate(int(birth[0]), int(birth[1]), int(birth[2]), int(birth[3]))
        addr = find_address_by_id(list_address, i[3])
        address = Address(addr[0], addr[3], addr[1], addr[2])
        students.append(Student(i[0], i[5], str(i[6]), i[7], i[1], full_name, birth_date, address))
    return students
def stat_student_same_city():
    '''Liệt kê các sinh viên trong cùng 1 thành phố'''
    data = student_in_same_city()
    for i in data:
        print(i)
def list_register_earliest(students):
    '''TOP5 5 học sinh đăng ký sớm nhất'''
    data = student_register_soonest()
    for i in data:
        student = find_student_by_id(students,i[0])
        print(student, i[1])
def list_student_gpa_high(students):
    data = student_gpa_highest()
    for i in data:
        student = find_student_by_id(students,i[0])
        print(student)

def find_students_gpa_nd2(students):
    max = 0.0
    for i in students:
        if float(i.gpa) > max:
            max = float(i.gpa)
    second = 0.0
    for i in students:
        if float(i.gpa) > second and float(i.gpa) != max:
            second = float(i.gpa)
    for i in students:
        if float(i.gpa) == second:
            print(i)

def stat_scond_max_gpa(students):
    result = find_second_max_gpa()
    print('==> Danh sách sinh viên có điểm TB cao thứ hai: ')
    title = f'{"CMND/CCCD":15}' \
            f'{"Họ và tên":30}{"Địa chỉ":35}' \
            f'{"Ngày sinh":20}{"Mã SV":15}' \
            f'{"Email":30}{"C.Ngành":15}' \
            f'{"Gpa":15}'
    print(title)
    for r in result:
        student = find_student_by_id(students, r[0])
        print(student)
def list_student_most_reg(students):
    result = student_register_many_subject()
    for i in result:
        print(find_student_by_id(students,i[0]))


def list_student_zero_reg(students):
    data = student_zero_register()
    for i in data:
        print(find_student_by_id(students,i[0]))

def find_register_earliest(reg):
    data = find_earliest()
    for i in reg:
        if i.register_id == data[0][0]:
            print(i)
def find_register_latest(reg):
    data = find_latest()
    for i in reg:
        if i.register_id == data[0][0]:
            print(i)
def update_name_by_student_id(students):
    id = input('Nhập mã sinh viên: ')
    try:
        if is_idStudent_valid(id):
            stu = find_student_by_id(students,id)
            if stu is not  None:
                name = input('Nhập tên cần thay đổi: ')
                old = (stu.full_name.first,stu.full_name.mid,stu.full_name.last)
                try:
                    if is_name_valid(name):
                        stu.full_name = name
                        new = (stu.full_name.first,stu.full_name.mid,stu.full_name.last)
                        update_student_name_db(old,new)
                        print('Thành công')
                except NameError as e:
                    print(e)
    except StudentIdError as e:
        print(e)
def update_gpa_by_student_id(students):
    id = input('Nhập mã sinh viên: ')
    try:
        if is_idStudent_valid(id):
            stu = find_student_by_id(students,id)
            if stu is not  None:
                gpa = input('Nhập diem cần thay đổi: ')
                try:
                    if is_grade_valid(gpa):
                        stu.gpa = gpa
                        data = (gpa,id)
                        update_student_gpa_db(data)
                        print('Thành công')
                except GpaError as e:
                    print(e)
    except StudentIdError as e:
        print(e)
def update_student_birth_date(students):
    id = input('Nhập mã sinh viên: ')
    try:
        if is_idStudent_valid(id):
            stu = find_student_by_id(students, id)
            if stu is not None:
                birth = input('Nhập ngày sinh cần thay đổi: ')
                old = (stu.birth.day,stu.birth.month,stu.birth.year)
                try:
                    if is_birth_date_valid(birth):
                        stu.birth = birth
                        new = (stu.birth.day,stu.birth.month,stu.birth.year)
                        update_student_birth_date_db(old,new)

                        print('Thành công')
                except BirthError as e:
                    print(e)
    except StudentIdError as e:
        print(e)
def update_credit_subject(subjects):
    id = input('Nhập mã môn học: ')
    try:
        if is_idSubject_vaild(id):
            sub = find_subject_by_id(subjects, id)
            if sub is not None:
                credit = input('Nhập số tín cần thay đổi: ')
                try:
                    if is_credit_valid(credit):
                        sub.credit = credit
                        update_subject_credit_db(credit,id)
                        print('Thành công')
                except CreditError as e:
                    print(e)
    except SubjectIdError as e:
        print(e)

def update_student_address(students):
    id = input('Nhập mã sinh viên: ')
    try:
        if is_idStudent_valid(id):
            stu = find_student_by_id(students, id)
            if stu is not None:
                address = input('Nhập địa chỉ cần thay đổi: ')
                old = (stu.address.wards,stu.address.district,stu.address.city)
                try:
                    if is_address_valid(address):
                        stu.address = address
                        new = (stu.address.wards,stu.address.district,stu.address.city)
                        update_student_address_db(old,new)

                        print('Thành công')
                except AddressError as e:
                    print(e)
    except StudentIdError as e:
        print(e)
def update_subject_register(register,subjects):
    id = input('Nhập mã sinh viên: ')
    id_subject = input('Nhập mã môn học: ')
    try:
        if is_idStudent_valid(id) and is_idSubject_vaild(id_subject):
            if is_register_exists(register,id,id_subject) is False:
                print('Lỗi sinh viên hoặc mã môn học không tồn tại')
                return
            else:
                new = input('Nhập mã môn học mới: ')
                try:
                    if is_idSubject_vaild(new):
                        sub = find_subject_by_id(subjects,new)
                        if sub is None:
                            print('Lỗi môn học không tồn tại')
                        else:
                            for i in register:
                                if i.subject.subject_id == id_subject and i.student.student_id == id:
                                    i.subject = sub
                            update_subject_register_db(new,id,id_subject)
                            print('Thành công')
                except SubjectIdError as e:
                    print(e)
    except (SubjectIdError,StudentIdError) as e:
        print(e)

def delete_subject(subject,register):
    id = input('Nhập mã môn học: ')
    try:
        if is_idSubject_vaild(id):
            sub = find_subject_by_id(subject,id)
            if sub is not None:
                subject.remove(sub)
                data = (id,)
                delete_subject_db(data)
                for i in register:
                    if i.subject.subject_id == id:
                        register.remove(i)
            else:
                print('MÔN HỌC KHÔNG TỒN TẠI')
    except SubjectIdError as e:
        print(e)
def delete_register(register):
    id = input('Nhập mã sinh viên: ')
    id_subject = input('Nhập mã môn học: ')
    try:
        if is_idStudent_valid(id) and is_idSubject_vaild(id_subject):
            if is_register_exists(register, id, id_subject) is False:
                print('Lỗi sinh viên hoặc mã môn học không tồn tại')
                return
            else:
                for i in register:
                    if i.subject.subject_id == id_subject and i.student.student_id == id:
                        register.remove(i)
                delete_subject_register_db(id_subject,id)
                print('Thành công')

    except (SubjectIdError, StudentIdError) as e:
        print(e)
def delete_student_by_last_name(student,register):
    last_name = input('Nhập họ: ')
    for i in student:
        if i.full_name.last == last_name:
            student.remove(i)
    for i in register:
        if i.student.full_name.last == last_name:
            register.remove(i)
    delete_student_by_last_name_db(last_name)
    print('Thành cong')
