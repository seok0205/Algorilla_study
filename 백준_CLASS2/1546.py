# M : 점수의 최댓값
N = int(input())
arr = list(map(int, input().split()))
new = []

result = 0

max_s = max(arr)
for i in range(N):
    new.append(arr[i]/max_s*100)
    
for i in range(N):
    result += new[i]
result = result / N
print(result)