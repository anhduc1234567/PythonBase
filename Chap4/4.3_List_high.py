
def print_matrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
def input_matrix(matrix, m, n):
    for i in range(0, m):
        matrix.append([int(x) for x in input().split()])
def input_matrix2(matrix, m ,n):
    arr = [int(x) for x in input().split()]
    for i in range(0,m):
        matrix.append([])
        for j in range(0,n):
            matrix[i].append(arr[i * n + j])

def chuyenvi(matrix, row, col):
    result = []
    for i in range(0,col):
        result.append([matrix[int(x)][i] for x in range(0,row)])
    return result

def triagle(height):
    result = []
    for i in range(0,height):
        result.append([])
        for j in range(0, 2 * height - 1):
            if height - i - 1 == j or j == height + i - 1 or i == height - 1:
                result[i].append(" * ")
            else:
                result[i].append("   ")
    return result

row, col = input("Nhap cap ma tran ").split()
m = int(row)
n = int(col)
matrix = []
input_matrix(matrix,m,n)
matrix_chuyen_vi = chuyenvi(matrix, m, n)

print_matrix(matrix)
print()
print_matrix(matrix_chuyen_vi)
h = int(input())
tri = triagle(h)
print_matrix(tri)

