def solution(s, skip, index):
    ans = ''
#   ord(a) = 97 ~ ord(z) = 122.  ASCII code
    
    for char in s:
        cnt = 0
        while cnt < index:
            char = chr(ord(char) + 1)
            if char > 'z':  
                char = 'a'
            if char not in skip:
                cnt += 1
        
        ans += char
    return ans