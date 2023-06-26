
# str = "nguyen duc anh duc anh anh duc"
# numbic = "1234556"
# print(str)
# print(str.strip()) # xóa khoảng trắng 2 đầu
# print(str.count("duc")) #đếm số lần xuất hiện
# print(str.endswith(" ",0,11))
# print(str.index("duc",8))
# print(str.isascii())
# print(str.replace("duc","DUCcc"))
# print(numbic.isnumeric())
'''capitalize()	Trả về bản sao của chuỗi gốc đã được viết hoa chữ cái đầu. Các chữ cái khác viết thường hoàn toàn.
count(sub[, start[, end]])	Trả về số lần xuất hiện của chuỗi con sub trong chuỗi mẹ trong đoạn tùy chọn từ start tới trước end.
endwith(sufix[, start[, end]])	Kiểm tra xem chuỗi kết thúc với suffix trong đoạn tùy chọn từ start đến trước end hay không. Nếu có, return True, ngược lại return False.
find(sub[, start[, end]])	Trả về vị trí xuất hiện đầu tiên của chuỗi con sub trong chuỗi mẹ. Tùy chọn vùng tìm kiếm trong lát cắt [start : end]. Trả về -1 nếu không tìm thấy.
format(*args, **kwargs)	    Thực hiện định dạng chuỗi kí tự.
index(sub[, start[, end]])	Tìm vị trí xuất hiện đầu tiên của chuỗi con sub trong chuỗi hiện tại. Tùy chọn vùng tìm kiếm trong lát cắt [start : end]. Văng ngoại lệ ValueError khi không tìm thấy kết quả.
isalpha()	    Trả về True nếu tất cả mọi kí tự trong chuỗi hiện tại đều là các chữ cái. Độ dài tối thiểu của chuỗi là 1 kí tự. Ngược lại, trả về False.
isalphanum()	Trả về True nếu tất cả các kí tự trong chuỗi kí tự là chữ cái hoặc chữ số. Độ dài chuỗi tối thiểu là 1 kí tự. Ngược lại trả về False. Một kí tự c nào đó thỏa mãn là alphanum nếu nó thỏa mãn một trong các hàm sau: isalpha(), isdecimal(), isdigit(), isnumeric().
isascii()	Trả về True nếu chuỗi kí tự rỗng hoặc tất cả các kí tự trong đó là ASCII, False trong trường hợp ngược lại. Giá trị kí tự ASCII có mã code point trong khoảng U+0000 đến U+007F.
isdecimal()	Trả về True nếu tất cả các kí tự trong chuỗi dài tối đa 1 kí tự là các chữ số hệ thập phân. Trả về False trong trường hợp ngược lại.
isdigit()	Trả về True nếu tất cả các kí tự trong chuỗi dài tối đa 1 kí tự là các chữ số. Trả về False trong trường hợp ngược lại.
isidentifier()	Kiểm tra xem một string có phải định danh hợp lệ không. Trả về True nếu là định danh hợp lệ và False trong trường hợp ngược lại.
islower()	Kiểm tra xem các kí tự trong chuỗi có phải tất cả là chữ thường hay không.
isnumeric()	Kiểm tra xem tất cả các kí tự trong chuỗi có phải số không. Độ dài chuỗi tối thiểu là 1 kí tự.
isspace()	Trả về True nếu chỉ có kí tự khoảng trắng trong chuỗi kí tự hiện tại. Độ dài chuỗi phải tối thiểu là 1 kí tự. Ngược lại trả về False.
isupper()	Trả về True nếu tất cả kí tự trong chuỗi dài tối thiểu 1 kí tự đều là kí tự chữ cái hoa. Ngược lại trả về False.
lower()	Trả về bản sao của chuỗi hiện tại trong đó tất cả kí tự đã được viết thường.
lstrip([chars])	Trả về bản sao của chuỗi hiện tại với các kí tự đầu đã bị lược bỏ. Tham số chars xác định tập các kí tự cần loại bỏ. Nếu khuyết tham số hoặc tham số là None, hàm này mặc định loại bỏ kí tự khoảng trắng.
partition(sep)	Tách chuỗi tại vị trí xuất hiện đầu tiên của sep. Trả về 3 tuple chứa đoạn trước, giá trị sep và đoạn sau giá trị sep. Nếu giá trị sep không tồn tại trong chuỗi. Trả về 3 tuple chứa chuỗi gốc và 2 chuỗi rỗng.
removeprefix(prefix, /)	Nếu chuỗi string bắt đầu với giá trị trong tham số prefix, trả về chuỗi con trong lát cắt string[len(prefix): ]. Ngược lại trả về bản sao của chuỗi gốc.
removesuffix(suffix, /)	Nếu chuỗi string kết thúc bởi giá trị trong suffix và suffix không rỗng, trả về giá trị string[:-len(suffix)]. Ngược lại trả về bản sao của chuỗi gốc.
replace(old, new[, count])	Trả về bản sao của chuỗi sau khi thay thế toàn bộ các giá trị old bởi giá trị trong new. Nếu tham số tùy chọn count được chỉ định, chỉ count giá trị old xuất hiện đầu tiên trong chuỗi được thay thế.
rfind(sub[, start[, end]])	Trả về vị trí xuất hiện cuối cùng của chuỗi con sub trong chuỗi hiện tại. Nếu không tìm thấy, trả về -1.
rindex(sub[, start[, end]])	Tương tự rfind() nhưng văng ngoại lệ khi sub không tồn tại trong chuỗi hiện tại.
split(sep=none, maxsplit=-1)	Trả về danh sách các từ có trong string, sử dụng sep làm dấu hiệu phân tách. Nếu maxsplit được chỉ định, tối đa maxsplit từ được tách ra. Nếu sep không được chỉ định giá trị cụ thể, chương trình sẽ tách chuỗi tại vị trí có dấu cách, loại bỏ hết dấu cách ở đầu và cuối chuỗi.
splitline([keepends])	Trả về một list các dòng trong chuỗi, phân tách tại vị trí các kí tự ngắt dòng như \n, \r, \r\n, \v  hoặc \x0b, \f hoặc \x0c, \x1c, \x1d, \s1e, \x85, \u2028, \u2029.
startwith(prefix[, start[, end]])	Trả về True nếu string bắt đầu với prefix, mặt khác trả về False. Nếu start, end được chỉ định, hàm sẽ bắt đầu kiểm tra tại vị trí start và kết thúc tại end.
strip([chars])	Trả về bản sao của string sau khi loại bỏ các dấu cách ở đầu và cuối chuỗi string.
swapcase()	Trả về chuỗi sau khi hoán đổi kí tự hoa thành kí tự thường và ngược lại.
title()	Trả về chuỗi với kí tự đầu mỗi từ viết hoa các kí tự còn lại viết thường.
upper()	Trả về một bản sao của string trong đó tất cả các kí tự được viết hoa hoàn toàn.
zfill(width)	Trả về bản sao của chuỗi hiện tại trong đó điền số 0 vào bên trái để tạo chuỗi với độ dài width. 
Nếu width <= len(string) thì chuỗi gốc sẽ được trả về.
'''
import re

