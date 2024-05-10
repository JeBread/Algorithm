str = input()
for x in str:
    if x.islower():
        print(x.upper(),end='')
    else:
        print(x.lower(),end='')