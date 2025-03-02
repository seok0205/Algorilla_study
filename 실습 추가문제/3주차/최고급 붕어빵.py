def result(time, timeline):
    for i in time:
        if timeline[i] < 1:
            return 'Impossible'
        else:
            for j in range(11112):
                timeline[j] -= 1
    return 'Possible'

T = int(input())
for t in range(1, T+1):
    # N : 사랑 수, M초의 시간동안 K개의 붕어빵 만들 수 있다.
    N, M, K = map(int, input().split())
    # N명의 사람이 언제 도착하는지
    time = list(map(int, input().split()))
    time.sort()

    # 0으로 된 배열 쌓은 다음
    # 각 초마다 붕어빵 개수 세어 높음(적립식)
    # 그 시간에 사람이 오면 붕어빵 카운트 줄인다.
    timeline = [0] * 11112
    count = 0
    for i in range(0, 11112, M):
        for j in range(M):
            if (i+j) < 11112:
                timeline[i+j] += K*count
        count += 1
    # print(timeline)
    
    answer = result(time, timeline)
    
    print(f'#{t} {answer}')
