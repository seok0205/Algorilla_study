'''
S2 11724 연결 요소의 개수

방향 없는 그래프가 주어졌을 때, 연결 요소(Connected Component)의 개수를 구하는 프로그램 작성

입력:
첫줄 N(정점 개수), M(간선 개수)
둘째줄 M개 줄에 간선의 양 끝점 u, v. 같은 간선은 한번만 주어짐
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    n_num = [i for i in range(n+1)]
    return parents, ranks, n_num


def find_set(x):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    
    if ref_x == ref_y:
        return
    
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


N, M = map(int, input().split())            # 유니온파인드 알고리즘 활용
parents, ranks, n_num = make_set(N)
result = 0
for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)
    
for i in range(1, N+1):         # 대표자 수 찾으면 연결요소 개수
    if parents[i] == n_num[i]:
        result += 1

print(result)