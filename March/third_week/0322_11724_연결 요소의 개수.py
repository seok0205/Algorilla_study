

import sys

input = lambda: sys.stdin.readline().rstrip()

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


N, M = map(int, input().split())
parents = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    if find_root(a) != find_root(b):
        union(a, b)
        # print(a, b, parents)
# print("before : ", parents)

for i in range(1, N+1):  # 유니온으로 호출 안 된 노드들도 대표자 업데이트 필요하므로 모든 노드에 대해 한 번 더 대표자 정리
    find_root(i)

# print("after : ", parents)

answer = set()
for entry in parents:
    if entry != 0:
        answer.add(entry)
# print(answer)
print(len(answer))
