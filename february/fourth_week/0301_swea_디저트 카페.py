'''
대각선 방향 움직여야 하며 사각형 모양 그려야 함
같은 숫자가 있으면 안 됨
가능한 경우 중 가장 디저트를 많이 먹는 경우의 디저트 수 출력 디저트 못 먹으면 -1로 출력
'''

from collections import deque


def dfs(r, c, start_r, start_c, direction, visited):
    global max_val

    # if len(visited) >= 4 and direction == 3 and (r, c) == (start_r, start_c):
    #     max_val = max(max_val, len(visited))
    #     return

    directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for d in range(direction, min(4, direction + 2)):
        next_r = r + directions[d][0]
        next_c = c + directions[d][1]

        if d == 3 and (next_r, next_c) == (start_r, start_c) and len(visited) >= 4:
            max_val = max(max_val, len(visited))
            return

        if 0 <= next_r < N and 0 <= next_c < N and district[next_r][next_c] not in visited:
            dfs(next_r, next_c, start_r, start_c, d, visited + [district[next_r][next_c]])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    district = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 0, [district[i][j]])

    print(f"#{t} {max_val}")
#
#
# def dfs(r, c, start_r, start_c, direction, visited):
#     global max_val
#
#     # 3번 방향 전환 후 돌아왔을 때 최대값을 갱신
#     if direction == 3 and (r, c) == (start_r, start_c):
#         max_val = max(max_val, len(visited))
#         return
#
#     directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
#
#     # 방향 전환을 두 가지로만 제한
#     for d in range(2):  # 0: 직진, 1: 좌회전
#         next_direction = (direction + d) % 4
#         next_r = r + directions[next_direction][0]
#         next_c = c + directions[next_direction][1]
#
#         if 0 <= next_r < N and 0 <= next_c < N and district[next_r][next_c] not in visited:
#             visited.append(district[next_r][next_c])
#             dfs(next_r, next_c, start_r, start_c, next_direction, visited)
#             visited.pop()  # 백트래킹
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     district = [list(map(int, input().split())) for _ in range(N)]
#
#     max_val = -1
#     for i in range(N):
#         for j in range(N):
#             dfs(i, j, i, j, 0, [district[i][j]])
#
#     print(f"#{t} {max_val}")





