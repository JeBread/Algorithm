def solution(phone_number):
    ans = ''
    for i in range(0, len(phone_number)-4):
        ans += '*'
    return ans + phone_number[-4:]