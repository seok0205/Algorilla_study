# N x N 퍼즐이 주어지는에 K의 길이를 갖는 단어가 들어갈
# 자리의 수를 출력하는 프로그램을 만들어라
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())      # N : 행렬의 크기  K : 단어의 길이
    # 글자를 입력 가능한 부분은 1
    # 아닌 부분은 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            c = arr[i][j]    #  현재 위치의 값
            if c == 1:
                # 행의 시작점 이거나 그 전의 행의 값이 0이면
                if i == 0 or arr[i-1][j] == 0:               
                    # 현재 위치에서 아래로 탐색해 나가며 sub_count를 늘려주고
                    # 더한 값이 조건과 일치하면 count를 늘려준다.
                    sub_count1 = 0    
                    for k in range(K-1):
                        # 현재 행의 인덱스에 range(K-1)만큼 더해가며
                        # 내가 원하는 글자의 길이인지 탐색
                        ni = i + (k+1)   # 현재위치에서 아래로 탐색
                        # 아래의 값이 1이거나 행렬의 범위를 벗어나지 않으면 if문 실행
                        if 0<=ni<N:
                            if arr[ni][j] == 1:
                                sub_count1 += 1
                        else:
                            break
                    # 끝부분 체크 : 끝부분이 행의 끝이거나 끝부분 바로 뒤의 값이 0이면 실행
                    if sub_count1 == K-1 and (i+K == N or arr[i+K][j] ==0):
                        count += 1
 
 
                if j == 0 or arr[i][j-1] == 0:
                    sub_count2 = 0
                    # 현재위치에서 오른쪽으로 탐색
                    for q in range(K-1):
                        nj = j + (q+1)
                        if 0<=nj<N:
                            if arr[i][nj] == 1:
                                sub_count2 += 1
                        else:
                            break
                    if sub_count2 == K-1 and (j+K == N or arr[i][j+K]==0):
                        count += 1
 
    print(f'#{t} {count}')