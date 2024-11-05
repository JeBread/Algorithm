def solution(todo_list, finished):
    ans = []
    for i in range(len(finished)):
        if not finished[i]:
            ans.append(todo_list[i])
    return ans