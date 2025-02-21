'''

4
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''


def check_omok():
    for i in range(N):
        count_row = 0
        for j in range(N):
            if matrix[i][j] == 'o':
                count_row += 1
                if count_row >= 5:
                    return "YES"
            else:
                count_row = 0

    for i in range(N):
        count_col = 0
        for j in range(N):
            if matrix[j][i] == 'o':
                count_col += 1
                if count_col >= 5:
                    return "YES"
            else:
                count_col = 0

    for i in range(N):
        for j in range(N):
            count_l = 0
            for k in range(5):
                if 0 <= i + k < N and 0 <= j + k < N:
                    if matrix[i + k][j + k] != 'o':
                        break
                    count_l += 1
            if count_l >= 5:
                return "YES"

    for i in range(N):
        for j in range(N):
            count_r = 0
            for k in range(5):
                if 0 <= i + k < N and 0 <= j - k < N:
                    if matrix[i + k][j - k] != 'o':
                        break
                    count_r += 1
            if count_r >= 5:
                return "YES"


T = int(input())
for t in range(1, T + 1):
    N = int(input())

    matrix = [list(input()) for _ in range(N)]

    answer = "NO" if check_omok() is None else check_omok()

    print(f"#{t} {answer}")
