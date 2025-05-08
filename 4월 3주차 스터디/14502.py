import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def recur(cnt, arr):
    global result
    if cnt == 3:
        now_arr = deepcopy(arr)
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    count = bfs(i, j, now_arr)

        result = max(count, result)
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                recur(cnt+1, arr)
                arr[i][j] = 0


def bfs(i, j, arr):
    q = deque()
    q.append((i, j))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<N and 0<=nc<M:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 3
                    q.append((nr, nc))
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
recur(0, arr)
print(result)