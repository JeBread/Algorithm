def solution(common):
    
    a1, a2 = common[0], common[1]
    d = a2 - a1
    if a1 != 0:
        r = a2 // a1 if a1 != 0 and a2 % a1 == 0 else None

    # 등차수열
    is_arithmetic = True
    for i in range(2, len(common)):
        if common[i] - common[i - 1] != d:
            is_arithmetic = False
            break
    if is_arithmetic:
        return common[-1] + d

    # 등비수열
    is_geometric = True
    if r is not None:
        for i in range(2, len(common)):
            if common[i - 1] != 0 and common[i] // common[i - 1] == r and common[i] % common[i - 1] == 0:
                continue
            is_geometric = False
            break
    if is_geometric:
        return common[-1] * r