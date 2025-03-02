def s_z(arr, i, j):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 벽에 막히지 않으면 그 방향으로 계속 진행
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        while 0<=nr<N and 0<=nc<N and arr[nr][nc] != 1:
            arr[nr][nc] = 3
            nr += dr[k]
            nc += dc[k]
    

def f_m(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

# 괴물은 1마리
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    i, j = f_m(arr)
    s_z(arr, i, j)
    # 벽이 없고 괴물의 광선이 닿지 않는 안전한 곳 찾기
    result = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                result += 1
    
    print(f'#{t} {result}')