lst = [int(input()) for _ in range(9)]
maxV = -1
ret = 0
for i in range(len(lst)):
    if lst[i] > maxV:
        maxV = lst[i]
        ret = i+1
print(maxV)
print(ret)