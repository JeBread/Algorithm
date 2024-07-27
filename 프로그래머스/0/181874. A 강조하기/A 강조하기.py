def solution(myString):
    ans = ''
    for x in myString:
        ans += x.lower()
    return ans.replace('a','A')