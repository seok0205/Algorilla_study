T = int(input())
for t in range(1, T+1):
    N = int(input())      # 노선의 개수
    # A이상 B이하인 정류장을 다닌다
    # 각 행의 첫번째 열은 A, 두번째 열은 B
    arr1 = [list(map(int,input().split())) for _ in range(N)]  # 혹시 여기서 바로 A,B를 받을 수 있나요??
    P = int(input())   # 주어지는 정류장의 수
    # 각 정류장의 위치
    arr2 = [int(input()) for _ in range(P)]

    result = [0]*P

    for i in range(N):          # i+1번 노선이 도는 정류장을 카운트 
        A = arr1[i][0]
        B = arr1[i][1]
        for j in range(P):      # j+1번 정류장에서 그 노선이 지나가면 +1
            if A <= arr2[j] <= B:
                result[j] += 1


    print(f'#{t}', ' '.join(map(str, result)))
    # print(f'#{t}', *result)
