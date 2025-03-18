T = int(input())
for t in range(1, T+1):
    # 수업을 들어야 하는 일수
    n = int(input())
    arr = list(map(int ,input().split()))
    # 우선 수업이 있는 날의 수 계산
    count = sum(arr)
    # 몇 주동안 들어야 하는지 계산(일수 계산 위해 * 7)
    result = 7 * (n // count)
    
    # 딱 떨어지면 뒤에서 부터 마지막 1이 언제인지 계산
    temp = n % count
    if temp == 0:
        for i in range(6, -1, -1):
            if arr[i] == 1:
                result -= (7 - i)
                break
    # 잔여 일수가 있으면 앞에서 부터 계산해서 수업이 있는 날에 잔여 이수 차감
    # 잔여 일수 없을 때까지 탐색후 result에 더해준다.
    else:
        for i in range(7):
            result += 1
            if arr[i] == 1:
                temp -= 1
                if temp == 0:
                    break
                
    print(f'#{t} {result}')