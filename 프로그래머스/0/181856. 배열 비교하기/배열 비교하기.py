def solution(arr1, arr2):
    ans = 0
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            ans = 1
        elif sum(arr1) < sum(arr2):
            ans = -1
        else:
            ans = 0
    elif len(arr1) > len(arr2):
        ans = 1
    else:
        ans = -1
            
    return ans