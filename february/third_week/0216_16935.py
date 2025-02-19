# 16935. 배열 돌리기 3

def type1(matrix, N, M):
    return matrix[::-1]

def type2(matrix, N, M):
    return [row[::-1] for row in matrix]

def type3(matrix, N, M):
    return [[matrix[N-1-j][i] for j in range(N)] for i in range(M)]

def type4(matrix, N, M):
    return [[matrix[j][M-1-i] for j in range(N)] for i in range(M)]

def type5(matrix, N, M):
    new_matrix = []
    sub_row_size = N//2
    sub_col_size = M//2
    first = []
    second = []
    third = []
    fourth = []
    i = 0
    while i < sub_row_size:
        first.append(matrix[i][:sub_col_size])
        second.append(matrix[i][sub_col_size:])
        third.append(matrix[i+sub_row_size][sub_col_size:])
        fourth.append(matrix[i+sub_row_size][:sub_col_size])
        i += 1

    j = 0
    while j < sub_row_size:
        fourth[j].extend(first[j])
        third[j].extend(second[j])
        j += 1

    for fourth_row in fourth:
        new_matrix.append(fourth_row)
    for third_row in third:
        new_matrix.append(third_row)

    return new_matrix

def type6(matrix, N, M):
    new_matrix = []
    sub_row_size = N//2
    sub_col_size = M//2
    first = []
    second = []
    third = []
    fourth = []
    i = 0
    while i < sub_row_size:
        first.append(matrix[i][:sub_col_size])
        second.append(matrix[i][sub_col_size:])
        third.append(matrix[i+sub_row_size][sub_col_size:])
        fourth.append(matrix[i+sub_row_size][:sub_col_size])
        i += 1

    j = 0
    while j < sub_row_size:
        second[j].extend(third[j])
        first[j].extend(fourth[j])
        j += 1

    for second_row in second:
        new_matrix.append(second_row)
    for first_row in first:
        new_matrix.append(first_row)

    return new_matrix


N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
type_of_calc = list(map(int, input().split()))

for t in range(R):
    if type_of_calc[t] == 1:
        matrix = type1(matrix, N, M)

    elif type_of_calc[t] == 2:
        matrix = type2(matrix, N, M)

    elif type_of_calc[t] == 3:
        matrix = type3(matrix, N, M)
        N, M = M, N

    elif type_of_calc[t] == 4:
        matrix = type4(matrix, N, M)
        N, M = M, N

    elif type_of_calc[t] == 5:
        matrix = type5(matrix, N, M)

    elif type_of_calc[t] == 6:
        matrix = type6(matrix, N, M)

for row in matrix:
    print(*row)