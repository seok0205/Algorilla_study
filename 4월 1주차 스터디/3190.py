# 벽 또는 자기 자신과 부딪히면 게임이 끝난다!
# 사과는 2로 표시할거
from collections import deque
import sys
input = sys.stdin.readline

# 얘가 방향을 바꿔야되는 명령인지?
def f(num):
    if num in info.keys():
        return info[num]
    else:
        return 0

# 좌표 넣으면 방향에 따라 다음 좌표가 어딘지 반환해주는 함수
def next_node(i, j, w):
    if w%4 == 0:
        return (i, j+1)
    elif w%4 == 1:
        return (i+1, j)
    elif w%4 == 2:
        return (i, j-1)
    else:
        return (i-1, j)

# 보드의 크기
N = int(input())
# 사과의 개수
K = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 2
# 방향 변환 횟수
L = int(input())
# 몇초뒤에 어느 방향으로 회전하는지 ( L : 왼쪽으로 회전, D : 오른쪽으로 회전 )
info = {}
for i in range(L):
    a, b = input().split()
    info[int(a)] = b

# 현재 뱀의 위치는 1로 표시
arr[0][0] = 1

# 방향
w = 0
# 몇초만에 끝나는지 결과
result = 0
# 현재 지렁이의 몸위치를 모두 q에 넣는다.
q = deque()
q.append((0, 0))

# 지렁이 대가리 위치
r, c = 0, 0
while True:
    result += 1
    nr, nc = next_node(r, c, w)
    # 벽에 부딪히면 종료
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        break
    # 만약 지렁이 몸을 만나면 종료
    if arr[nr][nc] == 1:
        break
    # 만약 사과 만나면 몸 길이 늘려준다.
    elif arr[nr][nc] == 2:
        arr[nr][nc] = 1
        q.append((nr, nc))
        r, c = nr, nc
    # 사과가 아니라 그냥 땅이면 원래 있던 부분 0으로 만들고 앞으로 나아감
    else:
        x, y = q.popleft()
        arr[x][y] = 0
        arr[nr][nc] = 1
        q.append((nr, nc))
        r, c = nr, nc
        
    next_way = f(result)
    if next_way == 'D':
        w += 1
    elif next_way == 'L':
        w -= 1 

print(result)


