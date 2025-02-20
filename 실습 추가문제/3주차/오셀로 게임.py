def black(i, j, board, N):
    # 본인 자리 흑으로 변경
    board[i][j] = 1
    # 위부터 시계방향
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    for k in range(8):
        nr, nc = i + dr[k], j + dc[k]
        # 백이 있는 인덱스 저장
        temp = []
        # 델타 탐색 돌아서 만약 백이 나오면 
        # 흑이 얼마나 있는지 확인
        while 0<=nr<N and 0<=nc<N and board[nr][nc] == 2:
            temp.append([nr, nc])
            nr += dr[k]
            nc += dc[k]
        # 만약 다음 칸에 흑이 있으면 둘려싸인 것이므로
        # 사이의 백들을 흑으로 변경
        if 0<=nr<N and 0<=nc<N and board[nr][nc] == 1:
            for a, b in temp:
                board[a][b] = 1
  
def white(i, j, board, N):
    board[i][j] = 2
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    for k in range(8):
        nr, nc = i + dr[k], j + dc[k]
        temp = []
        while 0<=nr<N and 0<=nc<N and board[nr][nc] == 1:
            temp.append([nr, nc])
            nr += dr[k]
            nc += dc[k]
        if 0<=nr<N and 0<=nc<N and board[nr][nc] == 2:
            for x, y in temp:
                board[x][y] = 2

T = int(input())
for t in range(1, T+1):
    # N : 보드의 크기(4or6or8), M : 돌을 놓는 횟수
    N, M = map(int, input().split())
    # 돌을 놓는 좌표 / 1 : 흑, 2 : 백
    arr = [list(map(int, input().split())) for _ in range(M)]
    # 우선 초기 상태의 보드을 만들어 보자
    board = [[0]*N for _ in range(N)]
    # 가운데에 초기의 흑과 백 배치
    board[N//2-1][N//2-1], board[N//2][N//2] = 2, 2
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1

    for i in range(M):
        x, y, color = arr[i]
        # 좌표평면에서 1부터 시작이므로 모든 좌표에서 1빼서 받아준다.
        x -= 1
        y -= 1
        if color == 1:
            black(x, y, board, N)
        else:
            white(x, y, board, N)
    
    count_b = 0
    count_w = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count_b += 1
            elif board[i][j] == 2:
                count_w += 1
    
    print(f'#{t}', count_b, count_w)
