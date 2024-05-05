from collections import Counter

def solution(s):
    # 문자의 등장 횟수를 계산
    char_count = Counter(s)
    
    # 한 번만 등장하는 문자만을 추출하고 사전 순으로 정렬
    single_chars = sorted([char for char, count in char_count.items() if count == 1])
    
    # 정렬된 문자들을 문자열로 합쳐서 반환
    return ''.join(single_chars)