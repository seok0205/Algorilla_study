T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = arr[0]
    min_value = arr[0]
    max_idx = 0
    min_idx = 0

    for i in range(N):
        # 최댓값 구하기
        if max_value <= arr[i]:
            max_value = arr[i]
            max_idx = i

        # 최솟값 구하기
        if min_value > arr[i]:
            min_value = arr[i]
            min_idx = i

    # 최댓값, 최솟값 위치 차이 구하기
    result = abs(max_idx - min_idx)

    print(f'#{test_case} {result}')
