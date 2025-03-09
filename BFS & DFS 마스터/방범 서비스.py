from collections import deque

# K 가 마을 크기를 넘어가면 안됨 (k : 1~N+1)
def bfs(arr, i, j, N, M):
    house = 0
    for k in range(1, N+2):
        # 각 k마다의 비용
        cost = k**2 + (k-1)**2

        visited = [[0]*N for _ in range(N)]
        q = deque()
        # 서비스 받을 수 있는 집의 수
        count = 0
        
        visited[i][j] = 1
        q.append([i, j, 0])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        # k 범위를 벗어나면 break
        while q:
            r, c, flag = q.popleft()
            # flag가 내가 탐색중인 k칸이 되면 break
            if flag == k:
                break
            # 집이 있으면 카운트 추가
            if arr[r][c] == 1:
                count += 1
                
            for w in range(4):
                nr, nc = r + dr[w], c + dc[w]
                if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append([nr, nc, flag+1])
        
        if count * M >= cost:
            house = max(house, count)
        
    return house

T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    final = 0
    for i in range(N):
        for j in range(N):
            final = max(bfs(arr, i, j, N, M), final)
            
    print(f'#{t} {final}')