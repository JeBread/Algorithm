from collections import Counter
def solution(k, tangerine):
    ans = 0
    counter = Counter(tangerine)
    sorted_Dict = sorted(counter.items(),key=lambda x : x[1],reverse = True)
    
    cnt = 0
    for i in sorted_Dict:
        k -= i[1]
        ans += 1
        
        if k <= 0:
            break
            
    return ans