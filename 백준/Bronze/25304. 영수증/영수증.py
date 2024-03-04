X = int(input())
N = int(input())
sum = 0
for _ in range(1, N+1):
    a, b = map(int, input().split())
    sum += a * b
if sum == X:
    print('Yes')
else:
    print('No')