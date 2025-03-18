# import sys
# sys.stdin = open('input.txt', 'r')
# 하 좌 우
dr = [1, 0, 0]
dc = [0, -1, 1]
# s 가는 경로의 길이
def recur(i, j, s, start):
    global result, idx
    
    if i == 99:
        if s < result:
            result = s
            idx = start
        return s
    
    if s > result:
        return
    
    visited[i][j] = 1
    
    for k in range(1, 3):
        nc =  j + dc[k]
        if 0<=nc<100 and arr[i][nc] == 1 and visited[i][nc] == 0:
            recur(i, nc, s + 1, start)
            return
        
    nr = i + dr[0]
    if arr[nr][j] == 1:
        recur(nr, j, s + 1, start)
    
    
T = 10
for _ in range(T):
    t = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    
    result = int(1e10)
    idx = -1
    
    for j in range(100):
        visited = [[0]*100 for _ in range(100)]
        temp = 0
        if arr[0][j] == 1:
            recur(0, j, 0, j)
            
    print(f'#{t} {idx}')