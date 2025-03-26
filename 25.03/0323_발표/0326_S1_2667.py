'''
S1 2667 단지번호붙이기

정사각형의 지도가 있음. 1은 집이 있는 곳, 0은 집이 없는 곳 나타냄
지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호 붙이려 함
여기서 연결된다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우 말함
대각선상에 집이 있는 건 해당안됨
지도 입력해 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬해 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def dfs(s1, s2, cnt):           # dfs 활용
    stack = []
    stack.append((s1, s2))
    visit[s1][s2] = cnt
    
    while stack:
        target = stack.pop()
        for k in range(4):
            x = target[0] + di[k]       # 델타 활용 4방향의 집 확인
            y = target[1] + dj[k]
            
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            
            if visit[x][y]:
                continue
            
            if apt[x][y] == '1':        # 조건 모두 만족하면 방문리스트에 단지 번호 부여
                visit[x][y] = cnt
                stack.append((x, y))
            
            
N = int(input())
apt = [input() for _ in range(N)]

visit = [[0] * N for _ in range(N)]
result = []
cnt = 0

for i in range(N):
    for j in range(N):
        if apt[i][j] == '1' and visit[i][j] == 0:       # 단지하나 생성될때마다 cnt는 하나씩 증가됨
            cnt += 1
            dfs(i, j, cnt)
            
for k in range(1, cnt+1):               # 단지번호만큼 개수 알아내기
    s = 0
    for l in range(N):
        s += visit[l].count(k)
    result.append(s)

result.sort()               # 오름차순 정렬

print(len(result))      # 출력
for i in result:
    print(i)