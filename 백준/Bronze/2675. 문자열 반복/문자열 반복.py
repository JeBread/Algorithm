T = int(input())
for tc in range(1, T+1):
    R, S = input().split()
    r = int(R)
    
    for word in S:
        print(word*r,end='')
    print()