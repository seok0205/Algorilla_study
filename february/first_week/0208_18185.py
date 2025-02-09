# N개의 라면 공장, 1-N번까지, i번공장에서 Ai개 라면 구매 예정
# 1 0 1 -> 1번공장에서 라면 1개, 2번공장에서 라면 0개, 3번공장에서 라면 1개
# 살 수 있는 법:
# i번공장에서 하나 구매 = 3원 / i, i+1번공장에서 라면 각각 하나 구매 = 5원 / i, i+1, i+2 각각 하나 구매 = 7원
# [2, 3, 2, 1] -> 7원 [1, 2, 1, 1] -> 7원 [0, 1, 0, 1] -> 6원 [0,0,0,0] : 21
# [2, 3, 2, 1] -> 5원 [1, 2, 2, 1] -> 7원 [0, 1, 1, 1] -> 7원 [0,0,0,0] : 19

# TODO: 시간초과로 다시 한 번 풀어봐야 함!

# N = int(input())
# arr = list(map(int, input().split()))
#
# cost = 0
# i = 0
# while i < N:
#
#     if i + 2 < len(arr) and arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
#         cost += 7
#         arr[i] -= 1
#         arr[i+1] -= 1
#         arr[i+2] -= 1
#         continue
#
#     if i + 1 < len(arr) and arr[i] > 0 and arr[i+1] > 0:
#         cost += 5
#         arr[i] -= 1
#         arr[i + 1] -= 1
#         continue
#
#     if arr[i] > 0:
#         cost += 3
#         arr[i] -= 1
#         continue
#
#     i += 1
#
# print(cost)

def buy_two(i, min_value):
    arr[i] -= min(arr[i], min_value)
    arr[i+1] -= min_value
    global cost
    cost += 5 * min_value

def buy_three(i, min_value):
    arr[i] -= min_value
    arr[i+1] -= min_value
    arr[i+2] -= min_value
    global cost
    cost += 7 * min_value

def buy_one(i, min_value):
    arr[i] -= min_value
    global cost
    cost += 3 * min_value

N = int(input())
arr = list(map(int, input().split()))

cost = 0
sum_arr = sum(arr)
for i in range(N):
    if i < N-2 and arr[i+1] > arr[i+2] and arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
        buy_two(i, arr[i+1] - arr[i+2])
        buy_three(i, min(arr[i], arr[i+1], arr[i+2]))
        buy_one(i, arr[i])
    elif i < N - 1 and arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
        buy_three(i, min(arr[i], arr[i+1], arr[i+2]))
        buy_two(i, min(arr[i], arr[i+1]))
        buy_one(i, arr[i])
    else:
        buy_one(i, arr[i])

print(cost)