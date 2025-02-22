T = int(input())
for t in range(1, T+1):
    # 초기 배열
    arr = list(map(int, input()))
    N = len(arr)
    
    ini = [0] * N
    count = 0
    for i in range(N):
        if arr[i] != ini[i]:
            if arr[i] == 1:
                count += 1
                for k in range(i, N):
                    ini[k] = 1
            else:
                count += 1
                for k in range(i, N):
                    ini[k] = 0
    print(f'#{t} {count}')