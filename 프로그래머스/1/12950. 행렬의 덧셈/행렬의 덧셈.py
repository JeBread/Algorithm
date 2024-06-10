def solution(arr1, arr2):
    
    m = len(arr1) # 행
    n = len(arr1[0]) # 열
    ans = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ans[i][j] = arr1[i][j] + arr2[i][j]
    return ans