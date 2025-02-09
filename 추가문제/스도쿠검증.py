T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    
    cnt = 0

    # 1. 행 검증
    for i in range(9):
        row_cnt = [0]*10    # 행 - 숫자 등장 횟수 카운트
        for j in range(9):
            row_cnt[arr[i][j]] += 1

        if row_cnt[1:10].count(1) == 9:
            cnt += 1

    # 2. 열 검증
    for i in range(9):
        col_cnt = [0]*10    # 열 - 숫자 등장 횟수 카운트
        for j in range(9):
            col_cnt[arr[j][i]] += 1

        if col_cnt[1:10].count(1) == 9:
            cnt += 1

    #3. 3*3 검증
    for box_x in range(0,9,3):
        for box_y in range(0,9,3):
            box_cnt = [0]*10    # 3*3 박스 - 숫자 등장 횟수 카운트
            for i in range(3):
                 for j in range(3):
                    box_cnt[arr[box_x+i][box_y+j]] += 1

            if box_cnt[1:10].count(1) ==9:
                cnt += 1

    result = 0

    if cnt == 27:
        result = 1
    else:
        result = 0

    print(f'#{test_case} {result}')