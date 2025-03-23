'''
G4 1197 최소 스패닝 트리

그래프가 주어질 때, 그 그래프의 최소 스패닝 트리를 구하라
최소 스패닝 트리는, 주어진 그래프의 모든 저점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리 말함
입력으로 주어지는 그래프는 하나의 연결 그래프임이 보장
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

import heapq


def prim(s):            # 프림 알고리즘 활용
    q = [(0, s)]
    visit = [0] * (V+1)
    min_w = 0
    
    while q:
        w, n = heapq.heappop(q)     # 최소힙에서 최상단 정보 꺼냄
        
        if visit[n]:        # 이미 방문한 곳이면 다음 정보
            continue
        
        visit[n] = 1        # 방문했음
        min_w += w          # 꺼낸 정보에선 최단 거리 가진 노드가 나오기 때문에 최솟값에 더해줌
        
        for next_w, next_n in graph[n]:     # 간선 정보 리스트에서 다음 가중치, 다음 노드 위치 탐색
            if visit[next_n]:               # 만약 방문한 곳들이면 다음 정보 탐색
                continue
            
            heapq.heappush(q, (next_w, next_n))     # 한번도 방문 안한 곳이면 최소힙에 푸시
    
    return min_w


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]        # 간선 정보 저장 리스트

for _ in range(E):                      # 간선 수만큼 정보를 저장해줌
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
result = prim(1)
print(result)