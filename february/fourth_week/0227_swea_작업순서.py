# def remove_visited_in_need_to_visit_list(num):
#     for entry in need_to_visit:
#         if num in entry:
#             entry.remove(num)
#
#
# for t in range(1, 11):
#     V, E = map(int, input().split())
#     arr = list(map(int, input().split()))
#     nodes = []
#     for i in range(0, len(arr), 2):
#         nodes.append([arr[i], arr[i + 1]])
#     # print(nodes)
#
#     adj_list = [[] for _ in range(V + 1)]
#     # print(adj_list)
#
#     for v, w in nodes:
#         adj_list[v].append(w)
#     # print(adj_list)
#
#     need_to_visit = [[] for _ in range(V + 1)]
#     for v, w in nodes:
#         need_to_visit[w].append(v)
#     # print(need_to_visit)
#
#     visited = [0] * (V + 1)
#     stack = []
#
#     answer = []
#
#     start_points = []
#     for i in range(1, V + 1):
#         for row in adj_list:
#             if i in row:
#                 break
#         else:
#             start_points.append(i)
#     # print(start_points)
#
#     s = 0
#     v = start_points[s]
#     visited[v] = 1
#     answer.append(v)
#     while True:
#         if need_to_visit[v]:
#             v = need_to_visit[v][0]
#             answer.append(v)
#             # print(v)
#         for w in adj_list[v]:
#             if not visited[w] and len(need_to_visit[w]) <= 1:
#                 visited[w] = 1
#                 answer.append(w)
#                 # print(w)
#                 remove_visited_in_need_to_visit_list(v)
#                 stack.append(v)
#                 v = w
#                 break
#             elif not visited[w] and len(need_to_visit[w]) > 1:
#                 remove_visited_in_need_to_visit_list(v)
#                 # s += 1
#                 # v = s
#                 v = need_to_visit[w][0]
#                 visited[v] = 1
#                 answer.append(v)
#                 break
#         else:
#             if stack:
#                 v = stack.pop()
#             else:
#                 break
#
#     print(f"#{t}", *answer)

# from collections import deque
#
# for t in range(1, 11):
#     # 정점 개수, 간선 개수
#     V, E = map(int, input().split())
#     # 간선 정보
#     nodes = list(map(int, input().split()))
#     # 간선 정보는 간선을 이루는 두 정점으로 표기
#     # 이 문제에서는 부모노드를 먼저 방문해야 하므로 부모-자식 관계에 대한 리스트 만들기
#     # 정점 번호가 1~V까지의 정수 값
#     in_degree = [0] * (V+1)
#     graph = [[] for _ in range(V+1)]
#
#     for i in range(0, len(nodes), 2):
#         v, w = nodes[i], nodes[i+1]
#         graph[v].append(w) # 일방향이므로 이렇게 한 방향으로만 넣기
#         in_degree[w] += 1 # 진입차수 증가시키기
#
#     Q = deque()
#     # 진입 차수가 0인 노드를 큐에 추가 = 부모가 없는 노드 큐에 추가
#     for i in range(1, V+1):
#         if in_degree[i] == 0:
#             Q.append(i)
#
#     # 방문 순서 저장하는 리스트
#     result = []
#
#     while Q:
#         v = Q.popleft()
#         result.append(v)
#
#         for w in graph[v]:
#             in_degree[w] -= 1
#             if in_degree[w] == 0:
#                 Q.append(w)
#
#     print(f"#{t}", *result)

from collections import deque

for t in range(1, 11):
    V, E = map(int, input().split())
    nodes = list(map(int, input().split()))

    adj_list = [[] for _ in range(V+1)]
    in_degree = [0] * (V+1)
    for i in range(0, len(nodes), 2):
        v, w = nodes[i], nodes[i+1]
        adj_list[v].append(w)
        in_degree[w] += 1

    Q = deque()
    for i in range(1, V+1):
        if in_degree[i] == 0:
            Q.append(i)

    while Q:
        v = Q.popleft()
        print("pop ", v)
        for w in adj_list[v]:
            print("decrease in_degree of ", w, "whose parent is ", v)
            in_degree[w] -= 1
            if in_degree[w] == 0:
                print("now ", w, " is in queue")
                Q.append(w)

    print(f"#{t}")
