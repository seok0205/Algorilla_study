def ch_int(arr):
    return arr[0]

N = int(input())
arr = []
for i in range(N):
    age, name = input().split()
    arr.append([int(age),name])

arr.sort(key=ch_int)
for i in arr:
    print(*i)