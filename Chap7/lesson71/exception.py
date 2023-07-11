
# BaseException	Lớp cha của mọi ngoại lệ có sẵn trong Python
# Exception	Lớp cha của mọi ngoại lệ có sẵn, không thuộc hệ thống có sẵn và ngoại lệ người dùng tự định nghĩa
# ArithmeticError	Lớp cha của các ngoại lệ toán học như OverflowError, ZeroDivisionError, FloatingPointError
# BufferError	Được kích hoạt khi một hành động liên quan bộ đệm không thể thực hiện
# LookupError	Lớp cha của các ngoại lệ liên quan đến khóa hoặc chỉ số trong bản đồ, tập hợp: IndexError, KeyError
# ImportError	Được kích hoạt khi lệnh import có vấn đề vì cố tải một modul nào đó
# IndexError	Được kích hoạt khi chỉ số ngoài biên list, tuple
# KeyError	Được kích hoạt khi ánh xạ key không tồn tại trong dict
# KeyboardInterrupt	Được kích hoạt khi người dùng nhấn tổ hợp phím ngắt như Ctrl C hoặc Delete
# NameError	Kích hoạt khi một định danh cần sử dụng không tồn tại
# OverflowError	Kích hoạt khi kết quả một phép toán quá lớn để thể hiện ra
# RecursionError	Kích hoạt khi trình biên dịch phát hiện số lần đệ quy vượt quá số lần tối đa cho phép
# SyntaxError	Kích hoạt khi trình phân tích cú pháp phát hiện lỗi cú pháp
# TabError	Kích hoạt khi căn lệ chứa các kí tự tab, khoảng trắng không nhất quán.
# TypeError	Kích hoạt khi một thao tác áp dụng cho đối tượng không phù hợp về kiểu.
# UnicodeError	Kích hoạt khi bộ mã hóa hoặc giải mã Unicode gặp lỗi
# ValueError	Kích hoạt khi một hành động hoặc hàm nhận đối số đúng kiểu nhưng giá trị không phù hợp.
# ZeroDivisionError	Kích hoạt khi đối số thứ 2 của phép chia hoặc phép chia dư là số 0
# Warning	Lớp cha của các cảnh báo

list = ['a','b','c','d']
try:
    print(list[5])
except IndexError:
    print("Lỗi vuot qua index")
dic = {'01':'anh','02':'duc','03':'long'}

try:
    print(dic['011'])
except KeyError:
    print("KEY KHONG TON TAI")
set = {'anh','duc','long'}
