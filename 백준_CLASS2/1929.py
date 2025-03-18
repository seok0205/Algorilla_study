import sys
# M이상 N이하의 소수를 모두 출력
M, N = map(int, sys.stdin.readline().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:  # i가 소수이면
        for j in range(i * i, N + 1, i):
            is_prime[j] = False  # i의 배수는 소수가 아님

for num in range(M,N+1):
    if is_prime[num]:
        print(num)
        