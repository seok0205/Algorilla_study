# N, M, K를 공백으로 구분해서 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 리스트로 받기
data = list(map(int, input().split()))

data.sort(reverse=True) # 받은 데이터를 정렬(원본 data변경)
first = data[0]
second = data[1]

result = 0

while m > 0:
    for i in range(k):   # 가장 큰 수를 k 번 더한다
        if m == 0:       # m 이 0 이라면 반복문 탈출
            break
        result += first
        m -= 1
    result += second      # 두번째로 큰 수를 한 번 더한다
    m -= 1

print(result)


# 입력값
# 5 8 3
# 2 4 5 6 3