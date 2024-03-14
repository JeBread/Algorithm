N = int(input())
arr = [[0] * 100 for _ in range(100)]

def paper(y, x):
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            arr[i][j] = 1

for _ in range(N):
    A, B = map(int, input().split())
    paper(A, B)

sum = 0
for i in range(100):
    for j in range(100):
        sum += arr[i][j]
print(sum)