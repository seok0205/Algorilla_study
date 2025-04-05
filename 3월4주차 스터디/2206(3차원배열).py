import sys
from collections import deque

def bfs():
    # visited[x][y][w]:
    # w == 0 : (x, y)에 벽을 부수지 않고 도착한 경우, w == 1 : 이미 벽을 부순 경우
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    
    dq = deque()
    dq.append((0, 0, 0))  # 시작점 (0,0)에서 벽 부수지 않은 상태(w=0)
    visited[0][0][0] = 1  # 시작점 거리 1
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while dq:
        x, y, w = dq.popleft()
        # 목적지 도착 시 현재까지 이동한 거리 반환
        if x == N - 1 and y == M - 1:
            return visited[x][y][w]
        for dx, dy in zip(dr, dc):
            nx, ny = x + dx, y + dy
            # 범위 내이고
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 공간인 경우
                if arr[nx][ny] == '0' and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    dq.append((nx, ny, w))
                # 벽인 경우, 아직 벽을 부수지 않은 상태라면
                elif arr[nx][ny] == '1' and w == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    dq.append((nx, ny, 1))
    return -1

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
result = bfs()
print(result)
