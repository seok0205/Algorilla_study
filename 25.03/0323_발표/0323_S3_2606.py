'''
S3 2606 바이러스

바이러스는 네트워크 통해 전파됨
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에 연결되어 있는
모든 컴퓨터는 웜 바이러스에 걸리게 됨

1번 컴퓨터가 웜 바이러스에 걸리면, 컴퓨터수, 네트워크 상에서 서로 연결되어 있는
정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수 출력.

접근 방법: bfs 활용.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def bfs():
    q = deque()
    q.append(1)
    visit = [0] * (computers+1)
    visit[1] = 1
    cnt = 0
    
    while q:
        target = q.popleft()
        for edge in edges[target]:      # 연결되어있는 네트워크 따라 방문
            if visit[edge] == 0:        # 방문안했으면 방문하고
                q.append(edge)
                visit[edge] = 1
                cnt += 1                # 감염 +1
    
    return cnt
    
    
computers = int(input())
couple = int(input())
edges = [[] for _ in range(computers+1)]

for _ in range(couple):         # 네트워크가 연결되어 있는 컴퓨터 번호쌍 받아서
    a, b = map(int, input().split())
    edges[a].append(b)          # 네트워크 간선 리스트에 저장. 양방향으로
    edges[b].append(a)
    
result = bfs()
print(result)