class NameError(Exception):
    def __init__(self,main,message = ' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'NameError: {self.message} {self.main}'


class StudentIdError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message
    def __str__(self):
        return f'StudentIdError: {self.message} {self.main}'


class SubjectIdError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'SubjectIdError: {self.message} {self.main}'


class TeacherIdError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'TeacherIdError: {self.message} {self.main}'


class CourseIdError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'CourseIdError: {self.message} {self.main}'


class TranscriptIdError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'TranscriptIdError: {self.message} {self.main}'


class GpaError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'GpaError: {self.message} {self.main}'


class CreditError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'CreditError: {self.message} {self.main}'


class BirthError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'BirthError: {self.message} {self.main}'

class SalaryError(Exception):
    def __init__(self, salary, message=''):
        super().__init__(message)
        self.__salary = salary
        self.__message = message

    def __str__(self):
        return f'SalaryError: {self.__message} : {self.__salary}'