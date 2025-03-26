'''
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1

1
5
0 0 1 1 1 1 1 1
1 1 1 1 1 0 1 0
0 0 0 0 1 0 0 1
0 1 0 1 0 1 0 1
4 -1
3 1
4 -1
3 -1
1 -1
'''

def rotate_counterclockwise(lst):
    lst.append(lst.pop(0))
    return lst


def rotate_clockwise(lst):
    lst.insert(0, lst.pop())
    return lst


def is_available_to_move(num_to_rotate, direction):
    left = num_to_rotate - 1
    right = num_to_rotate + 1
    if 0 <= left:
        if matrix[left][2] != matrix[num_to_rotate][6] and not visited[left][2]:
            visited[left][2] = 1
            visited[num_to_rotate][6] = 1
            is_available_to_move(left, -direction)
    if right < 4:
        if matrix[num_to_rotate][2] != matrix[right][6] and not visited[right][6]:
            visited[num_to_rotate][2] = 1
            visited[right][6] = 1
            is_available_to_move(right, -direction)
    if direction == 1:
        return rotate_clockwise(matrix[num_to_rotate])
    elif direction == -1:
        return rotate_counterclockwise(matrix[num_to_rotate])



T = int(input())
for t in range(1, T+1):
    K = int(input())  # 회전 횟수
    matrix = []
    answer = 0
    for _ in range(4):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)
    print("before : ", matrix)
    for _ in range(K):
        num, direction = map(int, input().split())  # 회전시킬 자석 번호, 회전 방향 (1: 시계방향, -1: 반시계방향)
        # 다르면 반시계 회전, 같으면 회전 안함
        visited = [[False] * 8 for _ in range(4)]
        how_to_rotate = is_available_to_move(num-1, direction)
    print("after : ", matrix)

    for i in range(4):
        if matrix[i][0] == 1:
            answer += 2**i

    print(f"#{t} {answer}")