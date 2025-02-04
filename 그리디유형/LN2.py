# Large Number 다른 풀이법
n, m, k = map(int, input().split())
list = list(map(int, input().split()))

list.sort(reverse=True)
first = list[0]
second = list[1]

# 수열을 만들어서 first의 값이 몇번 들어갈지 계산하는 방식
count = 0   # first의 값이 몇번 들어갈지 체크
count += m//(k+1) * k  
count += m%(k+1)

result = 0

result += count * first
result += (m-count) * second

print(result)

# 입력값
# 5 8 3
# 2 4 5 6 3