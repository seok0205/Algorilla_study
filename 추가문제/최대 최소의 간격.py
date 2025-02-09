T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_value = 11
    max_value = 0

    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    for i in range(N):
        if arr[i] == min_value:
            min_index = i + 1
            break

    for i in range(N - 1, -1, -1):
        if arr[i] == max_value:
            max_index = i + 1
            break

    result = abs(max_index - min_index)
    print(f"#{t} {result}")
