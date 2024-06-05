import math
from collections import deque

tc = int(input())
INF = math.inf

for t in range(tc):
    n = int(input())
    mapArr = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[INF for _ in range(n)] for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(deq, visited):
        while deq:
            (x, y, sums) = deq.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n or (nx, ny) == (0, 0) or visited[nx][ny] <= mapArr[nx][ny] + sums:
                    continue

                visited[nx][ny] = mapArr[nx][ny] + sums
                deq.append((nx, ny, visited[nx][ny]))
        return visited[-1][-1]

    deq = deque()
    deq.append((0, 1, mapArr[0][1]))
    deq.append((1, 0, mapArr[1][0]))
    print("#" + str(t + 1) + " " + str(bfs(deq, visited)))