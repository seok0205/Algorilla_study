'''
S2 2644 촌수계산

부모 자식 사이 1촌.
나, 할아버지는 2촌, 아버지 형제와 할아버지는 1촌, 나, 아버지 형제들과는 3촌.
여러 사람들에 대한 부모 자식간 관계가 주어지면 두 사람 촌수를 계산하는 프로그램 작성
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def bfs(s, e):
    q = deque()
    q.append(s)
    visit = [0] * (N+1)
    visit[s] = 1        # 자기자신은 1부터 시작 다음 부모노드가 번호 2를 받으면 차이가 1. 둘은 1촌.
    
    while q:
        target = q.popleft()
        for i in edge[target]:
            if visit[i] == 0:   # 번호 부여 안받았으면
                visit[i] = visit[target] + 1        # 그 전 노드가 부여받은 번호에 1더해서 받음
                q.append(i)
            if i == e:
                return visit[e] - visit[s]      # 목표 사람과 현재 사람의 번호차가 촌과 같다고 할 수 있음
    
    return -1       # 위 return 조건에서 걸리지않으면 연결되지 않은 것.
    

N = int(input())
a, b = map(int, input().split())
M = int(input())
edge = [[] for _ in range(N+1)]     # 간선 정보 저장 리스트

for _ in range(M):
    p_node, c_node = map(int, input().split())
    
    edge[p_node].append(c_node)
    edge[c_node].append(p_node)
    
result = bfs(a, b)

print(result)