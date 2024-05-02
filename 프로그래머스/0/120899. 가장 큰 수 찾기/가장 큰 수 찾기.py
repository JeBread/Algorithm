def solution(array):
    ans = []
    for i in range(len(array)):
        if array[i] == max(array):
            ans.append(max(array))
            ans.append(i)
    return ans