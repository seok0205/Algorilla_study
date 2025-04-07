'''
지도의 각 칸에 정수가 있음
이동한 칸에 숫자가 0이면 주사위의 바닥면 숫자가 지도의 칸에 복사됨
이동한 칸에 숫자가 0이 아니면 해당 숫자가 주사위 바닥면에 복사되고 칸의 숫자는 0이 됨
주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 매번 출력
가장 처음에 주사위에는 모든 면이 0임
지도 위에 주사위 윗 면은 1, 동쪽 바라보는 방향이 3인 상태로 놓여져 있음
주사위가 지도 바깥으로 이동 시 출력 X , 해당 명령 무시
(이동) 동: 1, 서: 2, 북: 3, 남: 4
'''


def move(row, col, dice_num):
    if 0 <= row < N and 0 <= col < M:
        if matrix[row][col]:
            dice_val[7-dice_num] = matrix[row][col]
            print(dice_val[dice_num])
            print(f"curr dice val : {dice_val}")
        else:
            matrix[row][col] = dice_val[7-dice_num]

# TODO: 이렇게 하면 옆으로 굴렸다가 위로 올릴 때 왼, 오 숫자가 상, 하 숫자가 되기 때문에
# 어느 방향이 상, 하가 될건지도 저장을 하던가 해야 될 듯
def get_dice_side(dice_num, direction):
    if dice_num == 1:
        if direction == 1:
            return 4
        elif direction == 2:
            return 3
        elif direction == 3:
            return 5
        elif direction == 4:
            return 2
    elif dice_num == 2:
        if direction == 1:
            return 4
        elif direction == 2:
            return 3
        elif direction == 3:
            return 1
        elif direction == 4:
            return 6
    elif dice_num == 3:
        if direction == 1:
            return 1
        elif direction == 2:
            return 6
        elif direction == 3:
            return 5
        elif direction == 4:
            return 2
    elif dice_num == 4:
        if direction == 1:
            return 6
        elif direction == 2:
            return 1
        elif direction == 3:
            return 5
        elif direction == 4:
            return 2
    elif dice_num == 5:
        if direction == 1:
            return 4
        elif direction == 2:
            return 3
        elif direction == 3:
            return 6
        elif direction == 4:
            return 1
    elif dice_num == 6:
        if direction == 1:
            return 4
        elif direction == 2:
            return 3
        elif direction == 3:
            return 2
        elif direction == 4:
            return 5


N, M, x, y, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(matrix)
dice_val = [0] * 7
commands = list(map(int, input().split()))
curr_row, curr_col = x, y
curr_front = 1
for command in commands:
    next_front = None
    if command == 1:
        curr_col += 1
        next_front = get_dice_side(curr_front, 1)
    elif command == 2:
        curr_col -= 1
        next_front = get_dice_side(curr_front, 2)
    elif command == 3:
        curr_row -= 1
        next_front = get_dice_side(curr_front, 3)
    elif command == 4:
        curr_row += 1
        next_front = get_dice_side(curr_front, 4)
    move(curr_row, curr_col, next_front)
