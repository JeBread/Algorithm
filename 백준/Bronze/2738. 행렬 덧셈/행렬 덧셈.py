N, M = map(int, input().split())
arr_A = [list(map(int, input().split())) for _ in range(N)]
arr_B = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr_A[i][j] += arr_B[i][j]
for row in arr_A:
    print(*row)