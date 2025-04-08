import sys
input = sys.stdin.readline
# 동서북남
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
'''
N x M 지도
주사위는 윗면이 1이고 동쪽을 바라보는 방향이 3인 상태로 놓아져 있다.
처음엔 모두 0이 적힌 상태로 시작
지도의 각 칸에는 정수가 쓰여져 있는데 만약 0이 쓰여져 있으면
주사위의 아랫면에 있는 수가 복사된다.
0이 아닌경우는 칸에 쓰여 있는 수가 주사위에 복사되며 그 칸은 0이 된다.
주사위를 놓은 곳의 좌표와 이동시키는 명령 주어질 때
매 명령마다 주사위의 상단에 쓰여 있는 값을 구해라!
만약 주사위가 지도 밖으로 벗어나는 명령일 경우 무시한다.(출력도 X)
'''
def next_dice(way):
    global dice
    # 동쪽 이동
    if way == 1:
        # 현재 주사위에서 상하좌우
        top, bot, left, right = dice[0], dice[1], dice[4], dice[5]
        dice[0] = left ; dice[1] = right ; dice[4] = bot ; dice[5] = top
    # 서쪽 이동
    elif way == 2:
        top, bot, left, right = dice[0], dice[1], dice[4], dice[5]
        dice[0] = right ; dice[1] = left ; dice[4] = top ; dice[5] = bot
    # 북쪽 이동
    elif way == 3:
        top, bot, front, back = dice[0], dice[1], dice[2], dice[3]
        dice[0] = front ; dice[1] = back ; dice[2] = bot ; dice[3] = top
    # 남쪽 이동
    else:
        top, bot, front, back = dice[0], dice[1], dice[2], dice[3]
        dice[0] = back ; dice[1] = front ; dice[2] = top ; dice[3] = bot
        

# 세로, 가로, 주사위 좌표(x, y), 명령 개수
N, M, x, y, o = map(int, input().split())
# 처음 주사위를 놓는 칸에 쓰여진 수는 항상 0이다!
arr = [list(map(int, input().split())) for _ in range(N)]
# 동서북남 -> 1,2,3,4
order = list(map(int, input().split()))
# 상하앞뒤좌우
dice = [0] * 6
r, c = x, y
for i in range(o):
    nr, nc = r + dr[order[i]-1], c + dc[order[i]-1]
    if nr < 0 or nr >= N or nc < 0 or nc >= M:
        continue
    next_dice(order[i])
    # 맵의 바닥이 0이면 주사위 아랫면으로 바꿔준다.
    if arr[nr][nc] == 0:
        arr[nr][nc] = dice[1]
        print(dice[0])
    # 맵의 바닥이 0이 아니면 주사위 바닥을 맵바닥숫자로 바꾸고 맵은 0으로 바꿈
    else:
        dice[1] = arr[nr][nc]
        arr[nr][nc] = 0
        print(dice[0])
    r, c = nr, nc