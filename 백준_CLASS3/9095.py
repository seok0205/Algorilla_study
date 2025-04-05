# 1,2,3의 합으로 어떠한 정수를 만드는 방법의 수 찾기
# 순서도 상관이 있다.(순열)
import sys

def recur(i):
    global count

    if i > n:
        return
    
    if i == n:
        count += 1
        return
    
    recur(i+1)
    recur(i+2)
    recur(i+3)

input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    count = 0

    recur(0)
    print(count)

    # dp
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7

    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    print(dp[n])
    