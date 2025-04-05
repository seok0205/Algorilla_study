import sys
input = sys.stdin.readline

# 계단의 수
N = int(input().strip())

# 계단별 점수
arr = [int(input().strip()) for _ in range(N)]

# 예외 처리: 계단이 1개 또는 2개인 경우
if N == 1:
    print(arr[0])
    sys.exit()
elif N == 2:
    print(arr[0] + arr[1])
    sys.exit()

# dp 배열 초기화
dp = [0] * N
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

# dp 점화식 적용
for i in range(3, N):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(dp[N-1])
