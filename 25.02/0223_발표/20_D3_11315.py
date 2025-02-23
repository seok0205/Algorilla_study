'''
D3 11315 오목 판정

NxN 판에 돌이 있거나 없을 수 있음.
돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정
'''


def find_omok(size):
    result = 'NO'       # 기본적으로 중간에 YES로 변경되지 않으면 NO출력
    
    for i in range(size):
        row_length = 0
        col_length = 0
        for j in range(size):
            if matrix[i][j] == 'o':     # 가로 o 체크
                row_length += 1
            else:
                row_length = 0
                    
            if matrix[j][i] == 'o':     # 세로 o 체크
                col_length += 1
            else:
                col_length = 0
            
            if row_length >= 5 or col_length >= 5:      # 5이상 한번만 나와도 됨. 따라서 1증가할때마다 5를 넘는지 체크.
                result = 'YES'
                return result       # 5 나오는 순간 바로 값 반환
        
    for i in range(1-size, size):
        X_length = 0
        Y_length = 0
        for j in range(size):       # (0,0) (N-1,N-1) 기준 대각선 o 체크
            if 0 <= i+j < size:
                if matrix[i+j][j] == 'o':
                    X_length += 1 
                else:
                    X_length = 0
                    
            if 0 <= size-1-i-j < size:      # (N-1, 0) (0, N-1) 기준 대각선 o 체크
                if matrix[size-1-i-j][j] == 'o':
                    Y_length += 1
                else:
                    Y_length = 0
                    
            if X_length >= 5 or Y_length >= 5:      # 마찬가지로 5 나오면 YES 반환
                result = 'YES'
                return result
    return result
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    
    answer = find_omok(N)
    
    print(f'#{tc} {answer}')