import sys
# 듣도 못한 사람 수, 보도 못한 사람 수
N, M = map(int, sys.stdin.readline().split())
arr1 = set(sys.stdin.readline().strip() for _ in range(N))
arr2 = set(sys.stdin.readline().strip() for _ in range(M))
result = arr1.intersection(arr2)
result = list(result)
result.sort()
print(len(result))
for word in result:
    print(word)