T = int(input())
for t in range(T):
    # k 층, n 호, 최대 14층, 14호까지 있음
    k = int(input())
    n = int(input())
    arr = [0] * 14
    for i in range(14):
        arr[i] = i+1
    
    for i in range(k):
        for j in range(1, n):
            arr[j] = arr[j-1] + arr[j]
    print(arr[n-1]) 