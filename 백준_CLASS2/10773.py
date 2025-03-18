# 잘못된 수를 부를 때마다 0을 외쳐서
# 가장 최근에 쓴 수를 지운다.
# 모든 수를 받아 적은 후 그 수의 합출력
K = int(input())
arr = []
for i in range(K):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
print(sum(arr))