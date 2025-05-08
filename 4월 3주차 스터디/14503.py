import sys
input = sys.stdin.readline
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 현재 칸의 주변 4칸중 청소되지 않은 빈 칸이 없으면
def first(i, j, w):
    # 새로운 방향은 현재 바라보는 방향 +2한 후 4로 나눈 나머지(우하상좌이기 때문)
    n_w = (w+2)%4
    nr, nc = i + dr[n_w], j + dc[n_w]
    # 맵을 벗어나지 않으면
    if 0<=nr<N and 0<=nc<M and arr[nr][nc] != 1:
        return (nr, nc, w)
    # 이동이 불가능하면 현재 칸을 리턴
    return (-1, -1, -1)

# 현재 칸의 주변 4칸중 청소되지 않은 빈 칸이 있으면
def second(i, j, w):
    w = (w-1) % 4
    nr, nc = i + dr[w], j + dc[w]
    # 맵을 벗어나지 않으며 이동이 가능하면
    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
        return (nr, nc, w, True)
    return (i, j, w, False)


N, M = map(int, input().split())
# 현재 위치, 바라 보는 방향 -> 0, 1, 2, 3 : 북, 동, 남, 서
r, c, w = map(int, input().split())
# 1은 벽이고 0은 청소되지 않은 빈 칸
arr = [list(map(int, input().split())) for _ in range(N)]
count = 0
while True:
    if arr[r][c] == 0:
        arr[r][c] = 2
        count += 1

    cleaned = False
    for k in range(4):
        r, c, w, moved = second(r, c, w)
        if moved:
            cleaned = True
            break
    
    # 인접한 청소를 하지 않은 구역이 없으면
    if not cleaned:
        (nr, nc, nw) = first(r, c, w)
        r, c, w = nr, nc, nw
        if (r, c, w) == (-1, -1, -1):
            break

print(count)