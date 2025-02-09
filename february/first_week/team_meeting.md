## 🎯 11092. 최대 최소의 간격
```python
T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T+1):  # # 각 테스트 케이스 실행
    N = int(input())  # 정수 개수 입력
    arr = list(map(int, input().split()))  # N개의 정수를 리스트로 저장

    # 1️⃣ 최대값 찾기
    max_num = max(arr)  # 배열에서 최대값 찾기
    max_num_id = 0  # 최대값의 위치 변수 초기화

    # 최대값이 여러 개 있을 경우, 마지막으로 나오는 위치 찾기
    for i in range(N-1, -1, -1):  # 배열을 끝에서부터 탐색
        if arr[i] == max_num:  # 최대값을 발견하면
            max_num_id = i  # 해당 인덱스를 저장
            break  # 가장 마지막에 나오는 최대값이므로 더 이상 탐색할 필요 없음

    # 2️⃣ 최소값 찾기
    min_num = min(arr)  # 배열에서 최소값 찾기
    min_num_id = arr.index(min_num)  # 최소값이 처음 등장하는 위치 찾기

    # 3️⃣ 두 위치의 차이를 절대값으로 출력
    print(f"#{t} {abs(max_num_id - min_num_id)}")
```

## 🎯 9386. 연속한 1의 개수
```python
T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T+1):  # 각 테스트 케이스 실행
    N = int(input())  # 수열의 길이 입력
    arr = list(map(int, input()))  # 공백 없이 제공된 0과 1로 이루어진 수열을 리스트로 변환

    # 1️⃣ 카운팅 소트 사용 - 연속된 1의 개수를 저장할 배열과 변수 초기화
    count_arr = [0 for _ in range(N)]  # 각 길이별 연속된 1의 개수를 저장할 배열
    answer = 0  # 최대 연속 1의 개수
    counts = 0  # 현재 연속된 1의 개수

    # 2️⃣ 수열을 돌면서 연속된 1의 개수 찾기
    for num in arr:
        if num == 1:  
            counts += 1  # 1이 연속되면 증가
        else:  
            count_arr[counts] += 1  # 연속된 1의 개수를 배열에 저장
            counts = 0  # 연속이 끊어졌으므로 초기화
    count_arr[counts] += 1  # else로 안끊긴 연속된 1의 개수를 저장

    # 3️⃣ 가장 큰 연속된 1의 개수 찾기
    for i in range(N-1, -1, -1):  # 배열을 뒤에서부터 탐색
        if count_arr[i]:  # 값이 존재하면
            answer = i  # 최대 연속된 1의 개수 업데이트
            break  # 가장 큰 값을 찾았으므로 종료

    # 4️⃣ 결과 출력
    print(f"#{t} {answer}")
```

## 🎯 6485. 삼성시의 버스 노선
```python
T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T+1): # 각 테스트 케이스 실행
    N = int(input())  # 버스 노선 개수 입력
    
    # 1️⃣ 카운팅 소트 사용 - 버스 노선 입력 및 카운트 배열 업데이트
    count_arr = [0] * 5001  # 정류장마다 지나는 버스 개수를 저장할 배열 초기화
    for _ in range(N):
        A, B = map(int, input().split())  # 버스 노선 범위 입력
        for i in range(A, B+1):  # 해당 범위 내 정류장의 카운트 증가
            count_arr[i] += 1
    
    # 2️⃣ 카운트 배열에서 결과 확인
    P = int(input())  # 확인할 버스 정류장 개수 입력
    result = []  # 결과 저장 리스트

    for _ in range(P):
        C = int(input())  # 특정 버스 정류장 번호 입력
        result.append(str(count_arr[C]))  # 나중에 결과 출력 형식을 생각하여 해당 정류장을 지나는 버스 개수를 스트링으로 받아 추가
    
    # 3️⃣ 결과 출력
    print(f"#{t} {' '.join(result)}")

```

