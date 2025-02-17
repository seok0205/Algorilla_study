T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        matrix[i].append(0)
    matrix.append([0 for _ in range(N)])
    
    result = 0
    
    for i in range(N):
        row_length = 0
        col_length = 0
        for j in range(N):
            if matrix[i][j]:
                row_length += 1
            elif matrix[i][j] == 0:
                row_length = 0
                
            if matrix[j][i]:
                col_length += 1
            elif matrix[j][i] == 0:
                col_length = 0
            
            if matrix[i][j+1] == 0 and row_length == K:
                result += 1
            if matrix[j+1][i] == 0 and col_length == K:
                result += 1
    
    print(f'#{tc} {result}')