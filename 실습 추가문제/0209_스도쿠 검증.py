# 올바른 스도쿠인지 검증
T = int(input())
for t in range(1, T+1):
    # 9 X 9 2차원 배열
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 먼저 가로 줄과 세로줄 먼저 확인
    result = 0
    count = 0      # 모든 케이스 통과시 count == 3*9=27이 되어야됨
    for i in range(9):
        sum_wid = 0                # 가로의 합
        sum_ver = 0                # 세로의 합
        for j in range(9):
            sum_wid += arr[i][j]    # 행은 고정 -> 열의 합
            sum_ver += arr[j][i]    # 열은 고정 -> 행의 합
            if sum_wid == 45:
                count += 1
            if sum_ver == 45:
                count += 1

    # 격자로 9칸 확인
    for i in range(3):
        for j in range(3):
            sum_ar = 0             
            ni = (3*i)                # 각 격자 칸의 첫번째 인덱스
            nj = (3*j)
            for p in range(3):
                for q in range(3):    # 첫 인덱스로 부터 오른쪽, 왼쪽으로
                    ar_i = ni + p     # 각 2칸씩 더 뻗어서 값들을 더해줌
                    ar_j = nj + q
                    sum_ar += arr[ar_i][ar_j]
            if sum_ar == 45:
                count += 1
    if count == 27:     # 모든 경우 만족시 결과값 1 출력
        result = 1

    print(f'#{t} {result}')

