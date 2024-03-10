S = input()
lst = [-1]*26
for i in range(len(S)):
    if lst[(ord(S[i])-97)] == -1:
        lst[(ord(S[i])-97)] = i
print(*lst)