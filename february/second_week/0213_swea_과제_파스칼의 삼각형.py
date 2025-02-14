# def pascal(num, i, arr):
#     # result = 0
#     arr = [[] for _ in range(num)]
#     arr[0] = [1]
#     arr[1] = [1, 1]
#     if len(arr) > num:
#         return
#
#     else:
#         arr[i] = [0 for _ in range(i+1)]
#         arr[i][0] = arr[i][-1] = 1
#         for j in range(0, i-1):
#             arr[i][j+1] = sum(arr[j:j+i-1])
#         # return arr
#         # return pascal(num, i+1, arr + [arr[i]])
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#
#     print(pascal(N, 2, []))
#
#     print(f"#{t}")


# def myprint(n, i, j, arr, count=1):
#     my_result = []
#
#     if i > n:
#         return
#
#     my_result.append(count)
#     print(count, end=" ")
#
#     if j == i:
#         print()
#         print(my_result)
#         myprint(n, i+1, 1, 1, arr + my_result)
#
#     else:
#         count = 0 if j+1 == 3 else 1
#         myprint(n, i, j + 1, count, arr)
#
# n = 10
# myprint(n, 1, 1, [])
#
# # def pascal()

# def arithmetic(a, d, n):
#     return [a + i * d for i in range(n)]
#
# aritmetic_arr = arithmetic(0, 1, 15)
# print(aritmetic_arr)
#
# arr = [1, 1, 1]
# array_len = 2
# for i in range(2, 15):
#     alpha = aritmetic_arr[i]
#     sub_array = [0 for _ in range(i+1)]
#     sub_array[0] = 1
#     sub_array[-1] = 1
#     for j in range(0, array_len-1):
#         sub_array[j+1] = sum(arr[array_len-1+alpha:array_len+1+alpha]) if array_len+1 < len(arr) else sum(arr[array_len-1:])
#     array_len += 1
#     arr += sub_array
#     # alpha +=
#     print(sub_array)

