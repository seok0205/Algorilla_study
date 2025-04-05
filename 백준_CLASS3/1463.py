import sys
# 전형적인 dp문제 주석처리는 하지 않고 나중에 다시 풀어보기
N = int(sys.stdin.readline())

dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[N])
