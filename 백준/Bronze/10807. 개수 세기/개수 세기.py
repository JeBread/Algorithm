N = int(input())

lst = list(map(int, input().split()))
v = int(input())
cnt = 0
for num in lst:
    if num == v:
        cnt += 1
print(cnt)