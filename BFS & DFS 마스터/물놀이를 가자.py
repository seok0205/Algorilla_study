from collections import deque

def bfs(arr, N, M):
    count = 0
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]
    q = deque()
    # 모든 땅 탐색
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                visited[i][j] = 1
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] == 'L':
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[x][y] + 1
                    q.append([nr, nc])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                count += visited[i][j] - 1
    print(q)
    return count 
          
T = int(input())
for t in range(1, T+1):
    # N x M 배열
    N, M = map(int, input().split())
    # W : 물, L : 땅
    arr = [list(input()) for _ in range(N)]
    result = bfs(arr, N, M)
    print(f'#{t} {result}')