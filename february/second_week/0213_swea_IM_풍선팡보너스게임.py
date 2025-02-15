T = int(input())
for t in range(1, T+1):

    N = int(input())
    matrix =[list(map(int, input().split())) for _ in range(N)]

    rows_sum_arr = [sum(row) for row in matrix]
    cols_sum_arr = [0 for _ in range(N)]
    for i in range(N):
        col_sum = 0
        for j in range(N):
            col_sum += matrix[j][i]
        cols_sum_arr[i] = col_sum

    max_sum = 0
    min_sum = rows_sum_arr[0] + cols_sum_arr[0]

    curr_sum = 0
    for i in range(N):
        for j in range(N):
            curr = matrix[i][j]
            curr_sum = rows_sum_arr[i] + cols_sum_arr[j] - curr
            max_sum = max(max_sum, curr_sum)
            min_sum = min(min_sum, curr_sum)

    print(f"#{t} {max_sum - min_sum}")