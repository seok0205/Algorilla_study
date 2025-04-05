import sys, heapq
input = sys.stdin.readline

# 시작점에서 내가 원하는 노드로 갈거임
# 가지 못한다면 -1을 반환하고 할 수 있다면 visited[end]를 리턴한다.
def dijkstra(graph, start, end):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    visited = set()
    # 우선 순위 큐 ( 거리, 노드 )
    pq = [(0, start)]

    while pq:
        dis, now = heapq.heappop(pq)

        if now == end:
            return distance[now]

        if now in visited:
            continue

        visited.add(now)

        for next_dis, next_node in graph[now]:
            if next_node not in visited and distance[next_node] > dis + next_dis:
                distance[next_node] = dis + next_dis
                heapq.heappush(pq, (distance[next_node], next_node))

    return -1

# 점점 개수, 간선 개수
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    # c : 정점 사이 거리
    a, b, c = map(int, input().split())
    heapq.heappush(graph[a], (c, b))
    heapq.heappush(graph[b], (c, a))
# 필수로 거쳐야 하는 정점 2개
v1, v2 = map(int, input().split())

# 1번 -> v1 -> v2 -> N번
st_1 = dijkstra(graph, 1, v1)
st_v1 = dijkstra(graph, v1, v2)
st_v2 = dijkstra(graph, v2, N)
result1 = [st_1, st_v1, st_v2]
flag1 = 0
# 1번 -> v2 -> v1 -> N번
st_11 = dijkstra(graph, 1, v1)
st_v11 = dijkstra(graph, v1, N)
st_v22 = dijkstra(graph, v2, v1)
result2 = [st_11, st_v11, st_v22]
flag2 = 0

for num in result1:
    if num == -1:
        flag1 = 1e10
        break
    flag1 += num

for num in result2:
    if num == -1:
        flag2 = 1e10
        break
    flag2 += num

if flag1 == 1e10 and flag2 == 1e10:
    print(-1)
else:
    print(min(flag1, flag2))