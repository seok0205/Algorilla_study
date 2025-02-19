T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    answer = "NO"

    # 우하-하좌-좌상-상우
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    # d = 0
    counts_right = 0
    counts_left = 0

    i = 0
    j = 0
    while True:
        if matrix[i][j] == 'o':
            counts += 1
        for d in range(len(dr)):
            nr = i + dr[d]
            nc = j + dc[d]
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 'o':
                i = nr
                j = nc
                break
        else:
            j += 1
            if j >= N - 1:
                j = 0
                i += 1

    print(f"#{t} {answer}")
