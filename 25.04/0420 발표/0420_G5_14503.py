'''
G5 14503 로봇 청소기

로봇 청소기와 방의 상태가 주어질 때, 청소하는 영역 개수를 구하는 문제

로봇 청소기 있는 방은 NxM크기 직사각형으로 나타내고, 1x1칸으로 나누어져 있음.
각 칸은 벽 혹은 빈칸. 청소기의 바라보는 방향은 동, 서, 남, 북 중 하나.
방의 각 칸은 좌표 (r, c)로 나타내고, 가장 북쪽 줄의 가장 서쪽 칸 좌표가 (0, 0).
가장 남쪽 줄의 가장 동쪽 좌표가 (N-1, M-1).

즉, 좌표 (r, c)는 북쪽에서 (r+1)번째에 있는 줄의 서쪽에서 (c+1)번째 칸을 가리킴.
처음 빈 칸은 전부 청소되지 않은 상태.

로봇 작동 방식:
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우,
    - 바라보는 방향 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아감
    - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동 멈춤.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우.
    - 반시계 방향으로 90도 회전
    - 바라보는 방향 기준 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
    - 1번으로 돌아감.

입력:
N, M : 방 크기 (3이상 50이하)
r, c, d : 좌표, 바라보는 방향. d가 0이면 북쪽, 1은 동, 2는 남, 3은 서.
N개의 줄동안 방의 상태 주어짐. 0은 청소되지 않은 빈칸, 1은 벽이 있는 곳. 방의 동서남북 끝중 하나 이상에 위치한 모든 칸에는 벽이 존재.
로봇 청소기가 있는 칸은 항상 빈 칸
'''

# import sys
# sys.stdin = open('tc.txt')

di = [-1, 0, 1, 0]      # 델타
dj = [0, 1, 0, -1]

def dfs(r, c, d):
    global result

    x, y, direction = r, c, d       # 첫 좌표, 방향

    while True:
        if visit[x][y] == 0:        # 청소 안했으면 청소함
            visit[x][y] = 1
            result += 1
        
        for _ in range(4):
            direction = (direction-1)%4     # 방향은 저장해놓고, 계속 돌림.
            nx = x + di[direction]          # 좌표 옮겨보기
            ny = y + dj[direction]

            if visit[nx][ny] or room[nx][ny]:       # 만약 방문했고, 벽이면 다음 방향 탐색
                continue
            
            x, y = nx, ny       # 방문해야할곳이면 좌표 변경
            break
        else:   # 주위 4방향이 모두 방문 불가라면 돌아가야함
            x, y = x - di[direction], y - dj[direction]     # 바라보던 방향의 뒤로 가기
            if room[x][y]:      # 만약 뒤가 벽이면 작동 중지 후 결과 출력
                print(result)
                return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
result = 0

dfs(r, c, d)