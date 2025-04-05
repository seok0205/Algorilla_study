# 상하좌우 이웃한 육지로만 이동가능
# 최단 경로로 가야돼
# 근데 젤 멀어야돼
import sys
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[0] * W for _ in range(L)]
    visited[i][j] = 1
    
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<L and 0<=nc<W and visited[nr][nc] == 0 and arr[nr][nc] == 'L':
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    
    max_len = 0
    for p in range(L):
        for q in range(W):
            if visited[p][q] > max_len:
                max_len = visited[p][q]
                
    return max_len-1

input = sys.stdin.readline
L, W = map(int, input().split())
arr = [list(input().strip()) for _ in range(L)]
# 모든 육지에서 출발을 해
# 각 지점부터 최단경로로 이동하는데 가장 먼 지점을 찾아
# 모든 경우 체크 후 가장 긴거 찾아
result = []
for i in range(L):
    for j in range(W):
        if arr[i][j] == 'L':
            temp = bfs(i, j)
            result.append(temp)
print(max(result))
            