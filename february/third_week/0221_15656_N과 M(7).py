# 같은 수 여러 번 골라도 됨, 수열은 오름차순으로 출력

def permutation(depth, arr):
    if depth == M:
        print(*result)
        return
    else:
        for i in range(N):
            result.append(arr[i])
            permutation(depth + 1, arr)
            result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
permutation(0, sorted(arr))
