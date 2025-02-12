T = int(input())
for t in range(1, T+1):
    N = int(input())   # 당근의 개수
    # 당근의 크기
    arr = list(map(int, input().split()))
    arr.sort()
    result = 10000000     # 최대와 최소의 차이
    for i in range(1, N-1):   # 첫번째 자를 구간 설정
        if arr[i] == arr[i-1]:  # 자른곳과 그 전의 값이 같으면 계속 진행
            continue
        for j in range(i+1, N):  # 두번째 자를 구간 설정
            if arr[j-1] == arr[j]:  # 자른곳과 그 전의 값이 같으면 계속 진행
                continue
            group1 = i              
            group2 = j - i
            group3 = N - j
            # 3그룹중 가장 큰 값이 문제 조건과 맞지 않으면 계속 진행
            if max(group1,group2,group3) > (N//2):   
                continue
            # 모든 조건 통과 시 그룹의 최댓값과 최솟값의 차이 구해서
            # 현재 result와 비교
            gap =  max(group1,group2,group3)-min(group1,group2,group3)
            if gap < result:
                result = gap
    # 모든 경우를 그냥 지나치면 원래 설정값이 나옴(실패)
    if result == 10000000:   
        print(f'#{t}', -1)
    else:
        print(f'#{t} {result}')