from collections import deque

# K 범위가 N을 넘지 않도록 설정 (1 ≤ K ≤ N)
def bfs(arr, i, j, N, M):
    max_houses = 0  # 최대로 커버할 수 있는 집의 개수

    for k in range(1, N+2):  # K는 1부터 시작
        cost = k * k + (k - 1) * (k - 1)  # 운영 비용
        visited = [[0] * N for _ in range(N)]
        q = deque([(i, j, 0)])  # (r, c, depth)
        visited[i][j] = 1
        count = 0  # 커버할 수 있는 집의 개수

        while q:
            r, c, depth = q.popleft()
            if depth >= k:  # K 범위 초과 시 종료
                break
            if arr[r][c] == 1:
                count += 1  # 집 개수 카운트
            
            # 4방향 탐색
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc, depth + 1))
        
        # 손해를 보지 않으면서 최대한 많은 집을 커버할 수 있도록 갱신
        if count * M >= cost:
            max_houses = max(max_houses, count)

    return max_houses


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    final_result = 0
    for i in range(N):
        for j in range(N):
            final_result = max(final_result, bfs(arr, i, j, N, M))
    
    print(f'#{t} {final_result}')
