'''
구슬은 좌우로만 움직일 수 있어 맨 위 벽돌만 깨트릴 수 있음
벽돌 숫자 1~9
구슬 명중한 벽돌은 벽돌에 적힌 숫자 - 1 만큼 상하좌우로 제거
N번 쏘기 가능, W: 가로, H: 세로
남은 벽돌 개수 출력

1


1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
'''
from collections import deque
import copy

# 구슬을 떨어트릴 위치를 고르기 위해 모든 열을 탐색
# 0 이상인 값을 가진 행*열 값을 찾아 큐에 추가
def execute(matrix, depth):
    global min_remains

    if depth == N:
        sub_remains = count_bricks(matrix)
        min_remains = min(min_remains, sub_remains)
        return

    for col in range(W): # 하나의 컬럼 선택 후 가장 위에 있는 값으로 아래 벽돌 부수기 진행
        curr_matrix = remove_bricks(col, copy.deepcopy(matrix)) # 구슬 벽돌에 충돌 후 벽돌 부수기 + 주변 벽돌 부수기
        curr_matrix = gravity(curr_matrix) # 부서진 후 생긴 공백 따라 밑으로 떨어트리기
        execute(curr_matrix, depth + 1) # 같은 행위를 depth가 N이 될 때까지 반복


def remove_bricks(col, curr_matrix):
    # row = None
    for i in range(H):
        if curr_matrix[i][col] > 0:
            row = i
            break
    else:
        return curr_matrix

    Q = deque()
    Q.append((row, col, curr_matrix[row][col]))
    curr_matrix[row][col] = 0

    while Q:
        curr_r, curr_c, distance = Q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            for d in range(1, distance):
                next_r = curr_r + di * d
                next_c = curr_c + dj * d
                if 0 <= next_r < H and 0 <= next_c < W and curr_matrix[next_r][next_c] > 0:
                    Q.append((next_r, next_c, curr_matrix[next_r][next_c]))
                    curr_matrix[next_r][next_c] = 0
    return curr_matrix

def count_bricks(matrix):
    count = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] != 0:
                count += 1
    return count

def gravity(matrix):
    for j in range(W):
        i = 0
        while i + 1 < H:
            if matrix[i][j] != 0 and matrix[i + 1][j] == 0:
                matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                i -= 1
                if i < 0:
                    i = 0
            else:
                i += 1
    return matrix

T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    min_remains = float('inf')
    execute(matrix, 0)
    print(f"#{t} {min_remains}")