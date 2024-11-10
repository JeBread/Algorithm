def solution(d, budget):
    ans = 0
    d.sort()
    sum = 0
    for i in range(len(d)):
        if sum > budget:
            continue
        if sum <= budget:
            if sum + d[i] <= budget:
                sum += d[i]
                ans += 1
        
    return ans