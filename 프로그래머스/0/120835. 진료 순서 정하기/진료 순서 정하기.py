def solution(emergency):
    ans = []
    lst = []
    lst = sorted(emergency, reverse=True)
    for x in emergency:
        ans.append(lst.index(x) + 1)
    return ans