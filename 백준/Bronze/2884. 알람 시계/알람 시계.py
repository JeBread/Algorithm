H, M = map(int, input().split())
if M < 45:
    if H == 0:
        H = 24
    print(f'{H-1} {(M+60)-45}')
else:
    print(f'{H} {M-45}')