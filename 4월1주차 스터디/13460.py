import sys
input = sys.stdin.readline
from collections import deque
'''
'.' : 빈칸 , '#' : 공이 이동 불가한 벽, 'O' : 구멍 위치
'R' : 빨간 공, 'B' : 파란 공
가장자리에는 모두 #이 있음
'''
'''
벽에 부딪히는걸 기준으로 stack에 넣은다음에 dfs를 돌리자
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(i, j, x, y, cnt):
    stack = deque()
    stack.append((i, j, x, y))
    cnt = 0
    while stack:
        p, q, r, c, cnt = stack.popleft()
        # 만약 빨간공의 위치가 구멍과 같으면 몇번 움직였는지 반환
        if (p, q) == (g_x, g_y):
            return cnt

        for k in range(4):
            z = 0
            w = 0
            temp = []
            while True:
                z += 1
                np, nq = p + dr[k]*z, q + dc[k]*z
                if 1<=np<N-1 and 1<=nq<M-1 and arr[np][nq] == 'B':
                    while True:
                        z += 1
                        if arr[np][nq] == '#':
                            temp.append(p+dr[k]*(z-1)) ; temp.append(nq)
                            break
                    break
                if 1<=np<N-1 and 1<=nq<M-1 and arr[np][nq] == '.':
                    continue
                if 1<=np<N-1 and 1<=nq<M-1 and arr[np][nq] == '#':
                    temp.append(p+dr[k]*(z-1)) ; temp.append(nq)
                    break
            while True:
                w += 1
                



N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
r_x, r_y = 0, 0
b_x, b_y = 0, 0
g_x, g_y = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            r_x, r_y = i, j
        if arr[i][j] == 'B':
            b_x, b_y = i, j
        if arr[i][j] == 'O':
            g_x, g_y = i, j

dfs(r_x, r_y, b_x, b_y, 0)