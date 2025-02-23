'''
D3 2805 농작물 수확하기

NxN크기 농장 존재. 규칙이 있음

1. 농장 크기는 항상 홀수
2. 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태만 가능

농장 크기 N, 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익 구하는 문제

제한 사항:
1 <= N < 50
농작물의 가치는 1~5
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    
    result = 0
    
    for i in range(N//2+1):     # 마름모의 꼭대기에서 중간 가장 긴 부분까지 합 구하기
        result += sum(farm[i][N//2-i:N//2+1+i])
    
    idx = -1
    for i in range(N-1, N//2, -1):      # 마름모 가장 긴 부분 바로 밑 부터 맨 아래 부분까지의 합
        idx += 1
        result += sum(farm[i][N//2-idx:N//2+1+idx])
        
    print(f'#{tc} {result}')