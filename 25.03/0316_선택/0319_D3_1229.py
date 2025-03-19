'''
D3 1229 암호문2

0 ~ 999999 사이의 수를 나열해 만든 암호문이 있음. 급히 수정해야함
이 암호문은 특수 제작된 처리기로만 수정 가능. 2개의 기능이 존재

1. I x,y,s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자 삽입. s는 덧붙일 숫자들.
2. D x,y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제.

입력:
첫줄 - 원본 암호문의 길이 N(100 <= N <= 200 정수)
두줄 - 원본 암호문
세줄 - 명령어의 개수(10 <= N <= 20 정수)
네줄 - 명령어
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    code = list(map(int, input().split()))
    c_num = int(input())
    command = list(map(str, input().split()))
    
    cnt = 0     # 명령 개수 세기
    idx = 0     # command 읽어갈 인덱스
    while True:
        if cnt == c_num:        # 존재하는 명령 모두 수행했으면 while문 중단
            break
        
        if command[idx] == 'I':         # I 명령
            cnt += 1                    # 수행했으니 명령 개수 1 증가
            x = int(command[idx+1])     # code(암호문)에 x자리부터 y개의 숫자를 넣을 것
            y = int(command[idx+2])
            for i in range(y):
                code.insert(x+i, command[idx+3+i])
        elif command[idx] == 'D':       # D 명령
            cnt += 1
            x = int(command[idx+1])     # code(암호문)에 x자리부터 y개의 숫자를 삭제할 것
            y = int(command[idx+2])
            for i in range(y):
                code.pop(x)
        
        idx += 1            # 한자리씩 탐색(I와 ,D를 발견하면 명령 시작함)
        
    print(f'#{tc} {" ".join(map(str, code[:10]))}')