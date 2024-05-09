def solution(bubbling):
    ans = 0
    lst = ['aya', 'ye', 'woo', 'ma']
    
    
    for i in bubbling:
        cnt = 0
        word = ''
        for j in i:
            word += j
            if word in lst:
                word = ''
                cnt += 1
        if len(word) == 0 and cnt > 0:
            ans += 1

    return ans