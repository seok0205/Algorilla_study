T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = min(arr)
    max_num = max(arr)
    min_num_idx = arr.index(min_num)
    max_num_idx = 0
    for i in range(N-1, -1, -1):
        if arr[i] == max_num:
            max_num_idx = i
            break

    print(f"#{t} {abs(max_num_idx - min_num_idx)}")