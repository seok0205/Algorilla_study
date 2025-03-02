# 두 로봇은 서로 다른 복도에 있으며
# 1번 버튼부터 시작한다.
T = int(input())
for t in range(1, T+1):
    arr = list(input().split())
    # 눌러야하는 버튼의 수
    N = int(arr[0])
    
    dict = {'O' : [], 'B' : []}
    # 입력받은 배열 순회해서 어떤 버튼을 먼저 눌러야 하는지 딕셔너리에 리스트로 저장
    for i in range(1, len(arr), 2):
       dict[arr[i]].append([i, int(arr[i + 1])])  # (입력 순서, 목표 버튼 위치) 저장


    # 총 걸리는 시간
    count = 0
    # 현재 위치 인덱스
    idx_O , idx_B = 1, 1

    temp_O = (abs(dict['O'][0][1] - idx_O) + 1) if dict['O'] else 0
    temp_B = (abs(dict['B'][0][1] - idx_B) + 1) if dict['B'] else 0

    for _ in range(N):
        if not dict['O']:  # 오렌지 명령이 남아있지 않다면 블루만 처리
            count += temp_B
            idx_B = dict['B'][0][1]
            del dict['B'][0]
            temp_B = (abs(dict['B'][0][1] - idx_B) + 1) if dict['B'] else 0
            continue

        if not dict['B']:  # 블루 명령이 남아있지 않다면 오렌지만 처리
            count += temp_O
            idx_O = dict['O'][0][1]
            del dict['O'][0]
            temp_O = (abs(dict['O'][0][1] - idx_O) + 1) if dict['O'] else 0
            continue

        # 오렌지가 먼저 버튼을 눌러야 하면
        if dict['O'][0][0] < dict['B'][0][0]:
            count += temp_O
            idx_O = dict['O'][0][1]
            del dict['O'][0]
            temp_O = (abs(dict['O'][0][1] - idx_O) + 1) if dict['O'] else 0
            temp_B = max(temp_B - temp_O, 1)  # 블루가 기다린 시간 고려

        else:  # 블루가 먼저 버튼을 눌러야 하면
            count += temp_B
            idx_B = dict['B'][0][1]
            del dict['B'][0]
            temp_B = (abs(dict['B'][0][1] - idx_B) + 1) if dict['B'] else 0
            temp_O = max(temp_O - temp_B, 1)  # 오렌지가 기다린 시간 고려

    print(f'#{t} {count}')