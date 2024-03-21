string = list(input())
string.reverse()
A, B = '', ''
for i in range(7):
    if string[i] == ' ': continue
    elif i < 3:
        A += string[i]
    else: B += string[i]
if int(A) > int(B):
    print(int(A))
else:
    print(int(B))