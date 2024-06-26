def solution(board):
    
    cnt = 0
    n = len(board[0])
    directy = [1, 1, 1, 0, -1, -1, -1, 0]
    directx = [-1, 0, 1, 1, 1, 0, -1, -1]
    bomb_y = []
    bomb_x = []
    
    # 처음 지뢰가 있는 곳 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb_y.append(i)
                bomb_x.append(j)

    # 처음 지뢰가 있던 곳 주변 위험지역 표시하기
    for i in range(len(bomb_y)):
        for k in range(8):
            dy = directy[k] + bomb_y[i]
            dx = directx[k] + bomb_x[i]
            if 0 <= dy < n and 0 <= dx < n:
                board[dy][dx] = 1
    # 안전한 지역 찾기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt += 1
    
    return cnt

# 다른 사람의 풀이

# def solution(board):
#     n = len(board)
#     danger = set()
#     for i, row in enumerate(board):
#         for j, x in enumerate(row):
#             if not x:
#                 continue
#             danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
#     return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)