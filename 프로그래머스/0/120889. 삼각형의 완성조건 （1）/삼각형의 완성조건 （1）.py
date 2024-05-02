def solution(sides):
    ans = 0
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        ans = 1
    else:
        ans = 2
    return ans