## 🎯 1979. 어디에 단어가 들어갈 수 있을까
```python
# 퍼즐의 하얀 부분 개수 세는 함수
def count_white_part(N, K, arr): # 퍼즐 크기 N, 찾으려는 단어 길이 K, 확인할 퍼즐 배열을 인자로 받음
    counts = 0 # 카운트 초기화
    
    # 왼쪽에서 오른쪽으로 탐색
    for i in range(N):
        for j in range(N - K + 1): # K 길이만큼 연속된 1이 있는지 확인하려는데 인덱스 범위 에러가 나지 않기 위해 N-K+1로 설정
            if sum(arr[i][j:j+K]) == K: # 흰색 부분은 값이 1이므로 해당 배열의 합이 찾으려는 단어 길이와 같은지 비교
                counts += 1 # 찾으려는 단어 길이와 같다면 카운트 증가
    
    return counts

T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T + 1): # 각 테스트 케이스 실행
    N, K = map(int, input().split())  # N: 퍼즐 크기, K: 찾으려는 단어 길이 입력
    matrix = [list(map(int, input().split())) for _ in range(N)]  # 퍼즐 배열 입력
    
    # 1️⃣ 세로 방향으로 확인하기 위해 배열 전처리
    zipped_matrix = list(map(list, zip(*matrix)))
    
    # 2️⃣ 가로 방향과 세로 방향 모두 확인
    answer = count_white_part(N, K, matrix) + count_white_part(N, K, zipped_matrix)
    
    # 3️⃣ 결과 출력
    print(f"#{t} {answer}")
```

## 🎯 1974. 스도쿠 검증
```python
T = int(input())  # 테스트 케이스 개수 입력
for t in range(1, T + 1): # 각 테스트 케이스 실행
    matrix = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 퍼즐 배열 입력
    
    is_wrong = False  # 잘못된 스도쿠인지 확인하는 변수

    # 카운팅 소트 사용
    # 1️⃣ 각 행에서 1~9 숫자가 중복되는지 체크
    for i in range(9):
        counts = [0] * 10  # 숫자 카운트 배열 (조건문에서 0보다 크다는 등의 조건 달기 귀찮아서 10 사이즈로 설정. 1~9에 대해서만 체크할 것임)
        for j in range(9):
            counts[matrix[i][j]] += 1  # 해당 숫자 카운트
        if counts[1:].count(0) > 0:  # 1~9까지 모든 숫자가 한 번씩 나와야 하는데 0인 게 있으면 틀린 것
            is_wrong = True # 틀렸다고 변수 설정
            break  # 잘못된 퍼즐이 있으면 더 이상 확인할 필요 없으므로 루프 빠져나오기

    # 2️⃣ 각 열에서 1~9 숫자가 중복되는지 체크
    if not is_wrong: # 각 행에서 중복되는 게 없다면
        zipped_matrix = list(map(list, zip(*matrix)))  # 열을 확인하기 위해 배열 전처리
        for i in range(9):
            counts = [0] * 10  # 숫자 카운트 배열
            for j in range(9):
                counts[zipped_matrix[i][j]] += 1
            if counts[1:].count(0) > 0:  # 1~9까지 모든 숫자가 한 번씩 나와야 하는데 0인 게 있으면 틀린 것
                is_wrong = True # 틀렸다고 변수 설정
                break # 잘못된 퍼즐이 있으면 더 이상 확인할 필요 없으므로 루프 빠져나오기

    # 3️⃣ 3x3 블록에서 1~9 숫자가 중복되는지 체크
    if not is_wrong:
        for i in range(3):
            for j in range(0, 7, 3):  # 3x3 블록의 왼쪽 위 위치
                counts = [0] * 10  # 숫자 카운트 배열
                for k in range(3):  # 3개의 행
                    for l in range(3):  # 3개의 열
                        counts[matrix[i*3 + k][j + l]] += 1
                if counts[1:].count(0) > 0:  # 1~9까지 모든 숫자가 한 번씩 나와야 하는데 0인 게 있으면 틀린 것
                    is_wrong = True # 틀렸다고 변수 설정
                    break # 잘못된 퍼즐이 있으면 더 이상 확인할 필요 없으므로 루프 빠져나오기
            if is_wrong: # break는 하나의 for loop만 빠져나오므로 하나 더 추가
                break

    # 4️⃣ 결과 출력 (잘못된 퍼즐이면 0, 아니면 1)
    answer = 0 if is_wrong else 1
    print(f"#{t} {answer}")
```