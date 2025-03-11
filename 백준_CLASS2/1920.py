# a : 찾는 값
def binsearch(a):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == a:
            return 1
        elif arr[middle] > a:
            end = middle - 1
        else:
            start = middle + 1
    return 0
         
N = int(input())
arr = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

arr.sort()

# 이진탐색
for num in check:
    print(binsearch(num))