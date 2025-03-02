# from collections import deque
#
# T = int(input())
# for t in range(1, T + 1):
#     map_size = int(input())
#     roads = [list(map(int, input())) for _ in range(map_size)]
#
#     start = (0, 0)
#     end = (map_size - 1, map_size - 1)
#
#     Q = deque()
#     distances = [[float('inf') for _ in range(map_size)] for _ in range(map_size)]
#     distances[0][0] = 0
#
#     Q.append(start)
#     r = c = 0
#     while Q:
#         r, c = Q.popleft()
#
#         # min_r, min_c = 0, 0
#         # min_val = float('inf')
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             next_r = r + di
#             next_c = c + dj
#             if 0 <= next_r < map_size and 0 <= next_c < map_size:
#                 if distances[next_r][next_c] > distances[r][c] + roads[next_r][next_c]:
#                     distances[next_r][next_c] = distances[r][c] + roads[next_r][next_c]
#                     Q.append((next_r, next_c))
#                 # min_r, min_c = next_r, next_c
#                 # min_val = roads[next_r][next_c]
#     for distance in distances:
#         print(*distance)
#
#     print(f"#{t}")

'''
1
4
0100
1110
1011
1010

'''

from collections import deque

T = int(input())
for t in range(1, T + 1):
    map_size = int(input())
    map_info = [list(map(int, input())) for _ in range(map_size)]
    cumulative_sum_graph = [[float('inf') for _ in range(map_size)] for _ in range(map_size)]
    start_r = start_c = 0
    Q = deque()
    Q.append((start_r, start_c))
    cumulative_sum_graph[start_r][start_c] = map_info[start_r][start_c]
    while Q:
        curr_r, curr_c = Q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            next_r, next_c = curr_r + di, curr_c + dj
            if 0 <= next_r < map_size and 0 <= next_c < map_size:
                if cumulative_sum_graph[next_r][next_c] > cumulative_sum_graph[curr_r][
                    curr_c] + map_info[next_r][next_c]:
                    Q.append((next_r, next_c))
                    cumulative_sum_graph[next_r][next_c] = cumulative_sum_graph[curr_r][curr_c] + map_info[next_r][
                        next_c]

    print(f"#{t} {cumulative_sum_graph[map_size - 1][map_size - 1]}")
