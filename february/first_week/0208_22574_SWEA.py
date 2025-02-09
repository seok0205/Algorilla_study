# SWEA D3 22574. 높은 곳으로

# 0 - 10^9층까지의 빌딩
# P층에는 폭탄 - 멈추면 안 됨
# N번의 기회, i (1 <= i <= N) 번째 선택에서
# 엘베 가만 둘지 위로 i층 올릴지 결정
# x층 -1) x층 머무르기 -2) x+i층에 멈추기
# 모든 N번의 선택이 끝났을 때 있을 수 있는 가장 높은 층 번호 구하기

T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    curr = 0
    for increment in range(1, N + 1):
        if curr + increment == P:
            curr += increment - 1
            # curr += (N-1)
        else:
            curr += increment
    print(curr)
