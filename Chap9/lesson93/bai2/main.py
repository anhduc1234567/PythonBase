import urllib.request
import json

class Birth:
    def __init__(self,day,month,year):
        self.d = day
        self.m = month
        self.y = year
    def __str__(self):
        return f'{self.d:6} {self.m:6} {self.y:8}'

class Student:
    def __init__(self,id,name,birth,gpa):
        self.id = id
        self.name = name
        self.birth = birth
        self.gpa = gpa
    def __str__(self):
        return f'{self.id:10} {self.name:25} {self.birth} {self.gpa:10}'

def decode_birth(dic):
    if 'day' in dic:
        day = dic['day']
        month = dic['month']
        year = dic['year']
        return Birth(day,month,year)
    else:
        return None
def decode_student(dic):
    if 'id' in dic:
        id = dic['id']
        name = dic['name']
        birth = decode_birth(dic['birth_date'])
        gpa = dic['gpa']
        return Student(id,name,birth,gpa)
    else:
        return dic
def read_json():
    with open('input2.json','r+',encoding='UTF-8') as inp:
        data = inp.read()
        students = json.loads(data,object_hook=decode_student)
        return students

def print_arr(arr):
    for i in arr:
        print(i)
def connect_internet():
    url = 'https://braniumacademy.net/resources/lesson95_data2.json'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    data = response.read()
    data_string = str(data, encoding='UTF-8')
    data_string = data_string.replace('\n','')
    with open('input2.json','w+',encoding='UTF-8') as inp:
        inp.write(data_string)

connect_internet()
students = read_json()
students.sort(key= lambda x:(x.birth.d,x.birth.m))
print_arr(students)