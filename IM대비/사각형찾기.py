# 사각형중 가로 세로 곱이 가장 큰 걸 출력
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    score = 0
    # 우 하
    dr = [0, -1]
    dc = [1, 0]
    for i in range(N):
        for j in range(N):
            temp = {'row' : 1, 'col' : 1}
            if arr[i][j] == 1:
                nr = i + dr[0]
                nc = j + dc[0]
                while 0<=nr<N and 0<=nc<N and arr[nr][nc] == 1:
                    nr += dr[0]
                    nc += dc[0]
                    temp['row'] += 1

                nr = i + dr[1]
                nc = j + dc[1]
                while 0<=nr<N and 0<=nc<N and arr[nr][nc] == 1:
                    nr += dr[1]
                    nc += dc[1]
                    temp['col'] += 1

            if temp['row'] * temp['col'] > score:
                score = temp['row'] * temp['col']
        
    print(temp)
    print(score)
    print(f'#{t} {score}')
                    