'''
D3 13038 교환학생

연중무휴인 대학교가 존재
교환학생들을 위한 수업이 특정 요일에만 진행
정보는 7개의 정수로 표현

일월화수목금토 순서로 0혹은 1로 수업의 유무 알 수있음

수업이 어떠한 요일에도 열리지 않는 경우는 없다고 가정해도 됨
교환학생으로 n일동안 수업을 들으려고하면 목표를 위해 지내야하는 최소 일수 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal_day(idx, s):
    global result
    
    cnt = 0     # 들은 수업 개수
    days = 0    # 지난 날짜
    i = idx     # 확인 날짜
    
    while True:
        if cnt == N:        # 수업 N번 들으면 종료
            break
        
        if (s >> i) & 0x1:  # i번째 비트 1이면 수업 있음
            cnt += 1        # 하나 듣고
        days += 1           # 수업 있든없든 날짜는 1 증가
        i = (i + 1) % 7     # 요일 0에서 6 반복

    if result > days:       # 총 지난 날짜가 정해져있는 최소 날짜보다 작으면 최솟값 교체
        result = days
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    schedule = list(map(int, input().split()))
    result = float("inf")           # 최소 기간 저장
    
    s_sum = sum((schedule[i] << i) for i in range(7))       # 비트마스크로 변환
    
    for i in range(7):
        if (s_sum >> i) & 0x1:      # 시작 요일을 다 다르게 해봄(수업이 있는 경우만 시작)
            cal_day(i, s_sum)
            
    print(f'#{tc} {result}')