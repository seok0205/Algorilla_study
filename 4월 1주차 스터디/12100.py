from copy import deepcopy

# 배열 좌우 반전
def mirror(arr):
    return [row[::-1] for row in arr]
# 배열 오른쪽 회전
def right(arr):
    return list(map(list, zip(*arr[::-1])))
# 배열 왼쪽 회전
def left(arr):
    return list(map(list, zip(*arr)))[::-1]

def move_arr(arr):
    now = 0
    new_arr = []

    for i in range(N):
        line = [num for num in arr[i] if num != 0]  # 0 제거하고 압축
        merged = []
        j = 0
        while j < len(line):
            if j + 1 < len(line) and line[j] == line[j + 1]:
                merged.append(line[j] * 2)
                now = max(now, line[j] * 2)
                j += 2  # 다음 블록은 스킵
            else:
                merged.append(line[j])
                now = max(now, line[j])
                j += 1
        # 나머지 빈 자리는 0으로 채움
        merged += [0] * (N - len(merged))
        new_arr.append(merged)

    return new_arr, now
    # for i in range(N):
    #     for j in range(N-1):
    #         if arr[i][j]:
    #             # 만약 0이 아닌 숫자가 나오면 다음 것들과 비교해서 같은 숫자가 나올 때까지 진행
    #             # 같은 숫자 나오면 합쳐준다.
    #             for p in range(j+1, N):
    #                 if arr[i][j] == arr[i][p]:
    #                     arr[i][j] = arr[i][j] + arr[i][p]
    #                     arr[i][p] = 0
    #                     break
    # now = 0
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] > now:
    #             now = arr[i][j]
    #         if arr[i][j]:
    #             for p in range(j-1, -1, -1):
    #                 if arr[i][p]:
    #                     arr[i][p+1] = arr[i][j]
    #                     arr[i][j] = 0
    # return arr, now
    



def recur(cnt, arr, now_max):
    global result
    if cnt == 5:
        result = max(now_max, result)        
        return
    # 만약 2의 남은횟수의 제곱을 현재의 max값에 곱했는데 지금까지 구한 max값보다
    # 작거나 같다면 더이상 진행할 필요가 없음.
    if now_max * (2 ** (5-cnt)) <= result:
        return
    
    for order in ['left', 'right', 'up', 'down']:
        copy_arr = deepcopy(arr)
        if order == 'left':
            new_arr, max_in_arr = move_arr(copy_arr)
            recur(cnt+1, new_arr, max_in_arr)
        elif order == 'right':
            new_arr, max_in_arr = move_arr(right(copy_arr))
            recur(cnt+1, new_arr, max_in_arr)
        elif order == 'up':
            new_arr, max_in_arr = move_arr(mirror(copy_arr))
            recur(cnt+1, new_arr, max_in_arr)
        else:
            new_arr, max_in_arr = move_arr(left(copy_arr))
            recur(cnt+1, new_arr, max_in_arr)

import sys
input = sys.stdin.readline
# 보드의 크기
N = int(input())
# 0은 그냥 빈 공간을 나타냄
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
recur(0, arr, 1)
print(result)