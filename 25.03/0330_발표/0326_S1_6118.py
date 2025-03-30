'''
S1 6118 숨바꼭질

농장에 헛간이 많이 널려있고 그 중 하나에 숨어야 함
헛간의 개수는 N개(2이상 20000이하), 1부터 셈.

술래가 1번 헛간부터 찾을 것을 알고 있음. 모든 헛간은 M(1이상 50000이하)개의 양방향 길로 이루어져 있고,
그 양 끝을 A_i, B_i로 나타냄. 또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능.

냄새가 지독해서 최대한 냄새가 안나게 숨을 장소 찾을것임
냄새는 1번 헛간에서의 거리(지나야 하는 길의 최소 개수)가 멀어질수록 감소.
냄새를 최대한 숨길 수 있는 헛간을 찾는 문제

입력:
N, M 공백 사이 두고 주어짐
M줄동안 A_i, B_i가 공백 사이 두고 주어짐

출력:
한줄로 이루어지고, 세 개의 값을 공백으로 구분지어 출력
숨어야 하는 헛간 번호(여러개면 가장 작은 헛간 번호), 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간 개수
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def bfs(s):                     # bfs 활용
    visit = [0] * (N+1)
    q = deque([s])
    visit[s] = 1
    
    while q:
        target = q.popleft()
        for i in connect[target]:
            if visit[i] == 0:
                visit[i] = visit[target] + 1        # 퍼져나갈 때마다 1씩 증가해서 이동한 거리 visit에 저장
                q.append(i)
    
    return visit        # 방문 리스트 반환


N, M = map(int, input().split())
connect = [[] for _ in range(N+1)]

for _ in range(M):                          # 간선 정보 생성
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)
    
visit = bfs(1)

distance = max(visit)       # 1번 헛간부터 퍼져나간 최대 거리 저장
barn_cnt = 0                # 최대 거리 가진 헛간 개수 저장할 변수

for i in range(N, 0, -1):       # 끝에서부터 세면 마지막 저장 i가 같은 거리 중 가작 작은 헛간 번호임
    if visit[i] == distance:
        barn_cnt += 1           # 숨을 수 있는 헛간 개수 증가
        barn_num = i            # 마지막 저장 헛간 번호가 가장 작은 번호
        
print(barn_num, distance - 1, barn_cnt)     # 경로가 하나일 때 이동 간선 개수는 총 노드 - 1