'''Viết hoa chữ cái đầu'''
# str = input("Nhap chuoi ")
# print(str.title())
'''Đêm nguyên âm phụ âm'''
def countNguyenam(str):
    str2 = str.lower()
    c = 0
    for i in str2:
        if i == "u" or i == "e" or i == "o" or i == "i" or i == "a":
            c += 1
    return c
# str = input()
# print(countNguyenam(str))
# print(len(str.split()))
'''Tìm soos ần xuat hien của chuoi con'''
# str1 = input()
# str2 = input()
# print(str1.count(str2))
'''Hiển thị các từ xuat hien 1 lần'''
def isExist(str,arr,end):
    for i in range(0,end):
        if arr[i] == str:
            return True
    return False

# str = input()
# word = str.split()
# for i in range(0,len(word)):
#     if isExist(word[i],word,i) == False:
#         print(f"{word[i]} ", end="")
# for i in word:
#     print(f"{i} - {word.count(i)}")
'''Đếm số lần xuất hiện các chữ cái'''
# str = input()
# for i in range(0,len(str)):
#     if str[i].isalpha() and isExist(str[i],str,i) == False:
#          print(f"{str[i]} : {str.count(str[i])}, ", end="")
''' Xu lu sâu'''
import re
def add_space(data: str):
    """This function add space after punctuations"""
    data = data.replace(".", ". ")
    data = data.replace(",", ", ")
    data = data.replace(":", ": ")
    data = data.replace(";", "; ")
    data = data.replace("!", "! ")
    data = data.replace("?", "? ")
    return data
str = input()
str = str.strip();
str = str.title()
str = add_space(str)
str = re.sub("\\s+", " ", str)
print(str)