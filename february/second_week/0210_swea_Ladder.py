# test_arr = [[1,0,0,0,1,0,1,0,0,1], [1,0,0,0,1,0,1,1,1,1], [1,0,0,0,1,0,1,0,0,1], [1,0,0,0,1,1,1,0,0,1], [1,0,0,0,1,0,1,0,0,1], [1,1,1,1,1,0,1,1,1,1], [1,0,0,0,1,0,1,0,0,1], [1,1,1,1,1,0,1,0,0,1], [1,0,0,0,1,1,1,0,0,1], [1,0,0,0,1,0,1,0,0,2]]
# curr_r, curr_c = 9, test_arr[9].index(2)
# print(curr_r, curr_c)
# # 상 - 좌 - 우
# d = 0
# dr = [-1, 0, 0]
# dc = [0, -1, 1]
#
# while curr_r > 0:
#     nr = curr_r + dr[d]
#     nc = curr_c + dc[d]
#
#     if 0 <= nr < 10 and 0 <= nc < 10:
#         curr_r = nr
#         curr_c = nc
#     if d == 0 and curr_c >= 1 and test_arr[curr_r][curr_c - 1] == 1:
#         d = 1
#     elif d == 0 and curr_c < 9 and test_arr[curr_r][curr_c + 1] == 1:
#         d = 2
#     elif d != 0 and curr_r >= 1 and test_arr[curr_r - 1][curr_c] == 1:
#         d = 0
#
#     answer = curr_c

for _ in range(10):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 델타 사용을 위해 현재 위치 설정
    curr_r, curr_c = 99, matrix[99].index(2)

    # 델타 설정
    # 상 - 좌 - 우
    d = 0
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    answer = 0

    # 최종 목적지는 첫 번째 행에 도달할 때 결정되므로 curr_r > 0
    while curr_r > 0:
        # 다음 위치 설정
        nr = curr_r + dr[d]
        nc = curr_c + dc[d]
        # 다음 위치가 범위 내에 있는지 확인 후 현재 위치로 업데이트
        if 0 <= nr < 100 and 0 <= nc < 100:
            curr_r = nr
            curr_c = nc
        # 사다리타기를 거슬러올라갈 때는 위로 갈 때는 좌우를 살펴야 하므로
        if d == 0 and curr_c >= 1 and matrix[curr_r][curr_c - 1] == 1:
            d = 1
        elif d == 0 and curr_c < 99 and matrix[curr_r][curr_c + 1] == 1:
            d = 2
        # 좌우로 갈 때는 위로 가는 옵션밖에 없으므로
        elif d != 0 and curr_r >= 1 and matrix[curr_r - 1][curr_c] == 1:
            d = 0

        answer = curr_c

    print(f"#{t} {answer}")