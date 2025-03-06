
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 보드 한 변의 길이 / M: 돌 놓는 횟수
    # 좌표 col, row (1부터 시작) 와 돌색깔 (1: 흑돌 / 2: 백돌)
    tasks = [list(map(int, input().split())) for _ in range(M)]

    board = [[0 for _ in range(N)] for _ in range(N)]
    center = N // 2
    board[center][center] = board[center - 1][center - 1] = 2
    board[center][center - 1] = board[center - 1][center] = 1

    for col, row, color in tasks:
        curr_r = row - 1
        curr_c = col - 1
        board[curr_r][curr_c] = color
        for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            next_r = curr_r + di
            next_c = curr_c + dj
            stack = []
            while 0 <= next_r < N and 0 <= next_c < N and board[next_r][next_c] != 0 and board[next_r][next_c] != color:
                stack.append((next_r, next_c))
                next_r += di
                next_c += dj

            if 0 <= next_r < N and 0 <= next_c < N and board[next_r][next_c] == color:
                for entry_r, entry_c in stack:
                    board[entry_r][entry_c] = color

    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f"#{t} {black} {white}")
