'''
적다  적당하다  많다
V-1  VlogV  V**2
9999 130000 100000000

주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소일 때의 가중치 합 출력

6 9
1 2 9
1 3 4
1 4 3
1 5 1
2 4 4
2 5 5
3 6 6
4 5 2
4 6 8
> 17

1. pypy로 제출하니 메모리 에러가 생겼는데 재귀함수를 쓰게 되면 실제 코테에서 pypy로 제출 못하는 건지 궁금하다
2. Python에서는 기본적으로 재귀 호출의 최대 깊이(limit)가 1000으로 설정
  -> 1000번 이상 호출되면 RecursionError(최대 재귀 깊이 초과 오류)가 발생
  재귀 깊이가 깊어지는 알고리즘(DFS, Union-Find, DP 등)을 사용할 때
  sys.setrecursionlimit(10**6)을 설정해서 재귀 한계를 늘려주기
'''
import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()  # 이걸 안넣으니까 확실히 느림, 없어도 맞긴 함

def find_root(x):
    if parents[x] != x:
        parents[x] = find_root(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_root(x)
    root_y = find_root(y)

    if root_x == root_y:
        return

    if root_x > root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


V, E = map(int, input().split())
parents = [i for i in range(V + 1)]
edges = []
for _ in range(E):
    A, B, W = map(int, input().split()) # -1000000 < W < 1000000
    edges.append((A, B, W))
edges.sort(key=lambda x: x[2])
count = 0
weights = 0
for A, B, W in edges:
    if find_root(A) != find_root(B):
        union(A, B)
        count += 1
        weights += W

        # if count == V - 1:
        #     break

print(weights)
