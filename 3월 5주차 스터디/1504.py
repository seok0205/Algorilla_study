import sys, heapq
input = sys.stdin.readline

# 시작점에서 내가 원하는 노드로 갈거임
# 가지 못한다면 -1을 반환하고 할 수 있다면 visited[end]를 리턴한다.
def dijkstra(start, end):
    distance = [float('inf')] * (N+1)
    distance[start] = 0

    # 우선 순위 큐 ( 거리, 노드 )
    pq = [(0, start)]

    while pq:
        dis, now = heapq.heappop(pq)

        if distance[now] < dis:
            continue

        for next_dis, next_node in graph[now]:
            new_dist = dis + next_dis
            
            if distance[next_node] <= new_dist:
                continue

            distance[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    
    return (distance[1] + distance[end], distance[N])


# 점점 개수, 간선 개수
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    # c : 정점 사이 거리
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
# 필수로 거쳐야 하는 정점 2개
v1, v2 = map(int, input().split())
one_v1_v2, v1_end = dijkstra(v1, v2)
one_v2_v1, v2_end = dijkstra(v2, v1)
result = min(one_v1_v2 + v2_end, one_v2_v1 + v1_end)
if result == float('inf'):
    print(-1)
else:
    print(result)