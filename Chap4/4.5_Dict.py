import show
n =int(input("So cap thong tin : "))
d = dict()

def find_max(dict:dict):
    value = list(dict.values())
    max = 1
    for i in value:
        if int(i) > int(max):
            max = i
    return max

for i in range(0, n):
    s = [x for x in input().split()]
    d[s[0]] = s[1]
max = find_max(d)
for i in d:
    if d[i] == max:
        print(f"{i}:{d[i]}", end=" ")
key = input()
d.pop(key)
print(d)
arr = ['duc', 'anh', 'nguyen']
show.show(arr)
#id  = [x for x in input().split()]

