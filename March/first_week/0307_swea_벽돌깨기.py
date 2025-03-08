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

def execute(matrix):
    global min_remains
    # min_remains = float('inf')
    # curr_matrix = copy.deepcopy(matrix)
    # candidates = find_where_to_shoot(curr_matrix)
    # while candidates:
    #     candidate_r, candidate_c, _ = candidates.pop()
    #     curr_matrix = remove_bricks(candidate_r, candidate_c, curr_matrix)
    #     curr_matrix = gravity(curr_matrix)
    #     sub_remains = count_bricks(curr_matrix)
    #     execute(curr_matrix)
    #     min_remains = min(sub_remains, min_remains)
    # return

def find_where_to_shoot(matrix):
    list = []

    for i in range(H):
        for j in range(W):
            if matrix[i][j] != 0:
                list.append((i, j, matrix[i][j]))
        if len(list) > 0:
            list.sort(key=lambda x: x[2])
            return list


def remove_bricks(r, c, curr_matrix):
    Q = deque()
    Q.append((r, c))
    while Q:
        curr_r, curr_c = Q.popleft()
        distance = curr_matrix[curr_r][curr_c] - 1
        curr_matrix[curr_r][curr_c] = 0
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            for d in range(1, distance):
                next_r = curr_r + di * d
                next_c = curr_c + dj * d
                if 0 <= next_r < H and 0 <= next_c < W:
                    Q.append((next_r, next_c))
    return curr_matrix

def count_bricks(matrix):
    count = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] != 0:
                count += 1
    return count

def gravity(matrix):
    for j in range(4):
        i = 0
        while 0 < i + 1 < 5:
            if matrix[i][j] == 1 and matrix[i + 1][j] == 0:
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
    execute(matrix)
    # answer = execute()
    print(f"#{t} {min_remains}")
