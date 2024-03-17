N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum = 0
maxV = -21e8
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum += lst[i] + lst[j] + lst[k]
            if maxV <= sum <= M:
                maxV = sum
            sum = 0

print(maxV)