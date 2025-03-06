def make_sub_groups(arr, arr_len):
    result = []
    for i in range(arr_len):
        for j in range(1, arr_len-i+1):
            print(i, j, arr_len-(i+j))
            print(f"w: {arr[:i]}")
            print(f"b: {arr[i:i+j]}")
            print(f"r: {arr[i+j:]}")
        # print(w, b, r)
    # print(result)

# arr = [1,2]
# M = 2
# make_sub_groups(arr, M)


def find_the_least_changes_case(matrix, row_len, rows_len):
    sub_changes = 0
    min_changes = float('inf')
    arr = [num for num in range(1, rows_len+1)]

    for i in range(rows_len):
        for j in range(1, rows_len-i+1):  # 해당 색깔로 정할 row의 인덱스 (1부터 시작)
            W = arr[:i]
            B = arr[i:i+j]
            R = arr[i+j:]

            for k in range(rows_len):
                if k < len(W):
                    sub_changes += count_changes(matrix[W[k]], row_len, 'W')
                if k < len(B):
                    sub_changes += count_changes(matrix[B[k]], row_len, 'B')
                if k < len(R):
                    sub_changes += count_changes(matrix[R[k]], row_len, 'R')
            if sub_changes < min_changes:
                min_changes = sub_changes
            sub_changes = 0
    return min_changes

def count_changes(arr, arr_len, color):
    changes = 0
    changes += (arr_len - arr.count(color))
    return changes


T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())

    colors = [list(input()) for _ in range(N)]

    changes = count_changes(colors[0], M, 'W')
    changes += count_changes(colors[N - 1], M, 'R')
    changes += find_the_least_changes_case(colors, M, N-2)

    print(f"#{t} {changes}")