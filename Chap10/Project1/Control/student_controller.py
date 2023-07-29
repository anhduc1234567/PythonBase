import re
from Chap10.Project1.exception import *
from Chap10.Project1.Model.student import Student
class StudentController:
    def is_name_vaild(self,name):
        if len(name) < 2 or len(name) > 50:
            raise NameError(name, 'Tên không được quá dài hoặc ngắn')
        for i in name.lower():
            if i.isalpha() is False and i != ' ':
                raise NameError(name, 'Tên không hợp lệ')
        return True
    def is_birth_vaild(self,birth):
        patter = r'^(0[1-9]|[1-2][1-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4})$'
        if re.match(patter,birth) is True:
            return True
        else:
            raise BirthError(birth,'Ngày sinh không hợp lệ')
    def is_gpa_vaild(self,gpa):
        patter = r'^[1-9].\d{2}$'
        mat = re.match(patter,gpa)
        if mat is True:
            if 0 <= float(gpa) <= 4:
                return True
            else:
                raise GpaError(gpa,'Điểm không hợp lệ')
        else:
            raise
    def is_email_vaild(self,email):
        pattern = '^[a-z_]+[a-z]+[0-9._-]*@[a-z0-9]+.[a-z]{2,4}$'
        matcher = re.search(pattern, email, flags=re.IGNORECASE)
        if matcher:
            return True
        else:
            raise EmailError(email,'Email không hợp lệ')


    def add(self,person_id,name,birth,email,gpa,major):
        try:
            self.is_name_vaild(name)
            self.is_email_vaild(email)
            self.is_gpa_vaild(gpa)
            self.is_birth_vaild(birth)
            return Student(person_id,name,birth,None,email,gpa,major)
        except (NameError,BirthError,EmailError,GpaError) as e:
            print(e)

if __name__ == '__main__':
    s =StudentController()
    s.add(1234567,'Nguye duc anh','12/10/2004','ajninin@gmail.com','7.89','cntt')


