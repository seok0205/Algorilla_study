import sys
# kruskal 사용
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
        
    return p[x]

def union(x, y):
    rep_x = find_set(x) ; rep_y = find_set(y)
    
    # 대표자가 같으면 return
    if rep_x == rep_y:
        return

    if rank[rep_x] > rank[rep_y]:
        p[rep_y] = rep_x
    elif rank[rep_x] < rank[rep_y]:
        p[rep_x] = rep_y
    else:
        if rep_x < rep_y:
            p[rep_x] = rep_y
            rank[rep_y] += 1
        else:
            p[rep_y] = rep_x
            rank[rep_x] += 1

# 한 컴터가 바이러스 걸리면
# 그 컴터랑 연결된 모든 컴터 바이러스 걸림
# 1번 컴터 바이러스 걸림
# 몇대의 컴터가 바이러스 걸리게 되는가

# 컴터의 수
V = int(sys.stdin.readline())
# 간선의 수
E = int(sys.stdin.readline())

p = [i for i in range(V+1)]
rank = [0] * (V+1)

for _ in range(E):
    x, y = map(int, sys.stdin.readline().split())
    if find_set(x) == find_set(y):
        continue
    else:
        union(x, y)
        
for i in range(1, V+1):
    p[i] = find_set(p[i])

result = p.count(p[1]) - 1
print(result)
