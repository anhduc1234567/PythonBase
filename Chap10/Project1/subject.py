class Subject:
    AUTO_ID = 1000
    def __init__(self,subject_id,name,credit):
        if subject_id is None:
            self.__subject_id = subject_id
        else:
            self.__subject_id = Subject.AUTO_ID
            Subject.AUTO_ID +=1
        self.__name = name
        self.__credit = credit
    @property
    def subject_id(self):
        return self.__subject_id
    @subject_id.setter
    def subject_id(self,value):
        self.__subject_id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def credit(self):
        return self.__credit
    @credit.setter
    def credit(self,value):
        self.__credit = value