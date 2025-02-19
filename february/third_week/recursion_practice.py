# N과 M (1)
# 1부터 N까지 자연수 중 중복 없이 M개 고른 수열
# def permutation(depth):
#     if depth == M:
#         print(*answer)
#         return
#
#     else:
#         for i in range(1, N + 1):  # 1부터 N까지의 수를 순회하면서
#             if not visited[i]:  # 방문한 적 없는 수에 대해
#                 visited[i] = 1  # 방문했다고 체크 및 answer 리스트에 삽입
#                 answer.append(i)  # 방문했다 안했다로 각각의 경우의 수가 만들어질 것임
#
#                 permutation(depth + 1)  # 다음 재귀 호출
#
#                 visited[i] = 0  # 재귀 호출 후 원상복귀 (백트래킹)
#                 answer.pop()
#
#
# # N = 자연수 범위의 끝, M = 수열 길이
# N, M = map(int, input().split())
#
# # 순열 = 서로 다른 n개의 원소 중 r개를 선택 후 순서 고려하여 나열하는 경우의 수
# # nPr
# # 문제에서 중복 없이 M개를 고르는 경우의 수열들을 물었음
# # visited 리스트를 사용하여 같은 숫자를 여러 번 선택하는 것을 방지 → 중복 없는 순열 생성
# # 만약 중복 순열을 만들고 싶다면 visited를 제거하고, answer 리스트에 바로 추가하면 됨
#
# visited = [0] * (N + 1)
# answer = []
# permutation(0)


# N과 M 2
# 1부터 N까지 자연수 중 중복 없이 M개를 고른 오름차순 수열

def permutation(depth):
    if depth == M:
        print(*answer)
        return
    else:
        for i in range(1, N+1):
            if len(answer) >= 1 and answer[-1] >= i:
                continue

            answer.append(i)
            permutation(depth + 1)
            answer.pop()

N, M = map(int, input().split())
answer = []
permutation(0)