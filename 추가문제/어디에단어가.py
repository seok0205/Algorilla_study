T = int(input())

for test_case in range(1, T+1):
    # N: 퍼즐의 가로, 세로 길이
    # K: 단어의 길이
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0

    # 행
    for i in range(N):
        cnt_row = 0     # 각 행에서 연속된 1의 개수
        for j in range(N):
            # arr[i][j]가 1이면 cnt_row + 1
            if arr[i][j] == 1:  
                cnt_row += 1    

            # arr[i][j]가 0일 때
            if arr[i][j] == 0:
                # cnt_row가 K이면(= 연속한 1의 개수가 K개 이면) cnt + 1
                if cnt_row == K:    
                    cnt += 1
                # 다시 cnt_row 0으로 초기화
                cnt_row = 0

        # 1으로 끝날 때를 고려해서 행이 끝날 때에도 한번 더 확인 
        if cnt_row == K:
            cnt += 1

    # 열
    for i in range(N):
        cnt_column = 0  # 각 열에서 연속된 1의 개수
        for j in range(N):
            # arr[j][i]가 1이면 cnt_column + 1
            if arr[j][i] == 1:
                cnt_column += 1

            # arr[j][i]가 0일 때
            if arr[j][i] == 0:
                # cnt_column이 K이면(= 연속한 1의 개수가 K개 이면) cnt + 1
                if cnt_column == K:
                    cnt += 1
                # 다시 cnt_col 0으로 초기화
                cnt_column = 0

        # 1으로 끝날 때를 고려해서 열이 끝날 때에도 한번 더 확인 
        if cnt_column == K:
            cnt += 1
            
    print(f'#{test_case} {cnt}')
