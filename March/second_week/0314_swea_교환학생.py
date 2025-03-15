
# 리스트로 구현
# def find_attending_days(start_idx):
#     global answer
#
#     count = 0
#     times = 0
#     idx = start_idx
#     while True:
#         if count == days:
#             break
#         if class_info[idx]:
#             count += 1
#         idx = (idx + 1) % 7
#         times += 1
#     answer = min(answer, times)
#     return
#
#
# T = int(input())
# for t in range(1, T + 1):
#     days = int(input())
#     class_info = list(map(int, input().split()))
#     answer = float('inf')
#
#     for i in range(7):
#         if class_info[i]:
#             find_attending_days(i)
#
#     print(f"#{t} {answer}")

# 비트마스킹으로 구현 - 위 코드와 아래 코드의 실행 시간에 차이는 거의 없었음
def find_attending_days(start_idx):   # 수업이 있다면 그 날부터 언제까지 참여해야 참여해야 하는 일수를 만족하는지 구한다
    global answer
    count = 0   # 수업을 참여하는 횟수를 카운트
    times = 0   # 며칠 연속으로 있어야 하는지 카운트
    idx = start_idx

    while count < days:
        if (class_mask >> idx) & 0x1:   # 시작 인덱스부터 왼쪽으로 밀면서 1과 비교한다
            count += 1
        times += 1
        idx = (idx + 1) % 7   # 일주일 이상 걸릴 수 있으므로 모듈러 연산으로 일주일 내에서 반복할 수 있게 한다

    answer = min(answer, times)

T = int(input())
for t in range(1, T + 1):
    days = int(input())
    class_info = list(map(int, input().split()))
    answer = float('inf')
    # 리스트를 이진수라고 보고 십진수를 구한다 다만 맨 왼쪽부터 시작하므로 해당 십진수를 이진수로 바꾸면 리스트 값을 거꾸로 한 것과 같다
    class_mask = sum((class_info[i] << i) for i in range(7))
    for i in range(7):
        # 해당 이진수를 왼쪽으로 밀며 1과 비교한다 = 수업이 있는 날을 찾는다
        if (class_mask >> i) & 0x1:
            find_attending_days(i)

    print(f"#{t} {answer}")