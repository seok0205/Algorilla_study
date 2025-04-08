import sys
input = sys.stdin.readline
'''
테트로미노란 정사각형 4개를 이어 붙인 도형
N x M 종이 위에 테트로미노 하나를 놓는다.
테트로미노 하나를 적절히 놓아 놓인 칸에 있는 수의 합의 최댓값?
회전이나 대칭시켜도 됨
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# dfs만으로는 엿모양이 해결이 안됨 -> 엿모양은 따로 처리
def dfs(i, j, s, cnt):
    global result
    if cnt == 4:
        result = max(result, s)
        return
    if s + (1000*(4-cnt)) <= result:
        return
    for k in range(4):
        nr, nc = i + dr[k], j + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc]:
            continue
        visited[i][j] = 1
        dfs(nr, nc, s+arr[i][j], cnt+1)
        visited[i][j] = 0

# 우 모양
def ect1(i, j):
    global result
    if i == N-1 or j >= M - 2:
        return 0
    val = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
    result = max(result, val)
# 아 모양
def ect2(i, j):
    global result
    if i >= N-2 or j == M - 1:
        return 0
    val = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1]
    result = max(result, val)
# 오 모양
def ect3(i, j):
    global result
    if i == 0 or j >= M-2:
        return 0
    val = arr[i][j] + arr[i-1][j+1] + arr[i][j+1] + arr[i][j+2]
    result = max(result, val)
# 어 모양
def ect4(i, j):
    global result
    if i >= N-2 or j == 0:
        return 0
    val = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j-1]
    result = max(result, val)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        dfs(i, j, 0, 0)
        ect1(i, j) ; ect2(i, j) ; ect3(i, j); ect4(i, j)
print(result)