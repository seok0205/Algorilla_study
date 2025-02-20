# 마름모 모양으로 전부 더해라!
T = int(input())
for t in range(1, T+1):
    # N은 항상 홀수
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 가운데 행을 기준으로 잡고 한칸씩 벌어져 나가볼까
    # 가운데 행은 더하고 시작
    mid = N//2
    result = sum(arr[mid])
    # 가운데 행 기준 한칸씩 멀어질때마다 더하는 열이 2씩 감소
    for i in range(N//2):
        for k in range(N - 2 - (2*i)):
            result += arr[mid-i-1][k+i+1]
            result += arr[mid+i+1][k+i+1]
    
    print(f'#{t} {result}')
    