def solution(n):
    ans = []
    nn = str(n)
    for x in nn[::-1]:
        ans.append(int(x))
    return ans