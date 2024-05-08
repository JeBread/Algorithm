def solution(quiz):
    ans = []
    lst = []
    for x in quiz:
        lst.append(x.split())
    for i in lst:
        if eval(''.join(i[0:3])) == int(i[4]):
            ans.append('O')
        else:
            ans.append('X')
    
    return ans