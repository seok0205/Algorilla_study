## 🎯 22375. 스위치 조작
```python
T = int(input())
for t in range(1, T+1):
    num_of_lights = int(input())
 
    before = list(map(int, input().split())) # 초기 상태
    after = list(map(int, input().split())) # 조작 후 상태
 
    idx = 0
    count = 0
    while before != after: # 둘이 같아질 때 까지
        compare = list(zip(before, after)) # 이렇게 풀긴했는데 지금 보니 굳이 zip으로..?
 
        before_val = compare[idx][0]
        after_val = compare[idx][1]
 
        if before_val != after_val:
            for i in range(num_of_lights-1, idx-1, -1): # 지금 보니 이것도 굳이 뒤에서부터...?
                before[i] = 1 if before[i] == 0 else 0
            count += 1
            idx = 0 # 지금 보니 이것도 굳이 왜 초기화..?
            if before == after:
                break
        else:
            idx += 1
 
    print(f"#{t} {count}")
```

## 🎯 20397. 돌 뒤집기 게임 2
```python
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # 돌의 수 N, 뒤집기 횟수 M
    default_arr = list(map(int, input().split())) # 돌들의 초기 상태
    task_arr = [list(map(int, input().split())) for _ in range(M)] # 뒤집기할 돌 순서와 개수 받아오기
 
    m = 0 # 뒤집기 카운트
    while m < M: # 뒤집기 횟수와 같아질 때 까지
        curr_idx = task_arr[m][0] - 1
        idx_to_move = task_arr[m][1]
        curr = default_arr[curr_idx]
        for i in range(1, idx_to_move+1):
            right_idx = curr_idx + i
            left_idx = curr_idx - i
            # 오른쪽과 왼쪽이 배열을 벗어나지 않고 마주보는 돌들이 같은 색일 때 
            if 0 <= right_idx < N and 0 <= left_idx < N and default_arr[right_idx] == default_arr[left_idx]:
                if default_arr[right_idx] == 0:
                    default_arr[right_idx] = 1
                    default_arr[left_idx] = 1
                else:
                    default_arr[right_idx] = 0
                    default_arr[left_idx] = 0
        m += 1
 
    print(f"#{t}",  *default_arr)
```

## 🎯 18575. 풍선팡 보너스 게임
```python
T = int(input())
for t in range(1, T+1):
 
    N = int(input())
    matrix =[list(map(int, input().split())) for _ in range(N)]
 
    # 현재 위치 값 빼고는 현재 위치의 행과 열의 합은 항상 같으므로 정보를 만들고 시작
    rows_sum_arr = [sum(row) for row in matrix] # 행 합은 sum으로 바로 구할 수 있음
    cols_sum_arr = [0 for _ in range(N)] # 열 합은 순회를 돌면서 구함
    for i in range(N):
        col_sum = 0
        for j in range(N):
            col_sum += matrix[j][i]
        cols_sum_arr[i] = col_sum
 
    max_sum = 0
    min_sum = rows_sum_arr[0] + cols_sum_arr[0] # 최솟값은 첫 번째 값으로 설정
 
    curr_sum = 0
    for i in range(N):
        for j in range(N):
            curr = matrix[i][j]
            curr_sum = rows_sum_arr[i] + cols_sum_arr[j] - curr # 행 합과 열 합에는 현재 위치 값이 중복되므로 빼주기
            max_sum = max(max_sum, curr_sum)
            min_sum = min(min_sum, curr_sum)
 
    print(f"#{t} {max_sum - min_sum}")
```

## 🎯 3499. 퍼펙트 셔플
```python
T = int(input())
for t in range(1, T+1):
 
    N = int(input())
    cards = list(input().split())
 
    middle = N // 2 if N % 2 == 0 else N // 2 + 1 # 홀수일 때 먼저 놓는 쪽에 한 장 더 들어가게 해야 해서
 
    first_deck = cards[:middle] # 먼저 놓는 카드 덱
    second_deck = cards[middle:] # 나중에 놓는 카드 덱
    first_len = len(first_deck)
    second_len = len(second_deck)
 
    result = []
 
    i = 0
    while i < N:
        if first_len > i:
            result.append(first_deck[i])
 
        if second_len > i:
            result.append(second_deck[i])
 
        i += 1
 
    print(f"#{t}", *result)
```

## 🎯 1979. 어디에 단어가 들어갈 수 있을까
지난 주에 했으므로 패쓰

## 🎯 1959. 두 개의 숫자열
```python
def get_result(bigger_num, smaller_num, bigger_arr, smaller_arr): # 긴 리스트를 기준으로 짧은 리스트 구간만큼 비교해주면 됨
    max_result = 0
    for i in range(bigger_num - smaller_num + 1):
        sub_B = bigger_arr[i:i + smaller_num]
        result = sum([(a * b) for a, b in zip(smaller_arr, sub_B)])
        max_result = max(result, max_result)
    return max_result

T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        max_result = get_result(M, N, B, A)
    else:
        max_result = get_result(N, M, A, B)

    print(f"#{t} {max_result}")
```

## 🎯 1244. 스위치 켜고 끄기
```python
num_of_switches = int(input())
switches_arr = list(map(int, input().split()))
num_of_students = int(input())
students_arr = [list(map(int, input().split())) for _ in range(num_of_students)]

for student in students_arr:
    gender, given_num = student[0], student[1]
    if gender == 1: # 남자면
        for i in range(num_of_switches): # 스위치 번호가 받은 번호의 배수인지 확인 위해
            if (i + 1) % given_num == 0: 
                switches_arr[i] = 0 if switches_arr[i] == 1 else 1 # 1이면 0으로, 0이면 1로
    elif gender == 2: # 여자면
        curr_idx = given_num - 1
        count = 0 # 카운트라고 썼지만 사실 좌우가 대칭인 길이
        for i in range(1, num_of_switches): # 좌우가 대칭이면서 가장 많은 스위치 포함하는 구간 찾기 위해
            right_idx = curr_idx + i
            left_idx = curr_idx - i
            if 0 <= right_idx < num_of_switches and 0 <= left_idx < num_of_switches: # 인덱스 에러 피하기 위해 
                if switches_arr[right_idx] != switches_arr[left_idx]: # 좌우가 대칭이 아니면 끝내기
                    break
                else:
                    count += 1
            else:
                break

        for i in range(curr_idx-count, curr_idx+count+1): # 좌우가 대칭인 구간에 스위치 상태 바꾸기 (자기자신 포함)
            switches_arr[i] = 0 if switches_arr[i] == 1 else 1

for i, val in enumerate(switches_arr, start=1):
    print(val, end=" ")
    if i % 20 == 0: # 20개가 될 때마다 20번째 것 출력 후 줄바꿈
        print()
```