def solution(my_string):
    ans = []
    for st in my_string:
        if st.isdigit():
            ans.append(int(st))
    ans.sort()
    return ans