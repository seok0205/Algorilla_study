import sys, copy
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# (i, j) : 시작점, (a, b) : 어디 벽을 깼는지
def bfs(i, j, a, b):
    arr_copy = copy.deepcopy(arr)
    # 벽을 통로로 바꿔줌
    arr_copy[a][b] = '0'
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<N and 0<=nc<M and arr_copy[nr][nc] == '0' and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
                if nr==N-1 and nc==M-1:
                    return visited[nr][nc]
        
    return -1

# 벽을 최대 1개 깰 수 있다
# 시작점 (1, 1)과 (N, M)은 항상 0
# 못가면 -1출력
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
# 모든 벽을 하나씩 깨보자
# 무조건 벽을 1개는 깨는게 경로가 짧아짐


if N == 2 and M == 2:
    print(3)
elif arr[0][1] == '1' and arr[1][0]=='1' and arr[N-1][M-2] =='1' and arr[N-2][M-1] =='1':
    print(-1)
else:
    result = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                result = max(bfs(0, 0, i, j), result)

    print(result)
