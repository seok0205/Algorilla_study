'''
D3 4615 재미있는 오셀로 게임

오셀로는 흑돌, 백돌 가진 사람이 번갈아가며 보드에 돌을 놓아 최종적으로
자신의 돌이 많은 사람이 이기는 게임

보드는 4x4, 6x6, 8x8 판이 존재
중앙에 4개의 돌을 놓고 시작하는데 흑돌, 백돌이 각각 2개씩, 대각선으로 마주본 형태로 놓고 시작

자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그곳에 돌을 놓을 수 있음

그 때, 상대편의 돌은 자신의 돌이 됨(가로, 세로, 대각선 가능)
돌이 놓을 곳이 없으면 상대편 플레이어가 다시 돌을 놓음

보드에 빈 곳이 없거나 양플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝남.
보드에 자신의 색의 돌이 많으면 승리, 그렇지 않으면 패배

입력:
N : 4, 6, 8 중 하나, M : 플레이어가 돌을 놓는 횟수
M줄 동안 돌을 놓을 위치와 돌의 색이 주어짐
돌색이 1은 흑, 2는 백
3 2 1이 입력되면 3, 2 좌표에 흑돌이 놓아진다는 뜻
돌 못놓는 곳은 입력으로 주어지지 않음

출력:
최종 흑돌 개수, 최종 백돌 개수
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int ,input().split())
    
    board = [[0] * N for _ in range(N)]     # 보드생성
    for i in range(2):                      # 시작시 중앙에 하얀돌, 검은돌 각각 서로 대각선 마주보는 형태로 시작
        board[N//2-i][N//2-i] = 2
        board[N//2-1+i][N//2-i] = 1
        
    di = [0, 0, 1, -1, 1, -1, 1, -1]        # 델타 좌표, 상하좌우 및 대각선
    dj = [1, -1, 0, 0, 1, -1, -1, 1]
    
    for _ in range(M):
        info = list(map(int, input().split()))  # 돌하나 둘때마다 보드상태 변환
        
        x = info[1] - 1
        y = info[0] - 1

        board[x][y] = info[2]       # 해당 좌표에 돌을 둠
        
        for i in range(8):          # 8방향 모두 탐색
            idx = 0
            need_change = []        # 바꿔야 할 돌 좌표
            while True:
                idx += 1            # 다른색의 돌 탐색 성공시마다 1칸씩 증가
                mx = x + di[i] * idx
                my = y + dj[i] * idx
                if 0 <= mx < N and 0 <= my < N and board[mx][my] not in [0, info[2]]:       # 만약 보드 안이고, 0과 같은 색의 돌 아니라면
                        need_change.append((mx, my))                                        # 바꿔야할 돌 좌표리스트에 추가
                elif need_change and 0 <= mx < N and 0 <= my < N and board[mx][my] == 0:    # 만약 바꿔야할 돌들이 있는데 갑자기 빈곳이 출현하면,
                    need_change.clear()                                                     # 이전돌들은 못 바꾸므로 리스트 초기화
                    break                                                                   # 더이상 해당 방향은 찾을 필요 X
                elif need_change and 0 > mx or N <= mx or 0 > my or N <= my:                # 0을 만날때와 마찬가지로 보드 밖을 마주해도 리스트 초기화 후 해당 방향 탐색 종료
                    need_change.clear()
                    break
                else:
                    break
                
            for j, k in need_change:        # 리스트에 담긴 돌들을 같은 색의 돌로 변환
                board[j][k] = info[2]
                
        white = 0   # 최종 백, 흑돌 수 구하기
        black = 0
        
        for i in range(N):
            white += board[i].count(2)
            black += board[i].count(1)
            
    print(f'#{tc} {black} {white}')