'''
D1 20397 돌 뒤집기 게임 2

돌의 양면은 흰, 검
i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둠
주어진 돌을 벗어나면 뒤집기 중지
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    IJ = [list(map(int, input().split())) for _ in range(M)]

    for i in range(len(IJ)):
        for j in range(1, IJ[i][1]+1):      # 돌 비교 횟수 1부터 j까지
            x = IJ[i][0] - 1        # 인덱스 i로 설정
            if 0 <= x+j < N and 0 <= x-j < N:       # 비교하려는 돌들이 배열안에 있어야 진행
                if stone[x+j] == stone[x-j]:        # 두 돌이 같으면
                    if stone[x+j]:                  # 0이면 1로, 1이면 0으로 변경
                        stone[x-j] = stone[x+j] = 0
                    else:
                        stone[x-j] = stone[x+j] = 1

    print(f"#{tc} {' '.join(map(str, stone))}")
