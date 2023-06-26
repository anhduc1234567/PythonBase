import math
import random

stra, strb = input().split()
n = int(stra)
k = int(strb)
print(f"{round(math.sqrt(n), k)}")

print("tinh sin goc x:")
print(f"Sin cua goc {n} la: ", round(math.sin(math.radians(n)), k))

'''round(x) làm tròn đến số nguyên gần nhất'''
print(round(4.3))
print(round(4.7))
''' random sinh số trong đoạn từ [0,n]'''
print(f"Random : {int(n * random.random())}")

'''Tính chu vi diện tích hình tròn '''
r = float(input("Nhap bán kính: "))
print(f"chu vi hình tron la : {round(2 * math.pi * r, 3)}")
print(f"dien tich la : {math.pi * r * r:0.3f}")
str_a, str_b, str_c = input("Nhap 3 canh cua tam giac :").split()
a1 = int(str_a)
b1 = int(str_b)
c1 = int(str_c)
p = (a1 + b1 + c1) / 2
print(f"Dien tích tam giac la: {math.sqrt(p * (p - a1) * (p - b1) * (p - c1)):0.2f}")
