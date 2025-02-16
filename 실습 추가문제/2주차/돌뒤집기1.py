T = int(input())
for t in range(1, T+1):
    # N : 돌의 개수, M : 돌을 뒤집는 경우
    N, M = map(int, input().split())
    # i 번째 돌부터 j개를 i번째 돌과 같은 모양으로 뒤집는다
    # 돌의 초기 상태
    arr = list(input().split())
    # i, j
    case = [list(map(int, input().split())) for _ in range(M)]
    for q in range(M):
        i = int(case[q][0])   # 뒤집어야 되는 돌의 위치
        j = int(case[q][1])   # 몇개 뒤집어야 되는지
        for k in range(j-1):
            if i+k<len(arr) and arr[i-1] != arr[i+k]:
                arr[i+k] = arr[i-1]
    result = ' '.join(arr)
    print(f'#{t} {result}')