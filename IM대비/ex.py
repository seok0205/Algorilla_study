T = int(input())
for t in range(1, T + 1):
    arr = list(input().split())
    N = int(arr[0])

    O_list = []  # 오렌지가 눌러야 하는 버튼 목록
    B_list = []  # 블루가 눌러야 하는 버튼 목록

    for i in range(1, len(arr), 2):
        if arr[i] == 'O':
            O_list.append(int(arr[i + 1]))
        else:
            B_list.append(int(arr[i + 1]))

    # 현재 위치
    idx_O, idx_B = 1, 1
    time = 0
    O_time, B_time = 0, 0  # 각각 로봇의 다음 버튼까지의 소요 시간

    while O_list or B_list:
        time += 1  # 1초 경과

        # 오렌지 이동
        if O_list and idx_O < O_list[0]:  
            idx_O += 1
        elif O_list and idx_O > O_list[0]:
            idx_O -= 1

        # 블루 이동
        if B_list and idx_B < B_list[0]:  
            idx_B += 1
        elif B_list and idx_B > B_list[0]:
            idx_B -= 1

        # 오렌지가 버튼을 누를 수 있는 경우
        if O_list and idx_O == O_list[0] and O_time == 0:
            O_list.pop(0)
            O_time = 1  # 버튼을 누르는 1초

        # 블루가 버튼을 누를 수 있는 경우
        if B_list and idx_B == B_list[0] and B_time == 0:
            B_list.pop(0)
            B_time = 1  # 버튼을 누르는 1초

        # 버튼을 눌렀으면 다음 명령을 위해 카운트 조정
        if O_time > 0:
            O_time -= 1
        if B_time > 0:
            B_time -= 1

    print(f'#{t} {time}')
