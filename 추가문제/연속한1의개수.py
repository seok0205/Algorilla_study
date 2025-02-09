T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))

    count_1 = 0     # 연속된 1의 횟수
    max_count_1 = 0 # 연속된 1의 횟수 중 최댓값
    cnt_list = []   # 연속된 1의 횟수를 저장할 리스트

    # 연속된 1의 횟수 구하기
    for i in range(N):
        # arr[i]가 1일 때
        if arr[i] == 1:
            count_1 += 1    # count_1에 1을 더하고
            cnt_list.append(count_1)    # cnt_list에 count_1 저장

        # arr[i]가 0일 때
        if arr[i] == 0:
            count_1 = 0 # count_1을 0으로 초기화

    # 연속된 1의 횟수 중 최댓값 구하기
    for j in range(len(cnt_list)):
        if max_count_1 < cnt_list[j]:
            max_count_1 = cnt_list[j]

    
    print(f'#{test_case} {max_count_1}')