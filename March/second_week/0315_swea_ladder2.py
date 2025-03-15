'''
최단 거리가 여러 개라면 col값이 제일 큰 것으로 출력
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
'''

from collections import deque

def play(start_row, start_col):
    global min_path, min_start
    count = 0
    Q = deque()
    visited = [[0] * SIZE for _ in range(SIZE)]
    Q.append((start_row, start_col))
    while Q:
        row, col = Q.popleft()
        visited[row][col] = 1
        count += 1
        for di, dj in [[0, 1], [0, -1], [1, 0]]:
            next_row, next_col = row + di, col + dj
            if 0 <= next_row < SIZE and 0 <= next_col < SIZE and matrix[next_row][next_col] != 0 and visited[next_row][next_col] == 0:
                Q.append((next_row, next_col))
                break

    if count < min_path:
        min_path = count
        min_start = max(min_start, start_col)


SIZE = 100
TC = 10
for _ in range(1, TC+1):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(SIZE)]
    min_path = float('inf')
    min_start = 0
    for j in range(SIZE):
        if matrix[0][j] == 1:
            play(0, j)

    print(f"#{t} {min_start}")
