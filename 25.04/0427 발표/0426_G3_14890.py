'''
G3 14890 경사로

NxN 지도가 있음. 지도 각 칸에는 그 곳의 높이가 적혀져 있음.

이 지도에서 지나갈 수 있는 길이 몇 개 있는지 확인해보려 함.
길이란 한 행 또는 한 열 전부를 나타내고, 한쪽 끝에서 다른쪽 끝까지 지나가는 것임.

길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 같아야 함.
경사로를 놓아서 지나갈 수 있는 길을 만들 수 있음.
경사로는 항상 높이가 1, 길이는 L임. 개수는 무한.
낮은 칸과 높은 칸 연결하고 아래 조건 만족해야 함.

조건:
1. 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 함.
2. 낮은 칸, 높은 칸의 차이는 1이여야함.
3. 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 함.

못 놓는 조건:
1. 경사로를 놓은 곳에 또 경사로를 놓는 경우
2. 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
3. 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
4. 경사로를 놓다가 범위를 벗어나는 경우

지도 주어지면 지나갈 수 있는 길의 개수를 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def check_can_go_row(list):     # 경사로를 깔아서 갈 수 있는지 확인하는 함수
    visit = [0] * N             # 경사로 깔았는지 표시할 방문 리스트

    for i in range(N-1):                # 인덱스 하나씩 확인
        if list[i] == list[i+1]:            # 만약 다음 값과 같으면 갈 수 있음
            continue
        else:
            if list[i] - list[i+1] == 1:        # 다음 높이가 1 낮다면
                if i+L < N:                     # 경사로 깔 길이를 만족하는지 확인. 만족못하면 못가는 길
                    if L == 1:                  # 경사로 길이가 1이면 다음 땅만 깔면 됨
                        visit[i+1] = 1
                    else:                       # 길이가 1이상이면
                        visit[i+1] = 1
                        for j in range(i+1, i+L):       # 그 앞의 길이 높이가 같은지 확인
                            if list[j] == list[j+1]:
                                visit[j+1] = 1
                            else:                       # 높이 다른 땅 나오면 못깜. 못가는 길 확정
                                return 0
                else:
                    return 0
            elif list[i] - list[i+1] == -1:     # 다음 높이가 1 높다면
                if i+1-L >= 0:                  # 경사로 깔 길이 만족하는 지 확인. 낮으면 이전 길을 확인해야함. 못하면 못가는 길
                    if visit[i]:        # 이미 경사로 깐 곳이면 못깜. 못 가는 길
                        return 0
                    
                    if L == 1:          # 경사로 길이 1이면 현재 자리를 방문했다고만 표시
                        visit[i] = 1
                    else:               # 경사로 길이 1 이상이면
                        visit[i] = 1
                        for j in range(i, i-L+1, -1):       # 이전 길 높이 같은지 모두 확인
                            if list[j] == list[j-1]:
                                if visit[j-1]:              # 같은 높이인데, 이미 경사로 깔아서 온 곳이면 경사로 설치 불가. 못 가는 길
                                    return 0
                                else:                       # 깔 수 있으면 깜
                                    visit[j-1] = 1
                            else:
                                return 0
                else:
                    return 0
            else:                   # 다음 값과 차이가 1이상나면 경사로 깔 수 없음. 못 가는 길
                return 0
    else:               # for문 return 없이 모두 이행하면 갈 수 있는 길
        return 1


def turn_right(arr):        # 배열을 돌려서 행, 열 모두 확인
    new_arr = list(map(list, zip(*list(arr[::-1][i] for i in range(N)))))
    return new_arr


N, L = map(int, input().split())

roads = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(N):      # 행 확인
    cnt = check_can_go_row(roads[i])
    result += cnt

new_roads = turn_right(roads)       # 열을 확인하기 위해 90도 회전

for i in range(N):      # 행으로 바뀐 열 확인
    cnt = check_can_go_row(new_roads[i])
    result += cnt

print(result)       # 갈 수 있는 길 확인