'''
D3 5789 현주의 상자 바꾸기

1번부터 N번까지의 N개의 상자를 가지고 있음.
처음엔 0으로 모두 적혀있음
Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 함.
i번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
Q회 동안 위 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값을 순서대로 출력하는 문제
'''

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(1, Q+1):     # 테스트 케이스 받을 때 i 1씩 증가
        L, R = map(int, input().split())

        for j in range(R-L+1):      # L과 R까지 i로 변경
            box[L+j-1] = i
    
    print(f'#{tc} {" ".join(list(map(str, box)))}')     # 출력