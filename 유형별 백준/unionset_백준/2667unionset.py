import sys
input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)
    if rep_x != rep_y:
        if rep_x < rep_y:
            p[rep_y] = rep_x
        else:
            p[rep_x] = rep_y

N = int(input().strip())
arr = [list(input().strip()) for _ in range(N)]

size = N * N
p = [i for i in range(size)]

# 인접한 집끼리 union 수행 (오른쪽, 아래쪽만 확인)
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            idx = i * N + j
            # 오른쪽 체크
            if j + 1 < N and arr[i][j + 1] == '1':
                union(idx, i * N + (j + 1))
            # 아래쪽 체크
            if i + 1 < N and arr[i + 1][j] == '1':
                union(idx, (i + 1) * N + j)

# 각 단지(집단)의 크기를 계산 (단, 집인 경우만)
complexes = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            idx = i * N + j
            root = find_set(idx)
            if root in complexes:
                complexes[root] += 1
            else:
                complexes[root] = 1

# 결과 출력: 단지 수, 그리고 각 단지 내 집의 개수를 오름차순 정렬
result = sorted(complexes.values())
print(len(result))
for count in result:
    print(count)
