import sys
sys.stdin.readline
# N+1일에 퇴사
N = int(input())
# 상담하는데 걸리는 시간, 페이
info = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * 25
# dp에는 현재까지 가장 최대로 벌 수 있는 것을 기록
now_max = 0
for i in range(N):
    day, pay = info[i]
    
    dp[i+1] = max(dp[i+1], dp[i])
    
    if N - i >= day:
        dp[i+day] = max(dp[i+day], dp[i] + pay)
 
print(dp[N])