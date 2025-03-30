'''
G4 1504 특정한 최단 경로

방향성 없는 그래프 주어짐. 1번에서 N번 정점으로 최단 거리 이동하려 함.

임의로 주어진 두 정점은 반드시 통과해야 함

한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동 가능.
하지만 반드시 최단 경로로 이동해야 함
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

import heapq


def dijkstra(s):
    hq = [(0, s)]               # 최소힙에 넣음. (거리, 위치)
    visit = [INF] * (N+1)       # 그 위치까지의 최단 거리 저장할 리스트
    visit[s] = 0                # 시작 위치는 최단 거리는 0임
    
    while hq:
        d, node = heapq.heappop(hq)     # 가장 거리가 짧은 위치로 갈 정보가 먼저 나옴
        
        if visit[node] < d:             # 만약 현재까지 알아낸 이 위치까지의 최단 거리보다 이번 정보의 거리가 더 크면, 탐색할 의미가 없으므로 다음 정보로 넘김
            continue
        
        for info in connect[node]:      # 이 위치와 연결된 위치의 정보들을 순회
            next_d = info[0]            # 다음 위치까지의 거리
            next_node = info[1]         # 다음 위치 번호
            
            new_dist = d + next_d       # 지금까지의 거리와 다음 위치까지 거리 합친것이 시작점부터 다음 노드까지의 거리
            
            if visit[next_node] <= new_dist:        # 만약 new_dist가 다음 노드가 가진 최단 거리보다 크면 다음 정보 탐색하러 감
                continue
            
            visit[next_node] = new_dist             # 위 조건에서 안걸렸다면 최단 거리 교체
            heapq.heappush(hq, (new_dist, next_node))       # 최소 힙에 새로운 최단거리와, 다음 위치의 정보를 묶어 푸시
            
    return visit        # 각 위치까지의 최단 거리 담은 리스트 반환
    

N, E = map(int, input().split())    # N: 정점 개수, E: 간선 개수
connect = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())     # a번 정점에서 b번 정점까지 양방향 길 존재, 그 길의 거리가 c.
    connect[a].append((c, b))
    connect[b].append((c, a))
    
need1, need2 = map(int, input().split())    # 반드시 지나야하는 정점 2개
INF = float('inf')

first_route = dijkstra(1)       # 출발점이 1
second_route = dijkstra(need1)  # 출발점이 반드시 지나야하는 정점
third_route = dijkstra(need2)

result_1 = first_route[need1] + second_route[need2] + third_route[N]        # 반드시 지나야하는 정점 둘중 하나를 지나면 그다음은 나머지 반드시 지나야하는 정점을 지나야함
result_2 = first_route[need2] + third_route[need1] + second_route[N]        # 따라서 need1을 먼저 지날때, need2를 먼저 지날때 두 가지 상황의 결과를 고르고, 최솟값을 판별

result = min(result_1, result_2)

if result == float('inf'):          # 그런데 최단 거리를 찾지 못한 결과가 하나라도 있으면 inf로 나옴. 만약 inf로 나왔다면 -1를 출력
    result = -1

print(result)