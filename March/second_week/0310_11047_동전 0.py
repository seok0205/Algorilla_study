# N: 동전 종류 / K: 동전의 합
# K원 만드는 데 필요한 동전의 최소 개수
# 시간 초과 코드
# N, K = map(int, input().split())
# coins = []
# count = 0
# for _ in range(N):
#     coins.append(int(input()))
# for coin in coins[::-1]:
#     if K <= 0:
#         break
#     while K >= coin:
#         K -= coin
#         count += 1
# print(count)

# 정답 코드
N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N):
    coins.append(int(input()))
for coin in coins[::-1]:
    if K == 0:
        break
    while K >= coin:
        count += (K // coin)
        K -= (coin * (K // coin))
print(count)