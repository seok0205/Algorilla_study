def f(arr):
    # 완전탐색으로 검색
    # 해당칸의 오른쪽, 아래, 왼쪽아래, 오른쪽아래 대각선만 탐색
    # 우, 하, 좌하, 우하
    # 5개 이상 연속한 부분이 있으면 'YES'출력
    dr = [0, 1, 1, 1]
    dc = [1, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # 본인자리 count
                    count = 1
                    while  0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        count += 1
                        # 다음 탐색에서 배열을 벗어나지 않고  
                        # o가 5개가 나오면 정답
                        if count == 5:
                            return 'YES'
                        # 5개가 안나오면 nr,nc를 계속 늘려주면서 탐색
                        nr += dr[k]
                        nc += dc[k]
    return 'NO'
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = f(arr)
    print(f'#{t} {result}')