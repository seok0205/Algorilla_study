'''
문제
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

입력
N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

출력
미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

예제 입력 1
30
예제 출력 1
30
'''
# 30의 배수가 되는 가장 큰 수: 0 포함, 각 자리 숫자의 합이 3의 배수, 큰 수부터 확인 (내림차순 정렬)
# 102 -> 210

N = list(input())
n = len(N)

# 수학적으로 구현
if '0' not in N:
    print(-1)
else:
    total = sum(map(int, N))
    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted(N, reverse=True)))

# 재귀로 구현
# def permute(arr, path, result):
#     if not arr:
#         # print(path)
#         result.append(path)
#         return result
#
#     for i in range(len(arr)):
#         permute(arr[:i] + arr[i+1:], path + [arr[i]], result)
#
# my_result = []
# permute(N, [], my_result)
# max_num = -1
#
# for nums in my_result:
#     nums_int = int(''.join(nums))
#     if nums_int < 30:
#         continue
#     elif nums_int % 30 == 0 and nums_int > max_num:
#         max_num = nums_int
# print(max_num)


# # 부분집합을 만들어서 하면 되려나 생각하며 한 접근
# # N = int(input())
# N = list(map(int, input()))
# # if N == 30:
# #     print(30)
# # else:
# arr = []
# for i in range(1<<len(N)):
#     subset = []
#     for j in range(len(N)):
#         if i & (1<<j):
#             subset.append(N[j])
#     print(subset)
#     arr.append(subset)
# print(arr)

