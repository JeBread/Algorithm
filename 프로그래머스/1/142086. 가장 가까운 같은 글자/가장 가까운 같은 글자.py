def solution(s):

    ans = []
    dict = {}

    for i in range(len(s)):
        if s[i] not in dict:
            ans.append(-1)
        else:
            ans.append(i-dict[s[i]])
        dict[s[i]] = i

    return ans