#9386 연속한 1의 개수
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input()) #개수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input()) #0과1로된 문자열
    x=input().split('0') #문자열에서 0 빼기
    #print(x) #[" ", "11", " ", "111"]
    #1이 많은 항목 길이를 세야겠다

    for i in x : #x배열 [" ", "11", " ", "111"]의 i번째 값이
        max_count_len = 0 #변수 0부터
        if max_count_len<len(i): #x배열의i번째값 길이보다 max_count_len이 작으면
            max_count_len = len(i) #max_count_len에 i번째 값의 길이 저장
    print(f'#{test_case} {max_count_len}')
    
    #1 2 4
    #10개 중 2개 맞음

  