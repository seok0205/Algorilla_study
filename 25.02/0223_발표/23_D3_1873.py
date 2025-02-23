'''
D3 1873 상호의 배틀필드

문자	의미
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

다음 표는 사용자가 넣을 수 있는 입력의 종류를 나타낸다.
 
문자	동작
U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

전차 이동시 게임 밖이면 이동 X
포탄 발사 시, 포탄은 벽돌이나 강철로 만들어진 벽에 충돌하거나 맵 밖으로 갈때까지 직진

포탄이 벽에 충돌하면 포탄은 소멸, 부딪힌 벽이 벽돌이라면 파괴 후 평지 변환
강철로 만들어진 벽에 포탄이 부딪히면 아무일도 안 일어남

맵밖으로 포탄이 이동 시 아무일도 안 일어남
초기맵 상태 및 사용자 입력이 주어질 때, 최종 게임 맵의 상태를 구하는 문제
'''


def shoot(mobile, field):
    '''
    mobile : 탱크의 현재 상태 (바라보는 방향, i좌표, j좌표)
    field : 이 함수를 실행하기 전 지도의 상태. 이 것을 포탄 발사한 뒤의 지도를 반환
    '''
    move_dic = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}     # 이동 방향 딕셔너리
    
    direction = move_dic[mobile[0]]
    idx = 0

    x = mobile[1]   # 전차가 현재 존재하는 위치에서 포탄 발사하므로 전차의 위치가 포탄의 출발 지점
    y = mobile[2]
    while True:     # move_dic 딕셔너리 활용. 포탄은 쭉 날라가면서 어디까지 갈지 모름. 따라서 while 사용
        idx += 1
        mx = x + direction[0] * idx     # 한칸씩 늘려가면서 탐색
        my = y + direction[1] * idx
        if 0 <= mx < H and 0 <= my < W and field[mx][my] == "*":        # 벽돌로 지어진 벽 만나면 파괴
            field[mx][my] = "."
            break
        elif 0 <= mx < H and 0 <= my < W and field[mx][my] == "#":      # 강철 벽 만나면 부수지 못함
            break
        elif 0 > mx or mx >= H or 0 > my or my >= W:                    # 맵 밖으로 나가면 종료
            break
    
    return field        # 포탄이 발사된 뒤의 지도상태 반환


def move(mobile, c):
    '''
    mobile : 탱크의 현재 상태(바라보는 방향, i좌표, j좌표)
    c : 입력받은 이동문자(UDLR)
    '''
    x = mobile[1]       # 현재 탱크의 위치 좌표
    y = mobile[2]
    if c == 'U':        # UP
        mobile[0] = '^'     # mobile의 바라보는 방향 설정
        if 0 <= x-1 < H and 0 <= y < W and battle_field[x-1][y] not in '-*#':       # 가려는 방향이 맵 안이거나 장애물이 존재하지 않으면 해당 방향 1칸 직진
            battle_field[x][y] = '.'                                                # 기존 위치는 평지로 변경
            mobile[1] = x - 1                                                       # mobile(tank)의 좌표를 방향에 따라 변경해줌
            battle_field[mobile[1]][mobile[2]] = mobile[0]                          # 전진한 위치에 탱크로 변경
        else:                                                                       # 만약 움직일 수 없다면
            battle_field[x][y] = mobile[0]                                          # 원래의 위치에서 방향만 바꿔줌
    elif c == 'D':
        mobile[0] = 'v'
        if 0 <= x+1 < H and 0 <= y < W and battle_field[x+1][y] not in '-*#':
            battle_field[x][y] = '.'
            mobile[1] = x + 1
            battle_field[mobile[1]][mobile[2]] = mobile[0]
        else:
            battle_field[x][y] = mobile[0]
    elif c == 'L':
        mobile[0] = '<'
        if 0 <= x < H and 0 <= y-1 < W and battle_field[x][y-1] not in '-*#':
            battle_field[x][y] = '.'
            mobile[2] = y - 1
            battle_field[mobile[1]][mobile[2]] = mobile[0]
        else:
            battle_field[x][y] = mobile[0]
    elif c == 'R':
        mobile[0] = '>'
        if 0 <= x < H and 0 <= y+1 < W and battle_field[x][y+1] not in '-*#':
            battle_field[x][y] = '.'
            mobile[2] = y + 1
            battle_field[mobile[1]][mobile[2]] = mobile[0]
        else:
            battle_field[x][y] = mobile[0]
    
    return mobile


T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    battle_field = [list(input()) for _ in range(H)]
    N = int(input())
    command = input()

    for i in range(H):      # 탱크의 첫 위치 및 상태 탐색
        for j in range(W):
            if battle_field[i][j] in "><v^":
                tank = [battle_field[i][j], i, j]
                
    for i in command:       # 커맨드 읽어가며 맵 상태 변환
        if i == 'S':
            battle_field = shoot(tank, battle_field)
        elif i in "UDLR":
            tank = move(tank, i)    
    
    for i in range(H):      # 출력
        if i == 0:
            print(f'#{tc} {"".join(battle_field[i])}')
        else:
            print(f'{"".join(battle_field[i])}')
    