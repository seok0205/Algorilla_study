'''
G4 14499 주사위 굴리기

NxM 크기 지도 존재. 지도의 오른쪽은 동쪽, 위쪽은 북쪽. 주사위 하나 존재.
주사위의 전개도는 

    2
4   1   3
    5
    6

이다. 지도의 좌표는 (r, c)로 나타내며 r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수

주사위는 지도 위에 윗면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y)임.
가장 처음에 주사위에는 모든 면에 0이 적혀져 있음.

지도의 각 칸에는 정수가 하나씩 쓰여져 있음. 주사위를 굴렸을 때, 이동한 칸에 쓰여있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사됨.
0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 됨.

주사위를 놓는 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때마다 상단에 쓰여 있는 값을 구하는 문제

주사위는 지도 바깥으로 이동 불가, 만약 이동시키려하면 해당 명령 무시, 출력도 하면 안됨.

입력 :
N, M, x, y, K : 세로, 가로, 주사위 놓은 곳 좌표 (x, y), 명령 개수
N개의 줄에 지도에 쓰인 수가 북쪽부터 남쪽으로, 각 줄은 서부터 동 순서대로 주어짐
주사위를 놓은 칸에 쓰인 수는 항상 0.
지도의 각 칸에 쓰인 수는 10 미만의 자연수
마지막 줄은 이동하는 명령 순서. 1, 2, 3, 4 : 동 서 북 남

출력 :
이동시 마다 주사위의 윗 면에 쓰인 수를 출력. 바깥이동 명령은 무시, 출력 X.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def east(x, y):     # 동쪽 굴렸을 때 주사위 변동, func는 지도와의 상호작용.
    a, b, c, d = dice[0], dice[2], dice[3], dice[4]
    dice[0], dice[2], dice[3], dice[4] = d, a, b, c
    func(x, y)
    

def west(x, y):     # 서쪽
    a, b, c, d = dice[0], dice[2], dice[3], dice[4]
    dice[0], dice[2], dice[3], dice[4] = b, c, d, a
    func(x, y)


def north(x, y):    # 북쪽
    a, b, c, d = dice[0], dice[1], dice[3], dice[5]
    dice[0], dice[1], dice[3], dice[5] = b, c, d, a
    func(x, y)


def south(x, y):    # 남쪽
    a, b, c, d = dice[0], dice[1], dice[3], dice[5]
    dice[0], dice[1], dice[3], dice[5] = d, a, b, c
    func(x, y)


def func(x, y):     # 주사위가 도착한 지도상의 값이 0이면 맵에 주사위 바닥의 값 복사
    if dice_map[x][y] == 0:
        dice_map[x][y] = dice[0]
    else:           # 지도에 값이 있으면 주사위 바닥에 지도의 값을 복사하고, 지도의 값이 0으로 변환
        dice[0] = dice_map[x][y]
        dice_map[x][y] = 0


N, M, x, y, K = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

di = [0, 0, 0, -1, 1]       # 델타
dj = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]       # 주사위 처음에는 모든 면이 0

for i in command:       # 명령 차례로 이행
    x += di[i]          # 좌표가 방향에 따라 바뀜
    y += dj[i]

    if x < 0 or x >= N or y < 0 or y >= M:      # 지도 밖으로 나가면 좌표이동 취소 후, 다음 명령 이행
        x -= di[i]
        y -= dj[i]
        continue
    
    if i == 1:      # 명령에 따른 방향으로 굴리기!
        east(x, y)
    elif i == 2:
        west(x, y)
    elif i == 3:
        north(x, y)
    elif i == 4:
        south(x, y)
        
    print(dice[3])      # dice list의 인덱스 3의 값이 주사위의 윗면