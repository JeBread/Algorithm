T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]

for i in range(T):
    print(f'#{i+1} {round(sum(lst[i])/len(lst[i]))}')
