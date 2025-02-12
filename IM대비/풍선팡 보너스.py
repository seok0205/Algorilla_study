T = int(input())
for t in range(1, T+1):
    # N x N 행렬
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    temp = 0
    for i in range(N):
        for j in range(N):
            temp += sum(arr[i])
            for k in range(N):
                temp += arr[k][j]
            temp -= arr[i][j]      # 본인 자리는 2번 더해짐    
            result.append(temp)
            temp = 0
    result.sort()
    print(f'#{t} {result[-1] - result[0]}')



