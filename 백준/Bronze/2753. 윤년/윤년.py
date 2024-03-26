Y = int(input())
ret = 0
if Y % 4 == 0:
    if Y % 100 != 0 or Y % 400 == 0:
        ret = 1
print(ret)