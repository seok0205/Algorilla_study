N = int(input())
arr = [int(input()) for _ in range(N)]
sorted_arr = sorted(arr, reverse=True)
total_price = 0
for i in range(2, N, 3):
    # if len(sorted_arr[i:i+3]) == 3:
    #     total_price += (sum(sorted_arr[i:i+3]) - sorted_arr[i+2])
    # else:
    #     total_price += sorted_arr[i]
    total_price += sorted_arr[i]

print(sum(sorted_arr) - total_price)