from collections import deque
 

def make_map(nr, nc, n, m):
    queue = deque()
    queue.append((nr, nc))
    walk_dist = [[0] * m for _ in range(n)]  # visited
    walk_dist[nr][nc] = 1
    while queue:
        r, c = queue.popleft()
        if water_park[r][c] == "W":
            return walk_dist[r][c] -1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= r + dr < N and 0 <= c + dc < M and walk_dist[r + dr][c + dc] == 0:
                nr, nc = r + dr, c + dc
                queue.append((nr, nc))
                walk_dist[nr][nc] = walk_dist[r][c] + 1
    return
 
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    water_park = [list(input()) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if water_park[i][j] == "L":
                ans += make_map(i, j, N, M)
    print(f'#{tc} {ans}')