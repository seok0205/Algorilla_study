import sys
# 동전의 종류, 만들어야될 가치의 합
N, K = map(int, sys.stdin.readline().split())
# 동전 종류
arr = list(int(sys.stdin.readline().strip()) for _ in range(N))
# 최소동전 사용해서 목표 가치 만들어라
count = 0
for i in range(N-1, -1, -1):
    if arr[i] > K:
        continue
    
    temp = 1
    flag = False
    while True:
        if K - arr[i]*temp >= 0:
            temp += 1
            flag = True
        else:
            break
        
    if flag:
        count += (temp - 1)
        K -= (temp-1) * arr[i]
        
    if K == 0:
        break

print(count)