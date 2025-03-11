N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

rank = []

for i in range(N):
    temp = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            temp += 1
    rank.append(temp)
print(*rank)