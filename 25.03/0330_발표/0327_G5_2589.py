'''
G5 2589 보물섬

보물섬 지도는 직사각형 모양이고 여러 칸으로 나뉘어져 있음.
각 칸은 육지 혹은 바다로 표시. 이동은 상하좌우로 이웃한 육지로만 가능.
한 칸 이동에 한시간 걸림.

보물은 서로간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두곳에 나뉘어 묻혀있음
육지를 나타내는 두곳 사이를 최단 거리로 이동하려면 같은 곳을 두번이상지나가거나, 멀리 돌아가선 안됨.

보물지도가 주어질때, 보물이 묻혀있는 두 곳의 최단 거리로 이동하는 시간을 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(s1, s2):                # bfs 알고리즘 활용
    q = deque()
    q.append((s1, s2))
    visit = [[0] * width for _ in range(height)]
    visit[s1][s2] = 1
    max_dist = 0

    while q:
        target = q.popleft()
        for k in range(4):
            x = target[0] + di[k]
            y = target[1] + dj[k]
            
            if x < 0 or x >= height or y < 0 or y >= width:
                continue
            
            if visit[x][y] or t_map[x][y] == 'W':
                continue
            
            visit[x][y] = visit[target[0]][target[1]] + 1
            max_dist = max(visit[x][y], max_dist)                   # bfs를 하면서 실시간으로 최대길이가 나오면 max_dist에 저장. 어차피 bfs는 가장 먼 위치까지의 최단 거리를 구하는 알고리즘.
            q.append((x, y))
            
    return max_dist


height, width = map(int, input().split())           # 보물지도의 세로, 가로 길이 입력

t_map = [list(input()) for _ in range(height)]      # 보물지도의 바다인지, 육지인지 표시한 상태 'W', 'L'로 구분 입력

result = 0

for i in range(height):
    for j in range(width):
        if t_map[i][j] == 'L':              # 육지마다 가장 먼 거리까지 가보기, 모든 육지 다돌아보면서 최장거리가 나오는 곳이 보물섬 있는 위치
            dist = bfs(i, j)
            result = max(dist, result)      # 나오는 길이는 (i,j) 좌표인 섬에서 가장 먼 육지까지의 최단 거리를 반환함. 따라서 현재 result와 비교해서 더 길이가 길게 나온 수를 골라야함
            
print(result-1)