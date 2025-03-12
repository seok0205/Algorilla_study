# 나이트가 체스판의 가장 왼쪽 아래 칸에 위치
# 네 가지 움직임
# 2칸 위로, 1칸 오른쪽
# 1칸 위로, 2칸 오른쪽
# 1칸 아래로, 2칸 오른쪽
# 2칸 아래로, 1칸 오른쪽
# 이동 횟수가 4보다 같거나 크다면 이동 방법 한 번씩 모두 사용해야 함
# 이동 횟수가 4보다 적으면 이동 방법에 제약 없음
# 방문할 수 있는 최대 칸 개수 출력
from collections import deque

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
curr_r, curr_c = N, 0
board[curr_r][curr_c] = 1
count = 0
Q = deque()
while curr_c < M:
    for di, dj in [[-2, 1], [-1, 2], [1, 2], [2, 1]]:
        next_r, next_c = curr_r + di, curr_c + dj
        if 0 <= next_r < N and 0 <= next_c < M and board[next_r][next_c] == 0:
            board[next_r][next_c] = 1
            Q
