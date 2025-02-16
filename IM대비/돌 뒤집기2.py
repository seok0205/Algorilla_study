T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # 돌의 현재 상태
    arr = list(input().split())
    case = [list(map(int, input().split())) for _ in range(M)]
    # 중심점이 되는 돌 : N 번째 돌
    for k in range(M):
        i = int(case[k][0])   # 가운데 돌의 위치
        j = int(case[k][1])   # 중심돌을 기준으로 몇번 체크 해야 되는지
        for p in range(j):
            # 현재 돌의 위치
            if i-p-2>=0 and i+p<len(arr) and arr[i-p-2] == arr[i+p]:
                if arr[i-p-2] == '1':
                    arr[i-p-2] = arr[i+p] = '0'
                else:
                    arr[i-p-2] = arr[i+p] = '1'
    result = ' '.join(arr)
    print(f'#{t} {result}')