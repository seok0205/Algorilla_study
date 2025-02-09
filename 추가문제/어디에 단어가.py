T = int(input())

for t in range(1, T + 1):
    # N: 퍼즐 크기, K: 단어 길이
    N, K = map(int, input().split())

    # 2차원 리스트
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    count = 0  # K 길이의 단어가 들어갈 수 있는 자리 개수

    # 가로 방향 확인
    for row in puzzle:
        blank = 0  # 연속된 1의 개수 저장
        for cell in row + [0]:  # 마지막에 0을 추가해 끊기도록 함
            if cell == 1:
                blank += 1  # 1이면 연속 개수 증가
            else:
                if blank == K:  # K개 연속이면 정답 카운트 증가
                    count += 1
                blank = 0  # 끊기면 초기화

    # 세로 방향 확인
    for col in range(N):
        blank = 0
        for row in range(N):
            if puzzle[row][col] == 1:  # 세로방향에서 1을 찾기
                blank += 1  # 1이면 연속 개수 증가
            else:
                if blank == K:
                    count += 1
                blank = 0  # 끊기면 초기화
        if blank == K:  # 마지막까지 1이 연속된 경우 처리
            count += 1

    print("#" + str(t), count)
