from collections import deque

def bfs(arr, structure, N, M, R, C, L):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    visited[R][C] = 1
    time = 1
    q.append([R, C, time])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c, l = q.popleft()
        
        if l == L:
            break
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                if arr[nr][nc] in structure[arr[r][c]][k]:
                    visited[nr][nc] = 1
                    q.append([nr, nc, l+1])
                    
    return visited
    
T = int(input())
for t in range(1, 1+T):
    # N x M 지하터널, (R, C) : 맨홀 뚜껑이 위치한 장소, L : 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 각 구조물이 서로 연결 될 수 있는지를 체크해두자
    # 상하좌우
    # 현재 위치를 중심으로 각 방향에 올 수 있는 파이프 체크
    structure = {1 : {0 : [1, 2, 5, 6], 1 : [1, 2, 4, 7], 2 : [1, 3, 4, 5], 3 : [1, 3, 6, 7]},
            2 : {0 : [1, 2, 5, 6], 1 : [1, 2, 4, 7], 2 : [], 3 : []},
            3 : {0 : [], 1 : [], 2 : [1, 3, 4, 5], 3 : [1, 3, 6, 7]},
            4 : {0 : [1, 2, 5, 6], 1 : [], 2 : [], 3 : [1, 3, 6, 7]},
            5 : {0 : [], 1 : [1, 2, 4, 7], 2 : [], 3 : [1, 3, 6, 7]},
            6 : {0 : [], 1 : [1, 2, 4, 7], 2 : [1, 3, 4, 5], 3 : []},
            7 : {0 : [1, 2, 5, 6], 1 : [], 2 : [1, 3, 4, 5], 3 : []}}
    
    result = bfs(arr, structure, N, M, R, C, L)
    final = 0
    for i in range(N):
        for j in range(M):
            if result[i][j] == 1:
                final += 1

    print(f'#{t} {final}')

    