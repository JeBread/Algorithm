def solution(myString):
    ans = ''
    for x in myString:
        if x.islower():
            x = x.upper()
            ans += x
        else:
            ans += x
    return ans