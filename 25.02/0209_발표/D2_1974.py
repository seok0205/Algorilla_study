'''
1979 D2 스도쿠 검증

9x9 2차원배열에 1부터 9까지의 숫자를 겹치지 않게 스도쿠 형식으로 되어있는지 확인하는 문제
스도쿠 형식이 맞으면 1, 아니면 0 출력

입력:
9x9 형태의 값이 채워진 배열(1~9)
'''

T = int(input())

for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    result = 1      # break가 일어나지 않는다면 조건 충족, 1 출력
    
    for i in range(9):      # 스도쿠 순회 시작
        num_row = list()    # 숫자가 나타나면 저장할 리스트 생성(행 전용, 열 전용)
        num_col = list()
        for j in range(9):
            if matrix[i][j] not in num_row:     # 해당 인덱스의 숫자가 리스트에 없다면
                num_row.append(matrix[i][j])    # 추가
            else:       # 이미 있다면 조건 불만족으로 결과 0 수정 후 반복문 탈출
                result = 0
                break
            if matrix[j][i] not in num_col:     # 이하 동문
                num_col.append(matrix[j][i])
            else:
                result = 0
                break
        
            if i in [0, 3, 6] and j in [0, 3, 6]:       # 9개의 박스의 숫자 i, j 인덱스가 왼쪽 꼭짓점 부분의 좌표이면 분석 시작
                num = list()        # 숫자 출현 시 저장할 리스트
                for a in range(3):
                    for b in range(3):
                        if matrix[i+a][j+b] not in num:     # 해당 인덱스 숫자 리스트 존재 X, 추가
                            num.append(matrix[i+a][j+b])
                        else:       # 이미 존재하다면 조건 불만족
                            result = 0
                            break
    
    print(f'#{tc} {result}')