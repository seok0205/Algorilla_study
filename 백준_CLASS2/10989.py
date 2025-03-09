N, K = map(int, input().split())
result = 1
temp = 1
for i in range(K):
    result *= N
    temp *= K
    N -= 1
    K -= 1
result = result // temp

print(result)