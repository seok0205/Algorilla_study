T = int(input())
for t in range(1, T+1):
    H, W, N = map(int, input().split())
    a = N//H + 1
    b = N%H
    if N%H == 0:
        b = H
        a = N//H
    result = str(b*100+a)
    print(result)
