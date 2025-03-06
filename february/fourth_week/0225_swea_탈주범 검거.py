# 1 상하좌우에 있는 터널과 연결됨
# 2 상하에 있는 터널과 연결됨
# 3 좌우에 있는 터널과 연결됨
# 4 상우에 있는 터널과 연결됨
# 5 하우에 있는 터널과 연결됨
# 6 하좌에 있는 터널과 연결됨
# 7 상좌에 있는 터널과 연결됨

# 멘홀에 있을 때가 탈출한 지 한 시간이 경과한 시점

from collections import deque

def find_ways(r, c):
    if map_info[r][c] == 1:
        ways = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]  # 상 하 좌 우
        result = []

        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:  # 맵 범위 체크
            if map_info[ways[0][0]][ways[0][1]] not in [3, 4, 7]:  # 다음 칸이 하를 포함할 때
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [3, 5, 6]:  # 다음 칸이 상을 포함할 때
                result.append(ways[1])

        if 0 <= ways[2][0] < map_height and 0 <= ways[2][1] < map_width:
            if map_info[ways[2][0]][ways[2][1]] not in [2, 6, 7]:  # 다음 칸이 우를 포함할 때
                result.append(ways[2])

        if 0 <= ways[3][0] < map_height and 0 <= ways[3][1] < map_width:
            if map_info[ways[3][0]][ways[3][1]] not in [2, 4, 5]:  # 다음 칸이 좌를 포함할 때
                result.append(ways[3])

        return result

    elif map_info[r][c] == 2:
        ways = [(r - 1, c), (r + 1, c)]  # 상 하
        result = []

        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:
            if map_info[ways[0][0]][ways[0][1]] not in [3, 4, 7]:
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [3, 5, 6]:
                result.append(ways[1])

        return result

    elif map_info[r][c] == 3:  # 좌 우
        ways = [(r, c - 1), (r, c + 1)]
        result = []
        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:
            if map_info[ways[0][0]][ways[0][1]] not in [2, 6, 7]:  # 다음 칸이 우를 포함할 때
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [2, 4, 5]:  # 다음 칸이 좌를 포함할 때
                result.append(ways[1])

        return result

    elif map_info[r][c] == 4:  # 상 우
        ways = [(r - 1, c), (r, c + 1)]
        result = []

        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:  # 맵 범위 체크
            if map_info[ways[0][0]][ways[0][1]] not in [3, 4, 7]:  # 다음 칸이 하를 포함할 때
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [2, 4, 5]:  # 다음 칸이 좌를 포함할 때
                result.append(ways[1])

        return result

    elif map_info[r][c] == 5:  # 하 우
        ways = [(r + 1, c), (r, c + 1)]
        result = []

        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:
            if map_info[ways[0][0]][ways[0][1]] not in [3, 5, 6]:  # 다음 칸이 상을 포함할 때
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [2, 4, 5]:  # 다음 칸이 좌를 포함할 때
                result.append(ways[1])

        return result

    elif map_info[r][c] == 6:  # 하 좌
        ways = [(r + 1, c), (r, c - 1)]
        result = []

        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:
            if map_info[ways[0][0]][ways[0][1]] not in [3, 5, 6]:  # 다음 칸이 상을 포함할 때
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [2, 6, 7]:  # 다음 칸이 우를 포함할 때
                result.append(ways[1])

        return result

    elif map_info[r][c] == 7:  # 상 좌
        ways = [(r - 1, c), (r, c - 1)]
        result = []

        if 0 <= ways[0][0] < map_height and 0 <= ways[0][1] < map_width:  # 맵 범위 체크
            if map_info[ways[0][0]][ways[0][1]] not in [3, 4, 7]:  # 다음 칸이 하를 포함할 때
                result.append(ways[0])

        if 0 <= ways[1][0] < map_height and 0 <= ways[1][1] < map_width:
            if map_info[ways[1][0]][ways[1][1]] not in [2, 6, 7]:  # 다음 칸이 우를 포함할 때
                result.append(ways[1])

        return result


T = int(input())
for t in range(1, T + 1):
    map_height, map_width, hole_r, hole_c, time = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(map_height)]

    # reachable_spots = 0

    visited = [[0 for _ in range(map_width)] for _ in range(map_height)]
    Q = deque()
    Q.append((hole_r, hole_c))
    visited[hole_r][hole_c] = 1
    # answer = 0

    while Q:
        curr_r, curr_c = Q.popleft()
        if visited[curr_r][curr_c] == time:
            answer = visited[curr_r][curr_c]
            break
        neighbors = find_ways(curr_r, curr_c)
        for neighbor_r, neighbor_c in neighbors:
            if 0 <= neighbor_r < map_height and 0 <= neighbor_c < map_width and not visited[neighbor_r][neighbor_c] and \
                    map_info[neighbor_r][neighbor_c] != 0:
                visited[neighbor_r][neighbor_c] = visited[curr_r][curr_c] + 1
                Q.append((neighbor_r, neighbor_c))

    count = 0
    for i in range(map_height):
        for j in range(map_width):
            if visited[i][j] > 0:
                count += 1

    print(f"#{t} {count}")
