import sys
input = sys.stdin.readline
'''
N : 짝수, 각 사람마다 1부터N까지 번호가 메겨져있음.
i, j번 사람이 같은 팀이 될때 시너지가 생긴다.(100이하의 정수)
팀 능력이는 이러한 시너지들의 합(양방향으로 더해짐)
각 팀 능력치의 차이가 최소가 되게 할때, 그 최솟값을 출력
'''
# 번호가 리스트에 담겨 주어졌을 때, 두 팀의 능력치 차이를 반환해주는 함수
def diff(temp:list):
    second = []
    for i in range(N):
        if i not in temp:
            second.append(i)
    a, b = 0, 0
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            a = a + arr[temp[i]][temp[j]] + arr[temp[j]][temp[i]]
            b = b + arr[second[i]][second[j]] + arr[second[j]][second[i]]
    return abs(a - b)

def recur(dep, cnt, temp:list):
    global result
    # 그러고 count도 같이 들고 들어가서 count가 N//2가 되면 return시키자
    if cnt == N // 2:
        now = diff(temp)
        result = min(result, now)        
        return
    if dep == N:
        return
    # 현재 cnt를 선택하고 들어가자
    recur(dep+1, cnt+1, temp+[dep])
    
    # 현재 cnt를 선택하지 않고 들어가자
    recur(dep+1, cnt, temp)
    
N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]
# N//2개를 선택하면 선택 종료하고 나머지는 자동 팀 완성 
# 모든 팀을 다 만들어서 시너지 계산해보자
result = 1e10
recur(0, 0, [])
print(result)