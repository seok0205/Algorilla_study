import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global count, result
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            q = deque()
            if arr[i][j] == '1' and visited[i][j] == 0:
                count += 1
                visited[i][j] = 1
                q.append((i, j))
                temp = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nr, nc = x + dr[k], y + dc[k]
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1' and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                            temp += 1
                result.append(temp)


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
# bfs로 풀어보자!
# 배열돌다가 1만났을때, visited체크하고 1만나는 개수 세어줌
# 다음 차례로 갈 때, visited확인하면서 visited체크 안되어 있으면 탐색 시작

count = 0
result = []
bfs(0, 0)
result.sort()
print(count)
for num in result:
    print(num)