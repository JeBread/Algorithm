N = int(input())
lst = [0]*1001

for _ in range(N):
    L, H = map(int, input().split())
    lst[L] = H

mx_i = 0
maxV = -21e8
sum1 = 0
for i in range(len(lst)):
    if lst[i] > maxV:
        maxV = lst[i]
        mx_i = i
maxV = -21e8
for i in range(mx_i + 1):
    if lst[i] > maxV:
        maxV = lst[i]
    sum1 += maxV

maxV = -21e8
sum2 = 0
for i in range(1000, mx_i, -1):
    if lst[i] > maxV:
        maxV = lst[i]
    sum2 += maxV

ret = sum1 + sum2
print(ret)
