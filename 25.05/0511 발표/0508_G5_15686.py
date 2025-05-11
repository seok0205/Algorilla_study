'''
G5 15686 치킨 배달

NxN 크기 도시 존재. 각 칸은 빈칸, 치킨집, 집 중 하나.
칸은 r행 C열 혹은 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미 r, c는 1부터 시작

치킨 거리는 집을 기준으로 정해짐.(가장 가까운 치킨집 사이의 거리) 각각의 집은 치킨 거리를 가지고 있음.
도시의 치킨 거리는 모든 집의 치킨 거리의 합.

일부 치킨집 폐업 시키려고 함. 치킨 집 중 최대 M개 고르고, 나머지 치킨집 폐업 시켜야함. 어떻게 고르면
도시의 치킨 거리가 가장 작게 될지 구하는 문제

입력:
N, M : 도시의 가로 세로
N개의 줄에 도시 정보주어짐
도시 정보는 0은 빈칸, 1은 집, 2는 치킨집. 집의 개수는 2N넘지않음. 적어도 하나는 존재.
치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def get_chicken_house():        # 치킨집과 집들 좌표 구하기
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                chicken.append((i, j))
            elif city[i][j] == 1:
                house.append((i, j))


def get_chicken_road(idx, cnt, visit):
    global result

    new_visit = visit.copy()

    if cnt == M:                    # 3개 치킨집 고르면 각자 집들의 치킨거리 구해서 총 합 구하기
        length = 0
        for i in house:             # 집마다 각각의 치킨거리 구해야함
            sub = INF
            for k in range(len(new_visit)):     # 선택한 M개의 치킨집과의 거리 구하고 최솟값이 치킨거리
                if new_visit[k]:
                    sub = min(sub, abs(chicken[k][0]-i[0])+abs(chicken[k][1]-i[1]))     # x좌표끼리 뺀 절댓값, y좌표끼리 뺀 절댓값 합친 게 치킨 거리 공식
            length += sub       # 도시의 치킨거리는 모든 집의 치킨 거리 합해야함

        result = min(result, length)        # 도시의 치킨 거리가 최솟값인지 비교
        return
    else:
        for i in range(idx, len(chicken)):
            if new_visit[i] != 1:
                new_visit[i] = 1
                get_chicken_road(i + 1, cnt + 1, new_visit)     # dfs 형식으로 모든 조합 탐색
                new_visit[i] = 0


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
INF = 1000000               # 주어진 범위내에선 나올 수 없는 수
result = INF
chicken = list()
house = list()

get_chicken_house()

visit = [0] * len(chicken)
get_chicken_road(0, 0, visit)

print(result)