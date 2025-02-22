def battle(board, order, H, W, N):
    # 시작점 찾기
    i, j = find_start(board, H, W)
    
    for k in range(N):
        # 위로가는 명령이 나오면 위 칸이 범위를 벗어나지 않고
        # 평지이면 이동, 다른 것이면 방향만 바꿔준다.
        if order[k] == 'U':
            if i > 0 and board[i-1][j] == '.':
                up(i, j, board)
                i -= 1
            else:
                board[i][j] = '^'
        elif order[k] == 'D':
            if i < H-1 and board[i+1][j] == '.':
                down(i, j, board)
                i += 1
            else:
                board[i][j] = 'v'
        elif order[k] == 'L':
            if j > 0 and board[i][j-1] == '.':
                left(i, j, board)
                j -= 1
            else:
                board[i][j] = '<'
        elif order[k] == 'R':
            if j < W-1 and board[i][j+1] == '.':
                right(i, j, board)
                j += 1
            else:
                board[i][j] = '>'
        else:
            shoot(i, j, board, H, W)
            

def find_start(board, H, W):
    for i in range(H):
        for j in range(W):
            if board[i][j] in ['^', 'v', '<', '>']:
                return i, j

def up(i, j, board):
    board[i][j] = '.'
    board[i-1][j] = '^'

def down(i, j, board):
    board[i][j] = '.'
    board[i+1][j] = 'v'

def left(i, j, board):
    board[i][j] = '.'
    board[i][j-1] = '<'

def right(i, j, board):
    board[i][j] = '.'
    board[i][j+1] = '>'

def shoot(i, j, board, H, W):
    # 강철벽 만나면 멈추고 벽돌벽은 평지로 바꾸고 멈춤
    if board[i][j] == '^':
        nr = i - 1
        while nr >= 0:
            if board[nr][j] == '#':
                break
            elif board[nr][j] == '*':
                board[nr][j] = '.'
                break
            nr -= 1
    elif board[i][j] == 'v':
        nr = i + 1
        while nr < H:
            if board[nr][j] == '#':
                break
            elif board[nr][j] == '*':
                board[nr][j] = '.'
                break
            nr += 1
    elif board[i][j] == '<':
        nc = j - 1
        while nc >= 0:
            if board[i][nc] == '#':
                break
            elif board[i][nc] == '*':
                board[i][nc] = '.'
                break
            nc -= 1
    elif board[i][j] == '>':
        nc = j + 1
        while nc < W:
            if board[i][nc] == '#':
                break
            elif board[i][nc] == '*':
                board[i][nc] = '.'
                break
            nc += 1

T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    order = list(input())
    
    battle(board, order, H, W, N)

    print(f'#{t}', end=' ')
    for row in board:
        print(''.join(row))
