'''
G1 13460 구슬 탈출 2

직사각형 보드에 빨간 구슬, 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼는 게임

보드 세로는 N, 가로는 M. 1x1 칸으로 나누어져 있음
가장 바깥 행과 열은 모두 막혀있고, 보드에는 구멍이 하나 있음.
구슬들은 칸에 딱 알맞은 크기.
파란 구슬이 구멍에 들어가면 안됨

중력을 이용해 구슬을 굴려야하는데, 왼쪽, 오른쪽, 위쪽, 아래쪽으로 기울일 수 있음
각각 동작에서 공은 동시에 움직임. 빨간 구슬이 구멍에 빠지면 성공, 파란 구슬이 빠지면 실패.
동시에 빠져도 실패. 빨간 구슬, 파란 구슬은 동시에 같은 칸에 있지 못함.
기울이는 동작을 그만하는건 더 이상 구슬이 움직이지 않을 때 까지.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 문제
만약 10번 이하로 움직여 빨간 구슬을 못 뺀다면 -1 출력

입력:
N, M : 세로, 가로
N줄 동안 보드의 상태 :
'.' : 빈 칸
'#' : 장애물 or 벽
'O' : 구멍의 위치
'R' : 빨간 구슬 위치
'B' : 파란 구슬 위치
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def reverse_board(board):       # 각 행의 리스트들을 거꾸로 나열한 뒤, 왼쪽으로 기울이고 다시 원래대로 복구하면 보드를 오른쪽으로 기울인 효과 나타냄
    return [list(reversed(i)) for i in board]


def turn_left(board):           # 보드를 왼쪽으로 돌린다음 왼쪽으로 기울이고 다시 오른쪽으로 돌려 복구하면 보드를 위로 기울인 효과
    return list(map(list, list(zip(*list(board[i][::-1] for i in range(len(board)))))))


def turn_right(board):          # 보드를 오른쪽으로 돌리고 왼쪽으로 기울이고 다시 왼쪽으로 돌려 복구하면 보드를 아래로 기울인 효과
    return list(map(list, list(zip(*list(board[::-1][i] for i in range(len(board)))))))


def tilt(board):
    board_copy = [i[:] for i in board]      # 깊은 복사
    
    for i in range(len(board)):
        hole = []                           # 동시에 구멍에 구슬 2개가 들어가면 실패, 빨간색만 들어가면 성공, 파란색만 들어가면 실패
        for j in range(len(board[0])-1):
            if board_copy[i][j] == 'B':     # 파란색 구슬이면,
                move = 0                    # 기울였을 때, 구슬이 몇칸을 굴러가는지 저장할 변수
                not_arrive = True           # 구멍에 도착한지 나타내는 변수
                for k in range(j-1, 0, -1):     # 구슬이 있는 곳부터 왼쪽으로 흘러갈 것이기 때문에 왼쪽으로 탐색
                    if board_copy[i][k] == 'O':     # 구멍이라면, hole 리스트에 파란색 넣고, 파란색 구슬을 배열에서 '.'로 변환해 없애줌.
                        hole.append('blue')
                        board_copy[i][j] = '.'
                        not_arrive = False          # 구멍에 들어갔기 때문에 False로 변환하고 탐색 중지
                        break
                    if board_copy[i][k] in ['#', 'R']:      # 벽이나, 빨간 구슬을 만난다면 탐색 중지
                        break
                    if board_copy[i][k] == '.':             # 빈칸이면 앞으로 나아가야하기때문에 move 변수 1 증가
                        move += 1
                if not_arrive:                              # 만약 아직 도착하지 못해 여전히 not_arive가 True라면, 증가한 move 변수만큼 구슬 이동(이동할 빈칸과 탐색 시작한 구슬의 자리를 바꾸어줌)
                    board_copy[i][j], board_copy[i][j-move] = board_copy[i][j-move], board_copy[i][j]
            
            if board_copy[i][j] == 'R':     # 빨간 구슬일 경우, 파란 구슬의 로직과 동일.
                move = 0
                not_arrive = True
                for k in range(j-1, 0, -1):
                    if board_copy[i][k] == 'O':
                        hole.append('red')
                        board_copy[i][j] = '.'
                        not_arrive = True
                        break
                    if board_copy[i][k] in ['#', 'B']:
                        break
                    if board_copy[i][k] == '.':
                        move += 1
                if not_arrive:
                    board_copy[i][j], board_copy[i][j-move] = board_copy[i][j-move], board_copy[i][j]
            
        if len(hole) == 2:          # 만약 hole에 'blue', 'red' 모두 들어가면 리스트 길이가 2일 것임. 그러면 실패이기 때문에 실패한 경우를 나타내는 2를 반환
            return board_copy, 2
        elif 'blue' in hole:        # blue만 들어있어도 파란색 구슬만 구멍으로 나온것이기 때문에 실패한 경우인 2 반환
            return board_copy, 2
        elif 'red' in hole:         # 만약 red가 들어있으면 성공, 1 반환
            return board_copy, 1
            
    return board_copy, 0        # hole에 아무것도 안들어갔다면, 다음 기울일 방향 정해야하므로, 0 반환

def game(board, p_board, direction, cnt, color):
    global result
    
    if cnt > result:        # 만약 이미 구한 최솟값보다 현재 탐색중인 경우의 수의 탐색 횟수가 크다면 탐색할 필요 없으므로 중단
        return
    
    if cnt > 10:            # 횟수 10회 넘어가도 중단
        return
    
    if color == 1:          # 만약 color 변수가 1이면 성공했다는 뜻. 최솟값 구하기
        result = min(result, cnt)
        return

    if color == 2:          # color 변수가 2라면 구슬 2개 한번에 들어갔거나, 파란구슬이 들어갔다는 뜻. 즉, 실패! 변화없이 중단
        return
    
    if cnt != 0 and board == p_board:       # 만약 이전 보드의 상태와 달라진 게 없다면, 중단(이유는 기울인 횟수의 최솟값을 구해야하는데 구슬이 움직이지 않았다면, 최솟값이 무조건 될 수가 없음)
        return
    
    board_copy = [i[:] for i in board]
    
    if direction == 'L':                    # 왼쪽으로 기울일때는 보드 상태 변환없이 기울이기
        new_board, color = tilt(board_copy)
    elif direction == 'R':                  # 오른쪽 기울이기
        new_board, color = tilt(reverse_board(board_copy))
        new_board = reverse_board(new_board)        # 다시 원래 보드의 방향으로 되돌리기
    elif direction == 'U':                  # 위로 기울이기
        new_board, color = tilt(turn_left(board_copy))
        new_board = turn_right(new_board)           # 왼쪽으로 돌렸다가 기울이고, 오른쪽으로 다시 돌려 방향 복구
    elif direction == 'D':                  # 아래로 기울이기
        new_board, color = tilt(turn_right(board_copy))
        new_board = turn_left(new_board)            # 오른쪽으로 돌렸다가 기울이고, 왼쪽으로 다시 돌려 방향 복구
    
    game(new_board, board_copy, 'L', cnt + 1, color)        # 재귀. 각기 다른 방향들로 탐색
    game(new_board, board_copy, 'R', cnt + 1, color)
    game(new_board, board_copy, 'U', cnt + 1, color)
    game(new_board, board_copy, 'D', cnt + 1, color)

    
N, M = map(int, input().split())
main_board = [list(input()) for _ in range(N)]
result = float('inf')           # 최솟값 구해야 하므로

game(main_board, main_board, 'L', 0, 0)
game(main_board, main_board, 'R', 0, 0)
game(main_board, main_board, 'U', 0, 0)
game(main_board, main_board, 'D', 0, 0)

if result == float('inf'):      # 만약 최솟값 비교를 한번도 시도하지 못했다면, 모두 실패하거나, 불가능한 보드 상태임. -1 출력
    print(-1)
else:  
    print(result)