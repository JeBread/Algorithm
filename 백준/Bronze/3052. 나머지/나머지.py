lst = [int(input()) for _ in range(10)]
for i in range(10):
    lst[i] = lst[i]%42
lst2 = []
for i in range(10):
    if lst[i] in lst2: continue
    lst2.append(lst[i])
print(len(lst2))