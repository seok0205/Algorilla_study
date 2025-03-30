'''
G3 2206 벽 부수고 이동하기

NxM의 행렬로 표현되는 맵이 존재. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳 나타냄.
(1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 함.
최단 경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작한느 칸과 끝나는 칸도 포함해서 셈.
만약 이동하는 도중 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한개 부수고 이동해도 됨
한칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸. 맵이 주어지면 최단경로 구하라.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [0, 0, 1, -1]              # 델타 활용
dj = [1, -1, 0, 0]


def bfs():                      # bfs활용. 최단 거리
    q = deque()
    q.append((0, 0, 0))         # 좌표와 벽이 깨졌는지 여부
    visit = [[[0, 0] for _ in range(M)] for _ in range(N)]          # [0, 0]은 0번 인덱스에는 벽을 아직 지나지 않은 상태에서의 이동거리, 1번 인덱스는 벽을 부순 상태에서의 최소 이동 거리 저장.
    visit[0][0][0] = 1          # 시작좌표에서는 벽인 경우가 없다고 가정되어 있기에, 벽을 깨지 않은 상태로 시작하고, 거리는 시작 위치 포함이므로 1로 시작
    
    while q:
        target = q.popleft()
        
        if (target[0], target[1]) == (N-1, M-1):            # 만약 (N, M)에 도달했다면, 큐에 먼저 들어있는 값이 최소 거리 값일 것임. 따라서 끝 좌표인지 확인되면 바로 반환
            return visit[target[0]][target[1]][target[2]]
        
        for k in range(4):                  # 델타 4방향 탐색
            x = target[0] + di[k]
            y = target[1] + dj[k]
            
            if x < 0 or x >= N or y < 0 or y >= M:              # 범위 밖이면 넘어감
                continue
            
            if area[x][y] == '1' and target[2] == 0:                # 벽이고, 아직 하나를 깨지 않은 상태면
                visit[x][y][1] = visit[target[0]][target[1]][0] + 1     # 벽을 부수고 통과 해버림
                q.append((x, y, 1))
            
            if area[x][y] == '0' and visit[x][y][target[2]] == 0:   # 지나갈 수 있는 통로이고, 아직 지나가지 않았다면,
                visit[x][y][target[2]] = visit[target[0]][target[1]][target[2]] + 1         # 방문 리스트 기록
                q.append((x, y, target[2]))

    return -1

N, M = map(int, input().split())

area = [list(input()) for _ in range(N)]

result = bfs()
print(result)