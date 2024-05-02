def solution(box, n):
    ans = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return ans