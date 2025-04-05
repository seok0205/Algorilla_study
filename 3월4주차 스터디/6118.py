# N개의 정점, M개의 간선
# 1번부터 시작
# 숨어야되는 정점(같으면 가장 작은 번호), 정점까지 거리, 같은 거리 가지는 정점의 수 출력
import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque([s])
    visited = [0] * (N+1)
    visited[s] = 1
    
    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next]:
                continue
            else:
                visited[next] = visited[now] + 1
                q.append(next)
    
    num = 0
    max_len = max(visited)
    count = visited.count(max_len)
    for i in range(1, N+1):
        if visited[i] == max_len:
            num = i 
            break
        
    return num, max_len - 1, count

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
a, b, c = bfs(1)
print(a, b, c)