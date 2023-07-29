import urllib.request
import xml.etree.ElementTree as et

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



def read_xml():
    parse = et.parse('input7.xml')
    root = parse.getroot()
    students = []
    for i in root:
        id = i[0].text
        age = i[1].text
        major = i[2].text
        gpa = i[3].text
        first = i[4][0].text
        mid = i[4][1].text
        last = i[4][2].text
        full_name = FullName(first,mid,last)
        wards = i[5][0].text
        district = i[5][1].text
        city = i[5][2].text
        address = Address(wards,district,city)
        students.append(Student(id,full_name,address,gpa,major,age))
    return students

def print_arr(arr):
    for i in arr:
        print(i)
def connect_internet():
    url = 'https://braniumacademy.net/resources/student.xml'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    data = response.read()
    data_string = str(data, encoding='UTF-8')
    data_string = data_string.replace('\n','')
    with open('input7.xml','w+',encoding='UTF-8') as inp:
        inp.write(data_string)
def write_xml(students):
    root = et.Element('students')
    for i in students:
        student = et.SubElement(root,'student')
        et.SubElement(student,'id').text = i.id
        et.SubElement(student,'age').text = i.age
        et.SubElement(student,'major').text = i.major
        et.SubElement(student,'gpa').text = i.gpa
        full_name = et.SubElement(student,'full_name')
        et.SubElement(full_name,'first').text = i.name.first
        et.SubElement(full_name, 'mid').text = i.name.mid
        et.SubElement(full_name, 'last').text = i.name.last
        address = et.SubElement(student, 'address')
        et.SubElement(address, 'wards').text = i.address.wards
        et.SubElement(address, 'district').text = i.address.district
        et.SubElement(address, 'city').text = i.address.city
    et.indent(root, space='\t')
    string = str(et.tostring(root,encoding='UTF-8',xml_declaration=True),'UTF-8')
    with open('output7.xml','w+',encoding='UTF-8') as out:
        out.write(string)

connect_internet()
students = read_xml()
print_arr(students)
write_xml(students)