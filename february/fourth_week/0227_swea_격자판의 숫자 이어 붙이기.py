def dfs(r, c, numbers):
    if len(numbers) == 7:
        result.add(numbers)
        return

    numbers += str(grid[r][c])

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        next_r = r + di
        next_c = c + dj
        if 0 <= next_r < 4 and 0 <= next_c < 4:
            dfs(next_r, next_c, numbers)

T = int(input())
for t in range(1, T + 1):

    grid = [list(map(int, input().split())) for _ in range(4)]

    result = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, '')

    print(f"#{t} {len(result)}")
