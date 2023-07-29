import re
# []	Một tập các kí tự
# \	Dấu hiệu chỉ ra đây là một chuỗi các kí tự đặc biệt
# .	Bất kì kí tự nào
# ^	Bắt đầu với
# $	Kết thúc với
# *	Xuất hiện 0 hoặc nhiều
# +	Xuất hiện 1 hoặc nhiều
# ?	Xuất hiện 0 hoặc 1 lần
# {}	Chính xác số lần xuất hiện trong cặp ngoặc này
# |	Hoặc
# ()	Gom nhóm

# Kí tự	Mô tả
# \A	So khớp ở đầu chuỗi kí tự
# \b	So khớp tại vị trí đầu hoặc cuối từ
# \B	So khớp tại vị trí khác đầu, cuối từ
# \d	So khớp giá trị số (0-9)
# \D	So khớp chuỗi kí tự không chứa kí tự số
# \s	So khớp kí tự khoảng trắng
# \S	So khớp kí tự  không phải khoảng trắng
# \w	So khớp bất kì chữ cái, chữ số hoặc dấu gạch dưới
# \W	Ngược lại của \w
# \Z	So khớp tại vị trí cuối chuỗi

# [abc]	Khớp với bất kì kí tự nào trong số các kí tự a, b hoặc c
# [a-z]	Khớp với bất kì kí tự nào từ a tới z
# [^abc]	Khớp với bất kì kí tự nào ngoại trừ a, b, c
# [0-9]	Khớp với bất kì kí tự nào từ 0 đến 9
# [0-5][0-9]	Khớp với bất kì cụm 2 kí tự số từ 00 đến 59
# [a-z][A-Z]	Khớp với bất kì kí tự nào là chữ cái hoa hoặc thường a-z
# [+]	Khớp với bất kì dấu + nào trong chuỗi kí tự
# [0-9]{3}	Khớp với bất kì số có 3 chữ số nào
# [a-b]{3,5}	Khớp bất kì chuỗi gồm các kí tự a hoặc b có 3-5 kí tự

'''Tách chuỗi '''
# string = input('Nhập vào 1 chuỗi: ')
# pattern = r'[\s\t,./?]+'
# words = re.split(pattern,string)
# print(words)
'''So khớp'''
string = input('Nhập vào chuỗi có định dạng ss:mm:hh : ')
pattern = r'^(\d{2})/\d{2}/\d{4}$'
pattern2 = r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}'
pattern3 = r'^(1[0-9]|0[0-9]|2[0-4]):([0-5][0-9]):([0-5][0-9])$'
if re.match(pattern2,string):
    print('THỎA MÃN')
else:
    print('KHÔNG ĐÚNG')