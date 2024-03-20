string = input()
cnt = 0
for i in range(len(string)):
    if string[i] == ' ':
        cnt += 1
if string[0] == ' ':
    cnt -= 1
if string[len(string)-1] == ' ':
    cnt -= 1
print(cnt+1)