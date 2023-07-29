import urllib.request
url = 'https://braniumacademy.net/courses/python3/lessons/bai-8-6-truy-cap-internet/'
# opener = urllib.request.build_opener()
# opener.addheaders = [('User-Agent'),'']
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen(url)
# data = response.read()
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', '')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
data = response.read()
data_string = str(data, encoding='UTF-8')
print(data_string)