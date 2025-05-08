# 하루에 하나씩 서로 다른 사람의 상담
# 최대 수익은?
# dp문제인거 같은데 점화식을 한번 세워보자..
def recur(cnt, s):
    global result

    if (cnt, s) in memo:
        return
    
    result = max(result, s)
    
    for i in range(cnt, N):
        day, pay = info[i]
        next_day = i + day
        if next_day <= N:
            recur(next_day, s + pay)
    
    memo[(cnt, s)] = result
    
import sys
sys.stdin.readline
# N+1일에 퇴사
N = int(input())
# 상담하는데 걸리는 시간, 페이
info = [list(map(int, input().split())) for _ in range(N)]

result = 0
memo = {}
recur(0, 0)
print(result)