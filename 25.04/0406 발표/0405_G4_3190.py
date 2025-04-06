'''
G4 3190 뱀

게임에 뱀이 나와서 기어다님. 사과를 먹으면 뱀 길이가 늘어남.
게임은 NxN 정사각 보드 ㅜ이에서 진행, 몇몇 칸에는 사과가 놓여져 있음
보드의 상하좌우 끝에 벽이있음. 게임 시작 시 뱀은 맨 위 맨 좌측에 위치, 뱀의 길이는 1.
뱀은 처음에 오른쪽을 향함.

매 초마다 이동 시 다음 규칙을 따름
1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치 시킴
2. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝남
3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음.
4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌. 즉, 몸 길이는 변하지 않음.

사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하시오.

입력:
N : 보드 크기
K : 사과 개수
K줄 동안 첫번째 정수는 행, 두번째 정수는 열 위치(사과의 위치 모두 다르고, 맨 위 맨 좌측에는 사과 없음)
L : 뱀의 방향 변환 횟수
L줄 동안 X(int), C(str) : 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L')혹은 오른쪽(C가 'D')으로 90도 회전시킨다는 뜻. 정보는 X가 증가하는 순으로 주어짐)
'''

# import sys 
# sys.stdin = open('tc.txt', 'r')

from collections import deque

N = int(input())    # 맵 크기
K = int(input())    # 사과 개수
game = [[0] * N for _ in range(N)]      # 맵
for _ in range(K):                      # 사과 배치
    r, c = map(int, input().split())
    game[r-1][c-1] = 'A'
    
change_cnt = int(input())       # 방향 변환 횟수
game[0][0] = 'S'                # 뱀 머리 배치

change_dic = {}
for _ in range(change_cnt):     # 게임 시작
    X, C = map(str, input().split())
    X = int(X)
    change_dic[X] = C

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # 방향 오른쪽부터 시작.
dir_num = 0
x = 0
y = 0
snake_body = deque()
snake_body.append((0, 0))

second = 0
while True:
    x += directions[dir_num % 4][0]
    y += directions[dir_num % 4][1]

    if x < 0 or x >= N or y < 0 or y >= N:
        second += 1
        break
    
    snake_body.append((x, y))
    second += 1
    
    change = change_dic.get(second)
    if change:
        if change == 'L':
            dir_num -= 1
        else:
            dir_num += 1
            
    if game[x][y] == 'A':
        game[x][y] = 'S'
        continue
    elif game[x][y] == 'S':
        break
    else:
        game[x][y] = 'S'
        disappear = snake_body.popleft()
        game[disappear[0]][disappear[1]] = 0
    
print(second)