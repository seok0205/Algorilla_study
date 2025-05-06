'''
G3 15683 감시

NxM 사무실에 K개의 CCTV가 설치. 종류는 5개.

1. 한 쪽 방향만 감시 가능
2. 양방향 감시 가능(2방향)
3. 직각 방향 감시 가능(2방향)
4. 3방향 감시 가능
5. 4방향 감시 가능

카메라는 감시 방향의 모든 칸은 감시 가능. 하지만 벽에 막히면 못함.
CCTV는 회전할 수 있음. 항상 90도 방향으로 하고 감시 방향이 가로 혹은 세로 방향이어야 함.

사무실 지도에서 0은 빈칸, 1에서 5는 카메라 종류, 6은 벽이다.
카메라를 회전시켜서 사각지대를 최소크기로하는 문제. 최소크기를 출력.
CCTV의 최대 개수는 8개를 넘지않음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

di = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # 방향 (동 남 서 북)

watch_area = {1: [[0], [1], [2], [3]],      # cctv 마다 촬영방향 다름. 회전시 경우의 수 모두 포함
              2: [[0, 2], [1, 3]],
              3: [[0, 1], [1, 2], [2, 3], [3, 0]],
              4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
              5: [[0, 1, 2, 3]]}


def watch(om, directions, x, y):        # 방향 따라 감시 영역 전개
    for d in directions:                # 촬영 방향
        nx = x
        ny = y
        while True:                     # 사무실 안이고 벽이 나오지 않으면 -1로 감시 중이라고 표시
            nx += di[d][0]
            ny += di[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break

            if om[nx][ny] == 6:
                break

            if om[nx][ny] == 0:
                om[nx][ny] = -1


def find_blind_spot(idx, om):       # cctv dfs 형식으로 완탐
    global result

    if idx == len(cctv_position):       # cctv모두 확인하면
        blind = 0
        for i in range(N):                  # 0개수 확인, (사각지대 갯수)
            blind += om[i].count(0)
        result = min(result, blind)         # 최솟값 비교
        return
    
    new_office = [i[:] for i in om]         # 사무실 정보 깊은 복사
    x, y, n = cctv_position[idx]            # cctv 정보 불러옴

    for directions in watch_area[n]:                # cctv 회전 방향 모두 확인
        watch(new_office, directions, x, y)         # 해당 회전 경우의 수 상황 시 영역 표시
        find_blind_spot(idx+1, new_office)          # 다음 cctv 경우의 수 확인하러 출발
        new_office = [i[:] for i in om]             # 회전 방문 리스트 겹칠 수 있어 따로 봐야함. 사무실 정보 초기화


N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]

cctv_position = list()
result = N * M

for i in range(N):
    for j in range(M):
        if office[i][j] in [1, 2, 3, 4, 5]:     # cctv 위치 확인하고 cctv 정보에 추가
            cctv_position.append((i, j, office[i][j]))

find_blind_spot(0, office)      # dfs 실행

print(result)