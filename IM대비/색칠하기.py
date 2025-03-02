# 10x10 격자판
T = int(input())
for t in range(1, T+1):
    red_sx, red_sy, red_ex, red_ey = map(int, input().split())
    blue_sx, blue_sy, blue_ex, blue_ey = map(int, input().split())
    arr = [[0]*10 for _ in range(10)]
    
    for i in range(red_sx, red_ex+1):
        for j in range(red_sy, red_ey+1):
            arr[i][j] = 1
    
    for i in range(blue_sx, blue_ex+1):
        for j in range(blue_sy, blue_ey+1):
            if arr[i][j] == 1:
                arr[i][j] = 2
    
    x1, y1 = -1, -1
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 2:
                x1, y1 = i, j
                break
        if x1 != -1 and y1 != -1:
            break

    x2, y2 = -1, -1
    for i in range(9, -1, -1):
        for j in range(9, -1, -1):  
            if arr[i][j] == 2:
                x2, y2 = i, j
                break
        if x2 != -1 and y2 != -1:
            break

    if x1 == -1 and y1 == -1:
        r1, r2, = 0, 0
    else:
        r1, r2 = y2-y1+1, x2-x1+1
    
    print(f'#{t}', r1, r2)