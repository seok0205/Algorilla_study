'''
D4 1211 Ladder2

사다리를 탔을 때 어느 사다리가 최단 거리로 바닥에 도착하는지 구하려고 함
출발점에서 아래방향 진행하면서 좌우 방향으로 이동 가능한 통로 나타나면 방향 전환
방향 전환 이후엔 다시 아래방향으로만 이동, 바닥 도착 시 멈춤
100x100 크기 2차원 배열로 주어진 사다리에서 모든 출발점을 검사해 바닥까지 가장 짧은 이동 거리를 갖는
시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드 작성(사다리는 1로 표현)
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

di = [0, 0]     # 좌우 방향 델타
dj = [1, -1]


def start(s1, s2, cnt):         # 사다리 타기 함수
    global result, min_route
    
    if s1 == 99:                # 바닥에 도착하면 최솟값끼리 비교 후 최솟값이면 시작 인덱스를 답으로 설정
        if cnt < result:
            result = cnt
            min_route = i
        return
    
    for k in range(2):          # 양옆 탐색
        x = s1 + di[k]
        y = s2 + dj[k]
        if 0 <= x < 100 and 0 <= y < 100 and ladders[x][y] and not visit[x][y]:
            visit[x][y] = 1
            start(x, y, cnt+1)      # 배열 안이고, 한번도 안간 칸이면 다음 칸으로 이동
            return
    else:                           # 양옆이 1이아니면 밑으로 가기
        visit[s1+1][s2] = 1
        start(s1+1, s2, cnt+1)


for tc in range(1, 11):
    t_num = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    
    result = float("inf")
    
    for i in range(100):        # 출발점 탐색
        if ladders[0][i]:       # 1이면 출발
            visit = [[0] * 100 for _ in range(100)]     # 방문 기록지
            start(0, i, 0)
            
    print(f'#{tc} {min_route}')