# 3kg, 5kg 설탕 봉지 있음
# 최소로 들고가는 개수
# 정확히 N킬로 못 만들면 -1출력
# 무게
N = int(input())
a = 5
b = 3
count = 1e5
result = -1
for i in range(N//5 + 1):
    temp = i
    num = N
    num -= 5*i
    if num % 3 != 0:
        continue
    else:
        temp += num // 3
        result = 0
    if temp < count:
        count = temp
if result != -1:
    print(count)
else:
    print(result)