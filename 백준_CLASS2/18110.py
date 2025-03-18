import sys

# 입력 받기
n = int(sys.stdin.readline())

# 예외 처리: n == 0이면 난이도 0 출력
if n == 0:
    print(0)
    sys.exit()

# 난이도 의견 리스트 입력받고 정렬
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

# 제외할 개수 (반올림)
del_num = round(n * 0.15)

# 모든 값이 제외되는 경우 방지
valid_count = n - del_num * 2
if valid_count <= 0:
    print(0)
    sys.exit()

# 절사 평균 계산
num = sum(arr[del_num:n - del_num])
print(round(num / valid_count))
