import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(i, j, s, cnt):
    global result
    if cnt == 4:
        result = max(result, s)
        return
    
    if s + (1000*(4-cnt)) <= result:
        return
    
    for k in range(4):
        nr, nc = i + dr[k], j + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc]:
            continue
        
        # 'ㅗ'모양 처리
        # 깊이가 2일때 현재 위치에서 한번더 dfs를 들어가준다.
        if cnt == 2:
            visited[nr][nc] = 1
            dfs(i, j, s + arr[nr][nc], cnt+1)
            visited[nr][nc] = 0
        
        visited[nr][nc] = 1
        dfs(nr, nc, s+arr[nr][nc], cnt+1)
        visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = 0
print(result)