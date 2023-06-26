import math
def add(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    return a / b
def mu(a, b):
    return a ** b
def lay_nguyen(a, b):
    return a // b
def UCLN(a,b):
    c = 0
    if a > b:
        c = b
    else:
        c = a
    for i in range(c,0,-1):
        if a % i == 0 and b % i == 0:
            return i
def BCNN(a , b):
    c = 0
    if a > b:
        c = a
    else:
        c = b
    while True:
       if c % a == 0 and c % b == 0:
           return c
       else:
           c += 1
def checkSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2,n,1):
        if n % i == 0:
            return False
    return True
def chechSoChinhPhuong(n):
    k = int(math.sqrt(n))
    p = float(math.sqrt(n))
    #print(f"{k} và {p} ", k - p)
    if k - p == 0:
        return True
    else :
        return False
def timSoNguyenToNext(n):
    n = n + 1
    while True:
        if checkSoNguyenTo(n) == True:
            return n
        n += 1
def phanTichThuaSo(n):
    i = 2
    c = 0
    while n != 1:
        if n % i == 0:
            c += 1
            n = n // i
        else:
            if c > 0:
                print(i, end=" ")
                if c > 1:
                    print("^",c, end="")
                if i != n // i:
                    print("x",end="")
            i += 1
            c = 0

    print(i, end="")
    if c > 1:
        print("^",c)

def chager(a):
    a = a ** 2


stra,strb = input().split()
a = int(stra)
b = int(strb)
print(f"Tong {a} va {b} la", add(a,b))
print(f"Tic {a} và {b} la ", nhan(a,b))
print(f"UCLN của {a} và {b} la ", UCLN(a,b))
print(f"BCNN CỦA {a} VA {b} la ", BCNN(a,b))
print(f"Các số nguyên tố có trong đoạn {a} và {b} là ",end="")
for i in range(a,b+1,1):
    if checkSoNguyenTo(i) == True:
        print(i, end=" ")
print()
print(f"Các số chính phương  có trong đoạn {a} và {b} là ",end="")
for i in range(a,b+1,1):
    if chechSoChinhPhuong(i) == True:
        print(i, end=" ")
print(f"Số nguyen to tiep theo cua {a} la: ", timSoNguyenToNext(a))
print(f"Phan tich thua so nguyen to cua {b} la: ",end="")
phanTichThuaSo(b)
