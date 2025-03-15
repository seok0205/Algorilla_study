'''
4*4 격자판
0 - 9 사이 숫자
임의의 위치에서 시작 -> 총 6번 이동 -> 7자리 수 생성
갔던 곳 또 가도 됨
만들 수 있는 서로 다른 일곱자리 수 개수 출력

1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''


def combination(count, row, col, path=[]):
    if len(path) == 7:
        result.add(''.join(path))
        return

    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        next_r, next_c = row + di, col + dj
        if 0 <= next_r < 4 and 0 <= next_c < 4:
            combination(count + 1, next_r, next_c, path + [grid[next_r][next_c]])


T = int(input())
for t in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            combination(0, i, j, [grid[i][j]])
    print(f"#{t} {len(result)}")
