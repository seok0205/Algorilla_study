import sys
sys.stdin = open('input.txt', 'r')

def count_deadlocks(table, size):
    count = 0  # 교착 상태 개수
    for col in range(size):  # 열 단위 탐색
        stack = []  # N극(1)만 저장하는 스택
        for row in range(size):
            if table[row][col] == 1:  # N극(1)을 발견하면 스택에 추가
                stack.append(1)
            elif table[row][col] == 2:  # S극(2)을 발견하면
                if stack:  # 스택에 N극이 있으면 교착 상태 발생
                    count += 1
                    stack.clear()  # 충돌 후에는 초기화
    return count


# 테스트 케이스 개수
T = 10
for t in range(1, T + 1):
    # 입력 처리
    M = int(input())  # 테이블 크기 (100x100)
    table = [list(map(int, input().split())) for _ in range(M)]

    # 교착 상태 개수 출력
    result = count_deadlocks(table, M)
    print(f'#{t} {result}')
