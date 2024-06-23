def solution(my_string, index_list):
    ans = ''
    for x in index_list:
        ans += my_string[x]
    return ans