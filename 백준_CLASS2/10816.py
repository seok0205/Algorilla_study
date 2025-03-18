# from sys import stdin

# # 1 ~ 500,000, 숫자 카드 개수
# N = int(stdin.readline())
# arr1 = sorted(map(int, stdin.readline().split()))
# M = int(stdin.readline())
# arr2 = list(map(int, stdin.readline().split()))

# for i in range(M):
#     if arr1[0] <= arr2[i] <= arr1[-1]:
#         count = 0
#         for num in arr1:
#             if num == arr2[i]:
#                 count += 1
#             if count and num != arr2[i]:
#                 break    
#         arr2[i] = count
#     else:
#         arr2[i] = 0
        
# print(*arr2)

from sys import stdin
_ = stdin.readline()
arr1 = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
arr2 = list(map(int,stdin.readline().split()))
index, m_dic = 0, {}

for m in sorted(arr2):
    cnt = 0
    if m not in m_dic:
        while index < len(arr1):
            if m == arr1[index]:
                cnt += 1; index += 1
            elif m > arr1[index]:
                index += 1
            else: break
        m_dic[m] = cnt

print(' '.join(str(m_dic[m]) for m in arr2))