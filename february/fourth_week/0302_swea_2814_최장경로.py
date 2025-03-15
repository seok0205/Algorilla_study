# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     adj_list = [[] for _ in range(N+1)]
#     for _ in range(M):
#         x, y = map(int, input().split())
#         adj_list[x].append(y)
#         adj_list[y].append(x)
#     max_counts = 0
#     stack = []
#     for node in range(1, N+1):
#         visited = [0] * (N+1)
#         stack.append(node)
#         visited[node] = 1
#         counts = 1
#         # curr = node
#         while stack:
#             curr = stack.pop()
#             for neighbor in adj_list[curr]:
#                 if not visited[neighbor]:
#                     counts += 1
#                     visited[neighbor] = 1
#                     stack.append(neighbor)
#                     curr = neighbor
#                     break
#
#         if counts > max_counts:
#             max_counts = counts
#     print(f"#{t} {max_counts}")


def dfs(curr_node, visited, counts):
    global max_counts

    visited[curr_node] = 1
    max_counts = max(max_counts, counts)

    for neighbor in adj_list[curr_node]:
        if not visited[neighbor]:
        # visited[neighbor] = 1
            dfs(neighbor, visited, counts + 1)
    visited[curr_node] = 0

T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 정점 수, M: 간선 수
    adj_list = [[] for _ in range(N + 1)]  # 인접 리스트

    # 간선 정보 입력받기
    for _ in range(M):
        x, y = map(int, input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)  # 양방향 간선 추가

    max_counts = 0  # 최장 경로의 길이를 추적하는 변수

    for node in range(1, N+1):
        dfs(node, [0] * (N+1), 0)

    print(f"#{t} {max_counts}")