def solution(n, computers):            
    
    def DFS(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] and not visited[a]:
                DFS(a)      
                
    ans = 0
    visited = [0 for _ in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            ans += 1
        
    return ans