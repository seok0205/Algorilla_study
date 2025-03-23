from collections import deque


def find_group(row, col):
    Q = deque()

    Q.append((row, col))
    visited[row][col] = True
    num = 0

    while Q:
        curr_row, curr_col = Q.popleft()

        num += 1

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            next_row, next_col = curr_row + di, curr_col + dj
            if 0 <= next_row < N and 0 <= next_col < N and not visited[next_row][next_col] and matrix[next_row][next_col] == 1:
                Q.append((next_row, next_col))
                visited[next_row][next_col] = True

    return num


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
nums = []
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1 and not visited[row][col]:
            num = find_group(row, col)
            nums.append(num)
nums.sort()
print(len(nums))
for num in nums:
    print(num)
