'''
S1 14889 스타트와 링크

축구 위해 모인 사람 N명, N은 짝수.
N/2 명으로 이루어진 스타트팀과 링크팀으로 사람을 나눠야 함.

1부터 N까지 배정. 능력치 조사를 함.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치임.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합.
Sij는 Sji와 다를 수도 있고, i번 사람과 j번 사람이 같은 팀에 속햇을 때 팀에 더해지는 능력치는 Sij, Sji임.

스타트 팀의 능력치와 링크 팀의 능력치 차이를 최소로 하려 함.
능력치 차이의 최솟값을 출력.

입력:
N : 짝수, 총 인원
N개 줄에 S가 주어짐(조합마다 점수를 담은 배열)
모든 점수는 0보다 크고 100보다 작거나 같은 정수. (i, i)는 0
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def make_team(cnt, idx):            # dfs 함수
    global result

    if cnt == N//2:         # 하나의 경우의 수 구해지면 팀 별 점수 차이 구하기
        team1 = 0
        team2 = 0

        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:       # 방문 한 곳이면 첫번째팀에
                    team1 += synergy[i][j]
                elif visit[i] == 0 and visit[j] == 0:       # 안한 곳이면 두번째팀에
                    team2 += synergy[i][j]
        
        result = min(result, abs(team1-team2))
        return
    
    else:                                   # 팀을 구성하기 전까지는 경우의 수 구하기
        for i in range(idx, N):
            if visit[i] == 0:
                visit[i] = 1
                make_team(cnt+1, i+1)
                visit[i] = 0


N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]

visit = [0] * N             # 경우의 수 구하기 위한 방문리스트
result = float('inf')       # 최솟값 구해야 하니까 엄청 높은 값으로 초기화

make_team(0, 0)

print(result)