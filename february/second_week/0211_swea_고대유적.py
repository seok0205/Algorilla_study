T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_len_building = 0

    for i in range(N):
        len_building_row = 0
        for j in range(M):
            if matrix[i][j] == 1:
                len_building_row += matrix[i][j]
            else:
                if len_building_row > max_len_building:
                    max_len_building = len_building_row
                len_building_row = 0
        if len_building_row > max_len_building:
            max_len_building = len_building_row

    for i in range(M):
        len_building_col = 0
        for j in range(N):
            if matrix[j][i] == 1:
                len_building_col += matrix[j][i]
            else:
                if len_building_col > max_len_building:
                    max_len_building = len_building_col
                len_building_col = 0
        if len_building_col > max_len_building:
            max_len_building = len_building_col

    print(f"#{t} {max_len_building}")