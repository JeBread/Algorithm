T = 10
for tc in range(1, T+1):
    N, lst = input().split()
    stack = []
    for i in range(len(lst)):
        if not stack or lst[i] != stack[-1]:
            stack.append(lst[i])
        else:
            stack.pop()
    print(f'#{tc}',end=' ')
    for i in range(len(stack)):
        print(stack[i],end='')
    print()