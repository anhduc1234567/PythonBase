import urllib.request
from collections import OrderedDict
from operator import itemgetter
import xml.etree.ElementTree as et
import json
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} {self.age}'
def write_json(str):
    with open('input1.json','w+',encoding='UTF-8') as inp:
        inp.write(str)
def decode_person(dic):
    if 'name' in dic:
        name = dic['name']
        age = dic['age']
        return Person(name,age)
    else:
        return dic

def print_arr(arr):
    for i in arr:
        print(i)

def read_json():
    with open('input1.json','r+',encoding='UTF-8') as inp:
        data = inp.read()
        people = json.loads(data,object_hook=decode_person)
        return people


def list_by_age(arr):
    dic = {}
    for i in arr:
        if i.age in dic:
            dic[i.age] += 1
        else:
            dic[i.age] = 1
    dic = OrderedDict(sorted(dic.items(), key=itemgetter(1)))
    for i in dic.keys():
        print(f'{i}  {dic[i]}')


url = 'https://braniumacademy.net/resources/lesson95_data1.json'
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', '')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
data = response.read()
str = str(data,'UTF-8')
str = str.replace('\n','')
write_json(str)

people = read_json()
print_arr(people)
list_by_age(people)