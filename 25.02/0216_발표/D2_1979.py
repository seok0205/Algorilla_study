'''
D2_어디에 단어가 들어갈 수 있을까

NxN 크기 2차원 배열에서 행과 열 기준 모두 1이 연속으로 나오는 횟수를 구하는 문제

입력:
N = 배열 가로,세로 길이
K = 구하려는 연속으로 1이나오는 횟수
matrix = 2차원 배열
'''

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0      # 결과 저장값
    
    for i in range(N):      # 배열의 넓이를 1씩 확장 대각선은 안구하므로 열, 행 기준으로 0의 값을 추가
        matrix[i].append(0)
    matrix.append(list(0 for _ in range(N+1)))
    
    for i in range(N):      # K만큼 연속해서 나오는 1. 경우의 수 구하는 반복문
        max_length_row = 0      # 연속되는 1의 길이 저장 변수
        max_length_col = 0
        for j in range(N):      # 한 반복문에서 행, 열의 연속된 1의 길이 구함
            if matrix[i][j] and matrix[i][j+1] or matrix[i][j]:     # 해당 인덱스와 다음 인덱스의 값도 1이거나 해당 인덱스의 값만 1일때
                max_length_row += 1     # 길이 1 증가
            else:       # 0일 때 연속 길이 초기화
                max_length_row = 0
                
            if matrix[j][i] and matrix[j+1][i] or matrix[j][i]:     # 해당 인덱스와 다음 인덱스의 값도 1이거나 해당 인덱스의 값만 1일때
                max_length_col += 1     # 길이 1 증가
            else:
                max_length_col = 0
                
            if matrix[i][j+1] == 0 and max_length_row == K:     # 만약 다음 인덱스에서 0이고, 연속이 끊길 예정일때, 이때까지 연속길이가 K와 같다면, 최종결과 1증가
                result += 1
                
            if matrix[j+1][i] == 0 and max_length_col == K:
                result += 1
    
    print(f'#{tc} {result}')