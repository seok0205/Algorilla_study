# 카드 3장을 합해서 M을 넘으면 안됨
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# arr.sort()
# a, b, c = 0, 0, 0
# temp = []
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             a, b, c = arr[i], arr[j], arr[k]
#             if a + b + c <= M:
#                 temp.append(a+b+c)
# temp.sort()
# print(temp[-1])
    
# 부분집합으로 다시 풀어보자

sub_set = []
for i in range(1<<N):
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp.append(arr[j])
    if len(temp) == 3:  
        sub_set.append(temp)

temp = []
for i in sub_set:
    a, b, c = i
    if a + b + c <= M:
        temp.append(a + b + c)
result = max(temp)
print(result)
        