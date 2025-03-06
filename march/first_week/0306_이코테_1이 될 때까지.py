'''
N이 1이 될 때까지 N-1 또는 N / K 수행
최소 수행 횟수 출력

17 4
(output) 3

25 5
(output) 2
'''

# 마지막으로 남은 수에 대해 1씩 빼는 과정이 빠짐
# N이 K로 나누어 떨어질 때까지 1씩 빼는 과정이 빠짐
N, K = map(int, input().split())
count = 0
while N != 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1
print(count)
