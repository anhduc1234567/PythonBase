import math
def finMax(num):
    max = num[0]
    for i in num:
        if i >= max:
            max = i
    return max
def findMax2(num):
    max2 = 0
    max = finMax(num)
    for i in num:
        if i != max :
            max2 = i
        break
    for i in num:
        if i > max2 and i != max:
            max2 = i
    return max2
def checkSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2,n,1):
        if n % i == 0:
            return False
    return True
def trungbinhcongchan(number):
    sum = 0
    for i in range(0,len(number),1):
        if i % 2 == 0:
            sum += number[i]
    a = math.ceil(len(number) / 2)
    return sum / a
def desophantuchiahetchok(num,k):
    count = 0
    for i in range(0, len(num)):
        if math.fabs(num[i]) % k == 0 and math.fabs(num[i]) >= k :
            count += 1
    return count
def printSoNguyenTo(numb):
    for i in range(0, len(numb)):
        if checkSoNguyenTo(numb[i]) == True:
            print(f"({i},{numb[i]})", end="")
def daonguoc(num):
    numRev = []
    for i in range(len(num)-1,-1,-1):
        numRev.append(num[i])
    return numRev
def checkArray(num,num2):
    for i in range(0,len(num)):
        if num2[i] != num[i] :
            return False
    return True
def merge(number, first,middle,last):
    sizeL = middle - first +1
    sizeR = last - middle
    left = []
    right = []
    for i in range(0, sizeL):
        left.append(number[i + first])
    for j in range(0, sizeR):
        right.append(number[j + 1 + middle])
    i = 0
    j = 0
    k = first
    while i < sizeL and j < sizeR:
        if left[i] < right[j]:
            number[k] = left[i]
            k += 1
            i += 1
        else:
            number[k] = right[j]
            k += 1
            j += 1
    while (i < sizeL):
        number[k] = left[i];
        i += 1
        k += 1
    while (j < sizeR):
        number[k] = right[j];
        j += 1
        k += 1
def merSort(number, first, last):
    if first < last:
        middle = (first + last) // 2;
        merSort(number,first,middle)
        merSort(number,middle+1,last)
        merge(number,first,middle,last)


n = int( input("Nhap so n : "))
numbers = []
#for i in range(0,n,1):

numbers = []
numbers = [int(x) for x in input().split()]
print(numbers)
sum = 0
for i in numbers:
    sum = sum + i
print(sum)
print(f"Trung binh cong là : {sum/n}")
print(f"Trung binh cong tai vi tri chan là : {int(trungbinhcongchan(numbers)) }")
printSoNguyenTo(numbers)
print()
print(f"So lon nhat thu 2 là : {findMax2(numbers)}")
k  = int(input("Nhap so k:"))
print(f"So phan tu chia het cho k la : {desophantuchiahetchok(numbers,k)}")
if(checkArray(numbers,daonguoc(numbers))) == True:
    print("YES")
else:
    print("NO")
merSort(numbers,0,n-1)
print(numbers)
str = [x for x in input("Nhap chuoi ky tu: ").split()]
merSort(str,0,len(str)-1)
print(str)
str.sort(key = lambda x: len(x))
print(str)