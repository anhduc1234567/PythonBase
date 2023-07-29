import urllib.request
import json
class FullName:
    def __init__(self,wards,district,city):
        self.first = wards
        self.mid= district
        self.last = city
    def __str__(self):
        return f'{self.first:6} {self.mid:6} {self.last:8}'

class Address:
    def __init__(self,wards,district,city):
        self.wards = wards
        self.district = district
        self.city = city
    def __str__(self):
        return f'{self.wards:6} {self.district:6} {self.city:8}'

class Student:
    def __init__(self,id,name,address,gpa,major,age):
        self.id = id
        self.name = name
        self.address = address
        self.major = major
        self.gpa = gpa
        self.age = age
    def __str__(self):
        return f'{self.id:10} {self.name} {self.age} {self.address}'\
                f'{self.gpa:10} {self.major}'

def decode_full_name(dic):
    if 'first' in dic:
        return FullName(dic['first'],dic['mid'],dic['last'])
    else:
        return None
def decode_address(dic):
    if 'wards' in dic:
        return FullName(dic['wards'],dic['district'],dic['city'])
    else:
        return None
def decode_student(dic):
    if 'id' in dic:
        id = dic['id']
        full_name = decode_full_name(dic['full_name'])
        age = dic['age']
        major = dic['major']
        gpa = dic['gpa']

        address = decode_address(dic['address'])
        return Student(id,full_name,address,gpa,major,age)
    else:
        return dic
def read_json():
    with open('input3.json','r+',encoding='UTF-8') as inp:
        data = inp.read()
        stundets = json.loads(data,object_hook=decode_student)
        return stundets

def print_arr(arr):
    for i in arr:
        print(i)

def connect_internet():
    url = 'https://braniumacademy.net/resources/lesson95_data3.json'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    data = response.read()
    data_string = str(data, encoding='UTF-8')
    data_string = data_string.replace('\n','')
    with open('input3.json','w+',encoding='UTF-8') as inp:
        inp.write(data_string)

connect_internet()
students = read_json()
print_arr(students)