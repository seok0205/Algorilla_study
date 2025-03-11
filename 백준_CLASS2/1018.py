# 체스판 다시 칠하기
# 8x8 체스판으로 줄여서 최소로 칠하는 횟수
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
check1 = [[0]*8 for _ in range(8)]
check2 = [[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            check1[i][j] = 'W'
            check2[i][j] = 'B'
        else:
            check1[i][j] = 'B'
            check2[i][j] = 'W'

result = 1e10
for p in range(N-7):
    for q in range(M-7):
        temp1 = 0
        temp2 = 0
        for i in range(8):
            for j in range(8):
                if arr[p+i][q+j] != check1[i][j]:
                    temp1 += 1
                elif arr[p+i][q+j] != check2[i][j]:
                    temp2 += 1
        if result > min(temp1, temp2):
            result = min(temp1, temp2)
print(result)
                    
