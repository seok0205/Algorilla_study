# N: 여학생 수 / M: 남학생 수 / K: 대회 대신 인턴십 참여 인원
# 2명의 여학생 + 1명의 남학생 으로 팀 결성 필수
# 최대의 팀 수 구하기

# 틀린 코드 - 틀리거나 시간 초과일 때는 중요한 것 먼저 배분해보기
# 또는 0에서부터 시작해서 그 값을 만들기

# N, M, K = map(int, input().split())
# answer = 0
# if (M - K) * 2 >= (N // 2):
#     M -= K
#     answer = min((N // 2), M)
# else:
#     i = 1
#     while i < K:
#         N -= i
#         M -= (K - i)
#         if M >= (N // 2):
#             answer = N // 2
#             break
#         i += 1
#
# print(answer)

N, M, K = map(int, input().split())
team_count = 0
while True:
    N -= 2
    M -= 1
    if N >= 0 and M >= 0 and N + M >= K:
        team_count += 1
    else:
        break
print(team_count)
