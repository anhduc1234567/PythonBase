
try:
    a = input('Nhao so : ')
    if a.isdigit() is False:
        raise ValueError('day k phai so nguyen ')
    else:
        print("JIS")
except ValueError as e:
    print(e)