T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_of_sums = 0
    for i in range(N):
        for j in range(M):
            sum_of_confetti = matrix[i][j]
            # curr_value = matrix[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                # for c in range(1, curr_value+1):
                #     next_r = i + di*c
                next_r = i + di
                    # next_c = j + dj*c
                next_c = j + dj
                if 0 <= next_r < N and 0 <= next_c < M:
                    sum_of_confetti += matrix[next_r][next_c]
            if sum_of_confetti > max_of_sums:
                max_of_sums = sum_of_confetti
    print(f"#{t} {max_of_sums}")