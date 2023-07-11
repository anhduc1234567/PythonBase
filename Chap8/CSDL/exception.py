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

class RegisterIdError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'RegisterIdError: {self.message} {self.main}'

class NameSubjectError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'NameSubjectError: {self.message} {self.main}'

class AddressError(Exception):
    def __init__(self, main, message=' '):
        super().__init__(message)
        self.main = main
        self.message = message

    def __str__(self):
        return f'AddressError: {self.message} {self.main}'