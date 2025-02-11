T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 우-우하-하-하좌-좌-좌상-상-상우
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    candidates = 0

    for i in range(N):
        for j in range(M):
            curr_r, curr_c = i, j
            count = 0
            for di, dj in directions:
                next_r, next_c = i + di, j + dj
                if 0 <= next_r < N and 0 <= next_c < M and matrix[next_r][next_c] < matrix[curr_r][curr_c]:
                    count += 1
            if count >= 4:
                candidates += 1

    print(f"#{t} {candidates}")
