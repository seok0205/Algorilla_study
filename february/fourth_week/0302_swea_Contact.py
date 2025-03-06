'''
24 2
100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2
100 17 | 39 22 | 100 8 | 100 7 | 7 100 | 2 7 | 2 15 | 15 4 | 6 2 | 11 6 | 4 10 | 4 2

24 2
11 6 6 2 4 2 4 10 2 15 15 4 2 7 7 1 1 7 1 8 1 17 3 22
'''
from collections import deque


for t in range(1, 11):
    data_len, start = map(int, input().split())
    nodes = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]
    for i in range(0, data_len, 2):
        v, w = nodes[i], nodes[i+1]
        adj_list[v].append(w)
    visited = [0 for _ in range(101)]
    answer = None
    Q = deque()
    Q.append(start)
    visited[start] = 1
    while Q:
        curr = Q.popleft()
        for neighbor in adj_list[curr]:
            if not visited[neighbor]:
                visited[neighbor] = visited[curr] + 1
                Q.append(neighbor)
    max_val = max(visited)
    for idx in range(len(adj_list)-1, 0, -1):
        if visited[idx] == max_val:
            answer = idx
            break

    print(f"#{t} {answer}")