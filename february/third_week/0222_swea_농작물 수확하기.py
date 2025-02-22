'''
1
1
3
output = 3

1
3
132
254
021
output = 16

1
5
05023
33212
12511
23321
24132
output = 25 (6+10+8+1)

1
7
3200021
1000023
3001023
0000004
1010033
3203112
1032100
output = 17 (3+4+4+4+2)

1
5
14054
44250
02032
51204
52212
output = 23
'''

from _collections import deque

T = int(input())
for t in range(1, T+1):
    N = int(input())
    values = [list(map(int, input())) for _ in range(N)]

    center = N // 2

    visited = [[0 for _ in range(N)] for _ in range(N)]
    Q = deque()
    Q.append((center, center))
    visited[center][center] = 1

    total_revenue = 0

    while Q:
        row, col = Q.popleft()
        total_revenue += values[row][col]

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            next_r = row + di
            next_c = col + dj
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c] and visited[row][col] <= N // 2:
                Q.append((next_r, next_c))
                visited[next_r][next_c] = visited[row][col] + 1

    print(f"#{t} {total_revenue}")
