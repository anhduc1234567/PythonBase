def tongCacchuso(n):
    if n < 10:
        return n
    else:
        return n%10 + tongCacchuso(n//10)
def timsodaonguoc(n):
    if n < 10:
        return n
    else:
        return int(str(n%10) + str(timsodaonguoc(n//10)))
def timchudaonguoc(string, i):
    if i == 0:
        return string[0]
    else:
        return string[i] + timchudaonguoc(string,i - 1)
def timSoCacChuSo(n):
    if n < 10:
        return 1
    else:
        return 1 + timSoCacChuSo(n//10)
def timFirst(n):
    if n < 10:
        return n
    else:
        return timFirst(n//10)

def makeMatrix(matrix, rowStart,rowEend,colStart ,colEnd,value):
    if rowStart >= rowEend or colStart >= colEnd:
        return
    for i in range(colStart,colEnd,1):
        matrix[rowStart][i] = value
        value += 1
    rowStart +=1
    for i in range(rowStart,rowEend,1):
        matrix[i][colEnd - 1] = value
        value += 1
    colEnd -= 1
    if rowStart < rowEend:
        for i in range(colEnd-1,colStart - 1,-1):
            matrix[rowEend - 1][i] = value
            value += 1
        rowEend -= 1
    if colStart < colEnd:
        for i in range(rowEend - 1, rowStart -1,-1):
            matrix[i][colStart] = value
            value += 1
        colStart += 1
    makeMatrix(matrix,rowStart,rowEend,colStart ,colEnd ,value)

n = int(input())
print("-----------------------------")
print(tongCacchuso(n))
print(timsodaonguoc(n))
print(timSoCacChuSo(n))
print(timFirst(n))
string = input("Nhap string ")
print(timchudaonguoc(string, len(string)-1))
stra,strb = input().split()
row = int(stra)
col = int(strb)
arr = []
value = 1
rowS = 0
colS = 0
for i in range(0,row,1):
    arr.append([])
    for j in range(0,col,1):
        arr[i].append(0)
makeMatrix(arr,rowS,row,colS,col,value)
for i in range(0,row,1):
    for j in range(0,col,1):
        print("{0:5}".format(arr[i][j]), end="")
    print()