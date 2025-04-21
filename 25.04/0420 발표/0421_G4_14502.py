'''
G4 14502 연구소

바이럿의 확산을 막기 위해 연구소에 벽을 세우려 함.
연구소는 NxM 직사각형, 1x1 칸으로 나누어져 있음.
빈 칸과 벽으로 이루어져 있고, 벽은 칸 하나 차지.
일부 칸은 바이러스 존재, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있음.
새로 세울 수 있는 벽의 개수는 3개, 꼭 3개를 세워야함.

0은 빈칸, 1은 벽, 2는 바이러스 있는 곳.
벽을 3개 세우고 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 함.
연구소가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 문제.

입력:
N, M : 세로, 가로
N개 줄에 지도의 모양 주어짐. 0은 빈칸, 1은 벽, 2는 바이러스.
2는 2개 이상 10개 이하.
빈칸의 개수는 3개 이상.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs():                  # 바이러스 퍼지기
    global result

    q = deque()
    visit = [i[:] for i in lab]     # 연구소 상태 가지고 옴

    for i in range(N):              # 모든 바이러스를 찾아서 인큐
        for j in range(M):
            if lab[i][j] == 2:
                q.append((i, j))

    while q:                    # 너비 우선 탐색 시작(바이러스 퍼져나감)
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visit[nx][ny]:
                continue

            visit[nx][ny] = 2
            q.append((nx, ny))
    
    safe_zone = 0           # 바이러스 모두 퍼지면 안전구역 구함
    for i in visit:
        safe_zone += i.count(0)

    result = max(result, safe_zone)     # 최댓값 비교


def wall(cnt):      # 벽 세우기(백트래킹)
    if cnt == 3:        # 만약 3번 세우면 바이러스 퍼트려보기
        bfs()
        return
    
    for i in range(N):              # 벽세워보기
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1       # 세우고
                wall(cnt + 1)       # 다음 벽세우기
                lab[i][j] = 0       # 세운 경우의 수 봤으니 벽 다시 없애기


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
result = 0

wall(0)

print(result)