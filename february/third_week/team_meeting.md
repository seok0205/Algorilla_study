## 🎯 상호의 배틀필드
```python
def find_start():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if game_map[i][j] == '^' or game_map[i][j] == 'v' or game_map[i][j] == '<' or game_map[i][j] == '>':
                return i, j
 
 
def move(curr_r, curr_c, move_idx):
    if moves[move_idx] == 'U':
        # 게임판 안에서 움직이고 다음 칸으로 이동이 가능하다면 이동+방향전환 그렇지 않으면 방향전환만
        return (curr_r - 1, curr_c, '^') if 0 <= curr_r - 1 < HEIGHT and game_map[curr_r - 1][curr_c] == '.' else '^' 
    elif moves[move_idx] == 'D':
        return (curr_r + 1, curr_c, 'v') if 0 <= curr_r + 1 < HEIGHT and game_map[curr_r + 1][curr_c] == '.' else 'v'
    elif moves[move_idx] == 'L':
        return (curr_r, curr_c - 1, '<') if 0 <= curr_c - 1 < WIDTH and game_map[curr_r][curr_c - 1] == '.' else '<'
    elif moves[move_idx] == 'R':
        return (curr_r, curr_c + 1, '>') if 0 <= curr_c + 1 < WIDTH and game_map[curr_r][curr_c + 1] == '.' else '>'
    elif moves[move_idx] == 'S':
        return 'shoot'
 
 
def shoot(curr_r, curr_c):
    if game_map[curr_r][curr_c] == '^':
        d = 1
        while 0 <= curr_r - d < HEIGHT: # 맵 안에 있을 때
            if game_map[curr_r - d][curr_c] == '*': # 벽돌 벽이면
                game_map[curr_r - d][curr_c] = '.' # 평지로 업데이트
                break
            elif game_map[curr_r - d][curr_c] == '#': # 강철 벽이면 따로 변경 사항 없음
                break
            else:
                d += 1 # 벽을 만날 때까지 포탄은 계속 되므로 d를 1씩 증가
    elif game_map[curr_r][curr_c] == 'v':
        d = 1
        while 0 <= curr_r + d < HEIGHT:
            if game_map[curr_r + d][curr_c] == '*':
                game_map[curr_r + d][curr_c] = '.'
                break
            elif game_map[curr_r + d][curr_c] == '#':
                break
            else:
                d += 1
    elif game_map[curr_r][curr_c] == '<':
        d = 1
        while 0 <= curr_c - d < WIDTH:
            if game_map[curr_r][curr_c - d] == '*':
                game_map[curr_r][curr_c - d] = '.'
                break
            elif game_map[curr_r][curr_c - d] == '#':
                break
            else:
                d += 1
    elif game_map[curr_r][curr_c] == '>':
        d = 1
        while 0 <= curr_c + d < WIDTH:
            if game_map[curr_r][curr_c + d] == '*':
                game_map[curr_r][curr_c + d] = '.'
                break
            elif game_map[curr_r][curr_c + d] == '#':
                break
            else:
                d += 1
 
 
T = int(input())
for t in range(1, T + 1):
    HEIGHT, WIDTH = map(int, input().split())
    game_map = [list(input()) for _ in range(HEIGHT)]
    num_of_inputs = int(input())
    moves = list(input())
 
    # 포탄발사 - 벽돌(*) 강철(#) 벽에서 멈추거나 계속 직진
    # 벽돌 벽에 부딪히면 포탄 소멸되고 그 칸은 평지가 됨
    # 강철 벽에 부딪히면 아무일도 일어나지 않음
    start_r, start_c = find_start()
    moves_idx = 0
    while moves_idx < num_of_inputs: # 명령이 끝날 때까지 진행
        command = move(start_r, start_c, moves_idx) # 명령이 어떤 것인지 확인
        if command == 'shoot': # 명령이 포탄발사라면 발사
            shoot(start_r, start_c)
        elif len(command) == 1: # 명령이 이동하는 것인데 다음칸으로 이동을 못할 경우 기존 칸에서 방향만 업데이트
            game_map[start_r][start_c] = command
        else: # 명령이 이동하는 것이고 다음칸으로 이동도 가능할 경우 
            next_r, next_c, next_move = command
            game_map[next_r][next_c] = next_move # 다음 칸에 요구된 방향으로 업데이트
            game_map[start_r][start_c] = '.' # 기존 칸은 평지로 업데이트
            start_r, start_c = next_r, next_c # 다음 칸을 기존 칸으로 업데이트하고 무브 인덱스도 1 증가시키기
        moves_idx += 1
 
    print(f"#{t}", end=" ")
    for row in game_map:
        print(''.join(row))
```