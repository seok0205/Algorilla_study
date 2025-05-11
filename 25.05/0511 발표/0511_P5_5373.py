'''
P5 5373 큐빙

루빅스 큐브는 삼차원 퍼즐. 보통 루빅스 큐브는 3x3x3 정육면체.
퍼즐 풀려면 아홉 개의 작은 정육면체 색이 동일해야 함.
큐브는 각 면을 양방향으로 90도 만큼 돌릴 수 있도록 만들어져 있음.
회전 마치면, 다른 면 돌릴 수 있음. 이렇게 큐브의 서로 다른 면 돌리다보면 색 섞기 가능.
이 문제에선 큐브가 모두 풀린 상태에서 시작.
윗면은 흰색, 아랫 면 노란색, 앞면은 빨간색, 뒷면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색.

루빅스 큐브 돌릴 방법 순서대로 주어짐. 모두 돌린 다음 가장 윗면의 색상을 구하는 문제

입력:
첫줄은 테스트 케이스 개수
다음부터는 테스트 케이스의 형태
첫째 줄은 큐브 돌린 횟수 n
둘째줄은 큐브 돌린 방법. 첫 문자는 U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼 면, R: 오른 면
두번째 문자가 돌린 방향. '+'는 시계방향. '-'는 반시계 방향(그쪽 면을 바라보았을때 기준)

출력:
큐브 모두 돌린 후의 윗 면 색상 출력.
첫 줄은 뒷 면과 접하는 칸의 색을 출력, 두번째, 세번째 줄은 순서대로 출력.
흰색은 w, 노랑 y, 빨강 r, 오렌지 o, 초록 g, 파랑 b.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def turn_left(cube):                            # 큐브 한 면 돌리기 (오, 왼)
    new_cube = [raw[:] for raw in cube]
    return list(map(list, zip(*list(raw[::-1] for raw in new_cube))))


def turn_right(cube):
    new_cube = [raw[:] for raw in cube]
    return list(map(list, zip(*list(raw[:] for raw in reversed(new_cube)))))


def change_cube(face, dir):                         # 큐브 맞추기
    new_up_cube = [raw[:] for raw in up_cube]           # 항상 모든 면 깊은 복사 후 진행
    new_under_cube = [raw[:] for raw in under_cube]
    new_front_cube = [raw[:] for raw in front_cube]
    new_back_cube = [raw[:] for raw in back_cube]
    new_right_cube = [raw[:] for raw in right_cube]
    new_left_cube = [raw[:] for raw in left_cube]

    if face in ['U', 'D']:          # 윗면과 아랫면은 바뀌는 면이 같음. 이때는 가장 행이아닌 열을 기준으로 바꾸는 상황이 많아서 오른면과 왼면을 돌려야 큐빙이 편함
        if face == 'U':
            if dir == '+':          # 오른쪽으로 돌릴 때
                new_right_cube, new_left_cube = turn_left(new_right_cube), turn_left(new_left_cube)
                a, b, c, d = new_front_cube[0], list(reversed(new_left_cube[0])), new_back_cube[2], list(reversed(new_right_cube[2]))       # 돌릴 때 인덱스는 고정이라서 역방향으로 들어가야하는 경우가 있음. 왜냐하면 어느 면이든 배열이 역방향으로 마주보게 되는 경우가 생기기 때문
                new_up_cube = turn_right(new_up_cube)
                new_front_cube[0], new_left_cube[0], new_back_cube[2], new_right_cube[2] = d, a, b, c
                new_right_cube, new_left_cube = turn_right(new_right_cube), turn_right(new_left_cube)
            else:           # 왼쪽 돌릴 때
                new_left_cube, new_right_cube = turn_right(new_left_cube), turn_right(new_right_cube)
                a, b, c, d = new_front_cube[0], list(reversed(new_left_cube[2])), new_back_cube[2], list(reversed(new_right_cube[0]))
                new_up_cube = turn_left(new_up_cube)
                new_front_cube[0], new_left_cube[2], new_back_cube[2], new_right_cube[0] = b, c, d, a
                new_left_cube, new_right_cube = turn_left(new_left_cube), turn_left(new_right_cube)
        else:
            if dir == '+':
                new_right_cube, new_left_cube = turn_right(new_right_cube), turn_right(new_left_cube)
                a, b, c, d = new_front_cube[2], list(reversed(new_left_cube[0])), new_back_cube[0], list(reversed(new_right_cube[2]))
                new_under_cube = turn_right(new_under_cube)
                new_front_cube[2], new_left_cube[0], new_back_cube[0], new_right_cube[2] = b, c, d, a
                new_left_cube, new_right_cube = turn_left(new_left_cube), turn_left(new_right_cube)
            else:
                new_right_cube, new_left_cube = turn_left(new_right_cube), turn_left(new_left_cube)
                a, b, c, d = new_front_cube[2], list(reversed(new_left_cube[2])), new_back_cube[0], list(reversed(new_right_cube[0]))
                new_under_cube = turn_left(new_under_cube)
                new_front_cube[2], new_left_cube[2], new_back_cube[0], new_right_cube[0] = d, a, b, c
                new_right_cube, new_left_cube = turn_right(new_right_cube), turn_right(new_left_cube)
    elif face in ['F', 'B']:            # 앞면과 뒷면을 기준으로 돌릴 때
        if face == 'F':
            if dir == '+':
                a, b, c, d = new_up_cube[2], list(reversed(new_right_cube[2])), list(reversed(new_under_cube[0])), new_left_cube[2]     
                new_front_cube = turn_right(new_front_cube)
                new_up_cube[2], new_right_cube[2], new_under_cube[0], new_left_cube[2] = d, a, b, c
            else:
                a, b, c, d = new_up_cube[2], new_right_cube[2], list(reversed(new_under_cube[0])), list(reversed(new_left_cube[2]))
                new_front_cube = turn_left(new_front_cube)
                new_up_cube[2], new_right_cube[2], new_under_cube[0], new_left_cube[2] = b, c, d, a
        else:
            if dir == '+':
                a, b, c, d = new_up_cube[0], new_right_cube[0], list(reversed(new_under_cube[2])), list(reversed(new_left_cube[0]))
                new_back_cube = turn_right(new_back_cube)
                new_up_cube[0], new_right_cube[0], new_under_cube[2], new_left_cube[0] = b, c, d, a
            else:
                a, b, c, d = new_up_cube[0], list(reversed(new_right_cube[0])), list(reversed(new_under_cube[2])), new_left_cube[0]
                new_back_cube = turn_left(new_back_cube)
                new_up_cube[0], new_right_cube[0], new_under_cube[2], new_left_cube[0] = d, a, b, c
    else:
        if face == 'L':         # 왼면, 오른면 기준으로 돌릴때는 나머지 면들이 십자가 모양 중 일자처럼 일렬로 쭉 내리면 되기 때문에 바꾸기 수월.
            a, b, c, d = new_up_cube[0], new_front_cube[0], new_under_cube[0], new_back_cube[0]
            if dir == '+':
                new_left_cube = turn_right(new_left_cube)
                new_up_cube[0], new_front_cube[0], new_under_cube[0], new_back_cube[0] = d, a, b, c
            else:
                new_left_cube = turn_left(new_left_cube)
                new_up_cube[0], new_front_cube[0], new_under_cube[0], new_back_cube[0] = b, c, d, a
        else:
            a, b, c, d = new_up_cube[2], new_front_cube[2], new_under_cube[2], new_back_cube[2]
            if dir == '+':
                new_right_cube = turn_right(new_right_cube)
                new_up_cube[2], new_front_cube[2], new_under_cube[2], new_back_cube[2] = b, c, d, a
            else:
                new_right_cube = turn_left(new_right_cube)
                new_up_cube[2], new_front_cube[2], new_under_cube[2], new_back_cube[2] = d, a, b, c
    
    return new_up_cube, new_under_cube, new_front_cube, new_back_cube, new_right_cube, new_left_cube        # 한차례 할때마다 나온 배열을 받음


T = int(input())

for _ in range(T):
    n = int(input())
    method = list(map(str, input().split()))

    up_cube = [['w'] * 3 for _ in range(3)]
    under_cube = [['y'] * 3 for _ in range(3)]
    front_cube = [['r'] * 3 for _ in range(3)]
    back_cube = [['o'] * 3 for _ in range(3)]
    left_cube = [['g'] * 3 for _ in range(3)]
    right_cube = [['b'] * 3 for _ in range(3)]

    for i in range(len(method)):
        if method[i][0] in ['L', 'R']:      # 왼면과 오른면 기준으로 돌릴때는 모든 면의 열이 바뀌기 때문에 바꾸고 함수 실행해줌. 원상 복귀 필수
            up_cube, front_cube, under_cube, back_cube = turn_right(up_cube), turn_right(front_cube), turn_right(under_cube), turn_right(back_cube)
            up_cube, under_cube, front_cube, back_cube, right_cube, left_cube = change_cube(method[i][0], method[i][1])
            up_cube, front_cube, under_cube, back_cube = turn_left(up_cube), turn_left(front_cube), turn_left(under_cube), turn_left(back_cube)
        else:
            up_cube, under_cube, front_cube, back_cube, right_cube, left_cube = change_cube(method[i][0], method[i][1])

    for i in up_cube:       # 값 출력
        print(''.join(i))