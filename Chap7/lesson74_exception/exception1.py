class StudentIdError(Exception):
    def __init__(self,id, message):
        super().__init__(message)
        self.id = id
        self.message = message
    def __str__(self):
        return f'StudentIdError: {self.message} {self.id}'
class FullNameError(Exception):
    def __init__(self,name,message):
        super().__init__(message)
        self.name = name
        self.mess = message
    def __str__(self):
        return f'FullNameError: {self.mess} {self.name}'
class AgeError(Exception):
    def __init__(self,age,mess):
        super().__init__(mess)
        self.age = age
        self.mess = mess
    def __str__(self):
        return f'AgeError: {self.mess} {self.age}'
class GradeError(Exception):
    def __init__(self,grade,massage=''):
        super().__init__(massage)
        self.grade = grade
        self.massage = massage
    def __str__(self):
        return f'GradeError: {self.massage}: {self.grade}'