# 수열에서 연속된 1이 최대가 되는 수 구하기
T = int(input())
for t in range(1, T+1):
    N = int(input())     # 수열의 길이
    num_list = list(map(int, input()))   # 0과 1로 구성된 리스트

    count = 0
    max_count = 0

    for i in num_list:
        if i == 1:
            count += 1
            if count > max_count:    # count 가 max_count보다 크면 
                max_count = count    # max_count 를 count 값으로 변경
        else:
            count = 0                # 만약 0이 나오면 count를 다시 0으로 바꿔준다.
    print(f'#{t} {max_count}')
