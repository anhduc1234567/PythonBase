import urllib.request
import xml.etree.ElementTree as et

class Plant:
    def __init__(self,commom,botanical,zone,light,price,availability):
        self.common = commom
        self.botanical = botanical
        self.zone = zone
        self.light = light
        self.price = price
        self.avai = availability

    def __str__(self):
        return f'{self.common:25} {self.botanical:35} {self.zone:15} {self.light:30} {self.price:10} {self.avai}'

def read_xml():
    parse = et.parse('input3.xml')
    root = parse.getroot()
    plants = []
    for i in root:
        common = i[0].text
        bont = i[1].text
        zone = i[2].text
        light = i[3].text
        price = i[4].text
        avai = i[5].text
        plants.append(Plant(common,bont,zone,light,price,avai))
    return plants

def print_arr(arr):
    for i in arr:
        print(i)
def connect_internet():
    url = 'https://braniumacademy.net/resources/plant_catalog.xml'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', '')]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(url)
    data = response.read()
    data_string = str(data, encoding='UTF-8')
    data_string = data_string.replace('\n','')
    with open('input3.xml','w+',encoding='UTF-8') as inp:
        inp.write(data_string)

connect_internet()
plants = read_xml()
print_arr(plants)