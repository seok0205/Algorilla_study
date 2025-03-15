'''
처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방 이동가능한지 구해야 함
처음 출발해야 하는 방 번호, 최대 몇 개 방 이동 가능한지 숫자 출력해야 함
이동할 수 있는 방의 개수가 최대인 방이 여러 개라면 최소값을 출력
이동하려는 방 존재해야 & 이동하려는 방에 적힌 숫자가 현재 방 숫자보다 1 더 커야
상하좌우 이동 가능

2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''


# def move_rooms(row, col, path):
#     global moving_num
#     global room_num
#
#     if len(path) > moving_num:
#         moving_num = len(path)
#         room_num = path[0]
#     if len(path) == moving_num and room_num > path[0]:
#         room_num = path[0]
#
#     for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         next_r = row + di
#         next_c = col + dj
#         if 0 <= next_r < N and 0 <= next_c < N and grid[next_r][next_c] == grid[row][col] + 1:
#             move_rooms(next_r, next_c, path + [grid[next_r][next_c]])
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     moving_num = 0
#     room_num = float('inf')
#     for i in range(N):
#         for j in range(N):
#             move_rooms(i, j, [grid[i][j]])
#
#     print(f"#{t} {room_num} {moving_num}")


def move_rooms(row, col):
    global moving_num
    global room_num

    if dp[row][col] != -1:
        return dp[row][col]

    dp[row][col] = 1

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        next_r = row + di
        next_c = col + dj
        if 0 <= next_r < N and 0 <= next_c < N and grid[next_r][next_c] == grid[row][col] + 1:
            dp[row][col] = max(dp[row][col], move_rooms(next_r, next_c) + 1)

    return dp[row][col]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * N for _ in range(N)]
    moving_num = 0
    room_num = float('inf')
    for i in range(N):
        for j in range(N):
            move_rooms(i, j)
            if dp[i][j] > moving_num:
                moving_num = dp[i][j]
                room_num = grid[i][j]
            elif dp[i][j] == moving_num and grid[i][j] < room_num:
                room_num = grid[i][j]

    print(f"#{t} {room_num} {moving_num}")
