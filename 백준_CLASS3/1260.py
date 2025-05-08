import sys
from collections import deque
input = sys.stdin.readline
'''
DFS, BFS로 탐색한 결과를 출력하는 프로그램 작성.
방문가능한 정점 여러개면 정점번호 작은거부터 방문 1번부터 N번
방문 가능한 점이 없는 경우 종료
'''
def dfs(V:int):
    visited = [0] * (N+1)
    stack = [V]
    result = []
    while stack:
        r = stack.pop()
        if not visited[r]:
            visited[r] = 1
            result.append(r)
            for num in reversed(graph[r]):
                if not visited[num]:
                    stack.append(num)    
    return result

def bfs(V:int):
    q = deque()
    q.append(V)
    visited = [0] * (N+1)
    visited[V] = 1
    result = [V]
    while q:
        r = q.popleft()
        for num in graph[r]:
            if visited[num]:
                continue
            q.append(num)
            visited[num] = 1
            result.append(num)
   
    return result
    

# 정점 개수, 간선 개수, 시작할 정점의 번호
N, M, V = map(int, input().split())
# 간선은 양방향
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i].sort()
    
result_dfs = dfs(V)
result_bfs = bfs(V)
print(*result_dfs)
print(*result_bfs)