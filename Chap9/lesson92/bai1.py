from datetime import date,datetime
import re

pattern = r'^\d{2}/\d{2}/\d{4}$'
str = input('Nhập ngày sinh: ')
if re.match(pattern,str):
    format = '%d/%m/%Y'
    birth = datetime.strptime(str,format)
    birth_date = birth.date()
    print(birth_date)
else:
    print('khong hop lệ')
