def solution(array):
	cnt_list = [0] * (max(array)+1) # 숫자 출연 횟수를 셀 리스트
	for i in array:
		cnt_list[i] += 1

	m = 0 # 최빈값의 개수
	for c in cnt_list:
		if c == max(cnt_list):
			m += 1
    
	if m > 1: # 최빈값이 2개 이상이면 -1을 리턴
		return -1
	else: # 최빈값이 1개이면 해당 숫자를 리턴
		return cnt_list.index(max(cnt_list))