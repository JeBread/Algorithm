h, w = map(int,input().split())
block = list(map(int,input().split()))
ans = 0
 
for i in range(1, w-1):
    left = max(block[ :i])
    right = max(block[i+1: ])
    m = min(left, right)
    if m > block[i]:
        ans += m - block[i]
 
print(ans)