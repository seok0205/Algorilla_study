import sys
input = sys.stdin.readline
'''
테트로미노란 정사각형 4개를 이어 붙인 도형
N x M 종이 위에 테트로미노 하나를 놓는다.
테트로미노 하나를 적절히 놓아 놓인 칸에 있는 수의 합의 최댓값?
회전이나 대칭시켜도 됨
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# dfs만으로는 엿모양이 해결이 안됨 -> 엿모양은 따로 처리
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