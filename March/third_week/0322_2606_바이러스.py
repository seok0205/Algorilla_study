
def find_root(x):
    if parents[x] != x:
        parents[x] = find_root(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_root(x)
    root_y = find_root(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


N = int(input())
M = int(input())
parents = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if find_root(a) != find_root(b):
        union(a, b)

for i in range(1, N+1):
    find_root(i)

print(parents.count(1) - 1)
