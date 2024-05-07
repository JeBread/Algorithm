def solution(keyinput, board):
    ans = [0, 0]
    n = (board[0]//2)
    m = (board[1]//2)
    for x in keyinput:
        if x == 'up':
            if ans[1] < m:
                ans[1] += 1
        elif x == 'down':
            if ans[1] > -m:
                ans[1] -= 1
        elif x == 'left':
            if ans[0] > -n:
                ans[0] -= 1
        else:
            if ans[0] < n:
                ans[0] += 1
    return ans