T = int(input())
for t in range(1, T+1):
    # N : 상자개수, Q : 뒤집는 횟수
    N, Q = map(int, input().split())
    # L부터 R 까지 뒤집음
    arr = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * N
    # i : 바꾸는 숫자
    for i in range(1, Q+1):
        L = arr[i-1][0]
        R = arr[i-1][1]
        for j in range(R-L+1):      
            box[j+L-1] = i
    
    print(f'#{t}', *box)
