T = int(input())
for t in range(1, T+1):
    # 각 배열의 길이
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    # 항상 arr1이 길이가 긴 값을 가지게 설정
    if len(arr1) < len(arr2):  
        arr1, arr2 = arr2, arr1

    # N > M     
    N, M = len(arr1), len(arr2)

    result = 0
    for k in range(N - M + 1):
        temp = 0
        for q in range(M):
            temp += arr1[k+q] * arr2[q]
        if temp > result:
            result = temp
     
    print(f'#{t} {result}')