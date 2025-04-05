import sys
def find_set(x):
    if x != p[x]:
        return find_set(p[x])
    return p[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return
    
    if rep_x < rep_y:
        p[rep_x] = rep_y
    else:
        p[rep_y] = rep_x

# 그래프가 주어질 때, 그 그래프의 최소 스패팅 트리를 구해라
V, E = map(int, sys.stdin.readline().split())
graph = []
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    graph.append((w, s, e))

# 가중치 기준 정렬
graph.sort(key= lambda x : x[0])

count = 0
min_dis = 0
p = [i for i in range(V+1)]
for w, s, e in graph:
    if find_set(s) == find_set(e):
        continue
    else:
        union(s, e)
        count += 1
        min_dis += w
        
    if count == V-1:
        break
print(min_dis)