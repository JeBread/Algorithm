def solution(k, m, score):
    res = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if (i + m) > len(score):
            return res
        res += min(score[i:i+m]) * m
    return res