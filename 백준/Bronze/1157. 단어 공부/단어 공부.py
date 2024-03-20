words = input().upper()
words1 = list(set(words))
cnt_list = []
for st in words1:
    cnt_list.append(words.count(st))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(words1[max_index]) 