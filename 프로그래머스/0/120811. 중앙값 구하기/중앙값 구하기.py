def solution(array):
    ans = 0
    array.sort()
    ans = array[len(array)//2]
    return ans