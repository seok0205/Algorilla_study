'''
0초부터 붕어빵 만들기 시작
M초의 시간동안 K개의 붕어빵 만듦
N명의 사람에게 제공
모든 사람에게 기다리는 시간 없이 제공 가능하면 Possible, 아니면 Impossible 출력

1
74 60 97
59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 59 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 60 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61
'''

# T = int(input())
# for t in range(1, T + 1):
#     # N명의 손님, M초마다 K개 만들 수 있음
#     N, M, K = map(int, input().split())
#     # 각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타냄
#     queue = sorted(list(map(int, input().split())))
#     print(f"{N}명의 손님, {M}초 마다 {K}개 만들 수 있음. 손님이 도착하는 초: {queue}")
#     answer = "Possible"
#     done = 0
#     seconds = 0
#     for customer in queue:
#         if customer < M:
#             answer = "Impossible"
#             break
#
#     if answer == "Possible":
#         while queue:
#             seconds += 1
#             if seconds % M == 0:
#                 done += K
#             for customer in queue:
#                 if customer == seconds and done:
#                     queue.pop(0)
#                     done -= 1
#                 elif customer == seconds and not done:
#                     answer = "Impossible"
#                     break
#             if answer == "Impossible":
#                 break
#
#     print(f"#{t} {answer}")

from collections import deque

T = int(input())
for t in range(1, T + 1):
    # N명의 손님, M초마다 K개 만들 수 있음
    N, M, K = map(int, input().split())
    # 각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타냄
    queue = deque(sorted(list(map(int, input().split()))))
    seconds = 0
    done = 0
    last_time = 0
    answer = "Possible"
    while queue:
        seconds = queue[0]
        if seconds >= M:
            done += ((seconds - last_time) // M) * K  # 추가 생산
            last_time = (seconds // M) * M  # 마지막으로 빵을 만든 시간을 M 배수로 설정

        while queue and queue[0] == seconds:
            queue.popleft()
            done -= 1
            if done < 0:
                answer = "Impossible"
                break

        if answer == "Impossible":
            break

    print(f"#{t} {answer}")