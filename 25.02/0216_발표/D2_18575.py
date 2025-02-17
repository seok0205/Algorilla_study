'''
D1 18575 풍선팡 보너스 게임

NxN 배열 한 숫자 선택하면 같은 행, 열의 숫자 합이 점수.
최대 격차를 구하는 문제
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_score = 0
    min_score = 0
    
    for i in range(N):
        for j in range(N):
            row_sum = sum(matrix[i])
            col_sum = list()
            for k in range(N):
                col_sum.append(matrix[k][j])
            col_sum = sum(col_sum)
        
            score = row_sum + col_sum - matrix[i][j]
            
            if max_score < score:
                max_score = score
                
            if min_score > score:
                min_score = score
            elif i == 0 and j == 0:
                min_score = score
            
    print(f'#{tc} {max_score - min_score}')