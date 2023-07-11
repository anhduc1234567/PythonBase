from datetime import datetime

from filter import *
from exception import *
class FullName:
    def __init__(self,f_id = 0,first = '', mid = '',last = ''):
        self.f_id = f_id
        self.__first = first
        self.__mid = mid
        self.__last = last
    @property
    def f_id(self):
        return self.__f_id
    @f_id.setter
    def f_id(self,value):
        self.__f_id = value

    @property
    def first(self):
        return self.__first
    @first.setter
    def first(self,value):
        self.__first = value

    @property
    def mid(self):
        return self.__mid
    @mid.setter
    def mid(self,value):
        self.__mid = value

    @property
    def last(self):
        return self.__last
    @last.setter
    def last(self,value):
        self.__last = value
    def __str__(self):
        return f'{self.last:5} {self.mid:5} {self.first:10}'
class Address:
    def __init__(self, add_id = 0, wards = '', district='',
                 city = ''):
        self.__add_id = add_id
        self.__wards = wards
        self.__district = district
        self.__city = city

    @property
    def add_id(self):
        return self.__add_id

    @add_id.setter
    def add_id(self, value):
        self.__add_id = value

    @property
    def wards(self):
        return self.__wards

    @wards.setter
    def wards(self, value):
        self.__wards = value

    @property
    def district(self):
        return self.__district

    @property
    def city(self):
        return self.__city

    @district.setter
    def district(self, value):
        self.__district = value

    @city.setter
    def city(self, value):
        self.__city = value

    def __str__(self):
        return f'{self.wards:5}-{self.district:5}-{self.city}'

class BirthDate:
    def __init__(self, bd_id=0, day=0, month=0, year=0):
        self.birth_date_id = bd_id
        self.day = day
        self.month = month
        self.year = year

    @property
    def birth_date_id(self):
        return self.__birth_date_id

    @birth_date_id.setter
    def birth_date_id(self, value):
        self.__birth_date_id = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'

class Person:
    def __init__(self,idp = '',full_name =None,birth = None
                 ,address = None):
        self.idp = idp
        self.full_name = full_name
        self.birth = birth
        self.address = address
    @property
    def idp(self):
        return self.__idp
    @idp.setter
    def idp(self,value):
        try:
            if is_person_id_valid(value):
                self.__idp = value
            else:
                raise ValueError('Số CCCD Không hợp lệ')
        except ValueError as e:
            print(e)
            self.__idp = '00000000000000'
    @property
    def full_name(self):
        return self.__full_name
    @full_name.setter
    def full_name(self,value):
        try:
            if isinstance(value,str) and is_name_valid(value):
                names = value.split(' ')
                mid = ''
                for i in range(1,len(names) - 1):
                    mid += names[i] + ' '
                self.__full_name = FullName(first=names[len(names) -1],last=names[0],mid=mid)
            elif isinstance(value, FullName):
                self.__full_name = value
        except NameError as e:
            print(e)
            self.__full_name = 'No name'

    @property
    def birth(self):
        return self.__birth_date
    @birth.setter
    def birth(self,value):
        if isinstance(value, BirthDate):
            self.__birth_date = value
        else:
            try:
                if isinstance(value, str) and is_birth_date_valid(value):
                    data = value.split('/')
                    self.__birth_date = BirthDate(day=int(data[0]), month=int(data[1]), year=int(data[2]))
            except BirthError as e:
                print(e)
                self.__birth_date = BirthDate(0, 1, 1, 2020)

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        if isinstance(value,Address):
            self.__address = value
        else:
            try:
                if is_address_valid(value):
                    data = value.split('-')
                    if len(data) == 1:
                        self.__address = Address(city=data[0])
                    elif len(data) == 2:
                        self.__address = Address(district=data[0], city=data[1])
                    else:
                        self.__address = Address(wards=data[0], district=data[1], city=data[2])
            except AddressError as e:
                print(e)
    def __str__(self):
        return f'CCCD:{self.idp:10}   {self.full_name}  '\
            f'{self.birth}  {self.address} '

class Student(Person):

    AUTO_ID = 1000
    def __init__(self,id_stu = None,email = '',gpa = '',major = ''
                ,idp = '',name = None,birth = None,
                address = None):
        super().__init__(idp,name,birth,address)
        self.student_id = id_stu
        self.email = email
        self.gpa = gpa
        self.major = major

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self,value):
        if value is None:
            self.__student_id = f'SV{Student.AUTO_ID}'
            Student.AUTO_ID += 1
        else:
            try:
                if is_idStudent_valid(value):
                    self.__student_id = value
            except StudentIdError as e:
                print(e)
                self.__student_id = None
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self,value):
        try:
            if is_grade_valid(value):
                self.__gpa = value
        except GpaError as e:
            print(e)
            self.__gpa = 0.0

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    def __str__(self):
        return f'Student: MSV:{self.student_id} {self.major:8}'\
            f'{self.email:25} {self.gpa} {super().__str__()}'
class Register:
    """Lớp mô tả lớp đăng ký"""
    AUTO_ID = 100

    def __init__(self, cid=None, rtime=None, student=None, subject=None):
        self.register_id = cid
        self.register_time = rtime
        self.student = student
        self.subject = subject

    @property
    def register_id(self):
        return self.__register_id

    @register_id.setter
    def register_id(self, value):
        if value is None:
            self.__register_id = Register.AUTO_ID
            Register.AUTO_ID += 1
        else:
            try:
                if is_idRegister_valid(f'{value}'):
                    self.__register_id = value
            except RegisterIdError as e:
                print(e)
                self.__register_id = 0

    @property
    def register_time(self):
        return self.__register_time

    @register_time.setter
    def register_time(self, value):
        if value is not None:
            if isinstance(value, str):  # nếu là string thì ta chuyển sang datetime
                self.__register_time = datetime.strptime(value, '%d/%m/%Y %H:%M:%S')
            if isinstance(value, datetime):  # nếu sẵn là datetime ta chỉ cần gán thẳng
                self.__register_time = value
        else:
            self.__register_time = datetime.now()  # về date time bạn xem chương 9 nhé

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    def __str__(self):
        return f'{self.register_id:<10}{self.student.student_id:15}' \
               f'{self.student.full_name.__str__():35}{self.subject.subject_id:<15}' \
               f'{self.subject.subject_name:35}' \
               f'{self.register_time.strftime("%d/%m/%Y %H:%M:%S"):30}'

class Subject:
    """Lớp mô tả thông tin môn học"""
    AUTO_ID = 1000

    def __init__(self, sid=None, name='', credit=''):
        self.subject_id = sid
        self.subject_name = name
        self.credit = credit

    @property
    def subject_id(self):
        return self.__subject_id
    @subject_id.setter
    def subject_id(self,value):
        if value is None:
            self.__subject_id = f'{Subject.AUTO_ID}'
            Subject.AUTO_ID += 1
        else:
            try:
                if is_idSubject_vaild(value):
                    self.__subject_id = value
            except SubjectIdError as e:
                print(e)
                self.__subject_id = 0
    @property
    def subject_name(self):
        return self.__subject_name
    @subject_name.setter
    def subject_name(self,value):
        try:
            if is_name_subject_valid(value):
                self.__subject_name = value
        except NameSubjectError as e:
            print(e)
            self.__subject_name = 'No name'

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, value):
        try:
            if is_credit_valid(f'{value}'):
                self.__credit = int(value)
        except CreditError as e:
            self.__credit = 0
            print(e)

    def __str__(self):
        return f'{self.subject_id:10} {self.subject_name:30} {self.credit}'

