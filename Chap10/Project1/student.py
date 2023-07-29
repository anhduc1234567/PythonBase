from datetime import date
class FullName:
    def __init__(self,first,mid,last):
        self.__first = first
        self.__mid = mid
        self.__last = last
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

class Person:
    def __init__(self,id,name,birth):
        self.__id = id
        self.__name = self.setName(name)
        fomat = '%d/%m/%Y'
        self.__birth = self.setBirth(birth)

    def setBirth(self,birth):
        b = birth.strip().split('/')
        return date(int(b[2]),int(b[1]),int(b[0]))
    def setName(self,name:str):
        words = name.strip().split()
        first = words[0]
        last = words[len(words) - 1]
        mid = ''
        for i in range(1,len(words)- 1):
            mid += words[i] + ' '
        return FullName(first,mid,last)


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        self.__birth = value



class Student(Person):
    AUTO_ID = 1000
    def __init__(self,person_id,name,birth,student_id,email,gpa,major):

        super().__init__(person_id,name,birth)

        if student_id is None:
            self.__student_id = f'SV{Student.AUTO_ID}'
            Student.AUTO_ID += 1
        else:
            self.__student_id = student_id
        self.__email = email
        self.__gpa = gpa
        self.__major = major


    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

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
    def gpa(self, value):
        self.__gpa = value

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        self.__major = value

    def __str__(self):
        return f'Student {self.student_id} {self.email}'