from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, 0))

    visit = [0 for _ in range(n+1)]
    visit[x] = 1

    while q:
        cur, cur_d = q.popleft()
        if cur == y:
            return cur_d
        
        for i, d in arr[cur]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i, cur_d + d))

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
ans = []

for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    ans.append(bfs(a, b))

for i in ans:
    print(i)