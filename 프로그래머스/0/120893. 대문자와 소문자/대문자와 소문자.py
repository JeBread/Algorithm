def solution(my_string):
    ans = ''
    for st in my_string:
        if st.isupper():
            ans += st.lower()
        else:
            ans += st.upper()
    return ans