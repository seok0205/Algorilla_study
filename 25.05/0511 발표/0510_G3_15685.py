'''
G3 15685 드래곤 커브

드래곤 커브는 아래와 같은 세 가지 속성으로 이루어져 있음. 이차원 좌표 평면 위에서 정의됨. x축은 ->, y축은 ↓ 방향
1. 시작 점
2. 시작 방향
3. 세대

0세대 드래곤 커브는 길이가 1인 선분. (0, 0)에서 시작하는 0세대 드래곤 커브는
시작 방향이 오른쪽일 때, (0, 0)에서 (1, 0)

1세대 드래곤 커브는 0세대 드래곤 커브를 끝 점 기준으로 시계 방향으로 90도 회전시킨 다음 0세대 드래곤 커브의 끝 점에 붙인 것.
끝 점이란 시작 점에서 선분을 타고 이동했을 대, 가장 먼 거리에 있는 점 의미
(0, 0) -> (1, 0) -> (1, -1)

2세대 드래곤 커브도 1세대를 만든 방법 활용해 만들 수 있음
(0, 0) -> (1, 0) -> (1, -1) -> (0, -1) -> (0, -2)

3세대 드래곤 커브도 2세대 드래곤 커브 활용해 만들 수 있음
(0, 0) -> (1, 0) -> (1, -1) -> (0, -1) -> (0, -2) -> (-1, -2) -> (-1, -1) -> (-2, -1) -> (-2, -2)

즉, K세대 드래곤 커브는 K-1세대 드래곤 커브를 끝점 기준으로 90도 시계 방향 회전시킨 다음 그걸 끝점에 붙인 것.

크기 100x100 격자 위에 드래곤 커브 N개 존재. 이때, 크기가 1x1 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형 개수를 구하는 프로그램을 작성.
격자 좌표는 (x, y), 0 <= x, y <= 100만 유효한 좌표

입력:
N : 드래곤 커브 개수
N개의 줄에 드래곤 커브의 정보
x, y : 드래곤 커브의 시작점.
d : 시작 방향(0, 1, 2, 3 차례로 동 북 서 남)
g : 세대
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

directions = {0: (0, 1), 1:(-1, 0), 2:(0, -1), 3:(1, 0)}        # 방향 딕셔너리


def dragon_curve(x, y, d, g):               # 드래곤 커브 구하는 함수
    way = [d]                               # 첫 방향 기억
    visit[x][y] = 1                         # 첫 꼭짓점 방문(visit는 하나의 칸이 하나의 꼭짓점)
    nx = x + directions[d][0]               # 무조건 0세대부터 시작임
    ny = y + directions[d][1]
    visit[nx][ny] = 1                       # 0세대는 하나의 선분 첫점과 끝점 방문

    for n in range(g):                      # 1세대 부터 해당. 0세대는 실행되지 않음
        generation = 2**n
        for i in range(generation):         # 세대 마다 2의 배수로 방문할점이 증가함. 0세대는 2개, 1세대는 3개, 2세대는 5개, 3세대는 9개, 4세대는 17개...
            if generation == 1:             # 1세대의 경우 90도 회전해서 점 한개 방문하고 끝. 1세대 전용 if문.
                nx += directions[(way[i]+1)%4][0]
                ny += directions[(way[i]+1)%4][1]

                way.append((way[i]+1)%4)    # 왔던 방향에 추가

                if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:      # 범위 이탈 방지
                    continue

                visit[nx][ny] = 1           # 꼭짓점 방문
                continue

            if i >= generation//2:          # 2세대부터 해당. 여기서부터 규칙이 존재. 왔던 방향이 만약 4개라면. 첫번째와 두번째 방향은 이전 방향과 정반대로 가지만, 세번째와 네번째 방향은 똑같음.
                nx = nx + directions[way[i]][0]     # 따라서 2의 지수적으로 증가한 수의 반을 나누고, 뒤쪽의 방향이면 이전방향과 같게 해줌
                ny = ny + directions[way[i]][1]
                
                way.append(way[i])                  # 계속 방향에 추가는 해줌. 뒷세대를 위해 기억해야함
                
                if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                    continue
                
                visit[nx][ny] = 1
            else:                                   # 이 else문은 반으로 나눈 인덱스 중 앞쪽의 방향이면 이전방향과 정반대로.
                new_way = (way[i]+2)%4              # 정반대로 가야하므로, 딕셔너리 키값을 2 증가시켜줌. 2 증가시켜주어야 정반대의 방향이 됨.
                nx = nx + directions[new_way][0]
                ny = ny + directions[new_way][1]

                way.append(new_way)

                if nx < 0 or nx >= 101 or ny < 0 or ny >= 101:
                    continue

                visit[nx][ny] = 1


N = int(input())
visit = [[0] * 101 for _ in range(101)]             # 유효 x, y가 0부터 100임 그래서 101칸을 만들어 줌.
result = 0

for _ in range(N):                                  # 드래곤 커브 모두 그려봄
    x, y, d, g = map(int, input().split())

    dragon_curve(y, x, d, g)

for i in range(100):                    # 4꼭짓점이 모두 드래곤 커브의 일부여야하므로, 
    for j in range(100):
        if visit[i][j]:
            if visit[i+1][j] and visit[i][j+1] and visit[i+1][j+1]:         # 사각형 모양이 있다면 결과 1증가
                result += 1

print(result)