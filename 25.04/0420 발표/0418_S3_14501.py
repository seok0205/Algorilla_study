'''
S3 14501 퇴사

상담원이 퇴사를 하려고 함
오늘부터 N+1일째 되는 날 퇴사를 하기 위해, 남은 N일 동안 최대한 많은 상담을 하려 함
최대한 많은 상담을 잡으라고 부탁했고, 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았음
각각의 상담은 완료하는데 걸리는 기간 T와 상담했을 때 받을 수 있는 금액 P로 이루어져 있음

N+1일부터는 회사에 없기 때문에 N-1일의 상담인데 걸리는시간이 3일이면 수행하지 못함. 따라서 N-1일의 상담은 진행하지 못하게됨

적절한 상담을 했을 때, 최대 이익을 구하는 문제

입력:
N : 주어진 날 수
N줄 동안 T와 P : 상담을 완료하는데 걸리는 시간(일), 완료 시 벌수있는 돈
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def plan(day, pay):     # 재귀
    global result
    
    if day > N:                     # 날짜가 퇴사날짜 지나면 재귀 중단 후 최댓값 비교
        result = max(result, pay)
        return
    
    if day + schedule[day][0] - 1 <= N:     # 만약 기간내에 마칠 수 있는 상담이고,
        if calender[day] == 0:              # 상담 계획이 없는 날이라면
            for i in range(schedule[day][0]):       # 계획 잡은 상태에서
                calender[day+i] = 1
            plan(day + 1, pay + schedule[day][1])       # 재귀 호출로 다음 일정 잡으러 출발
            for j in range(schedule[day][0]):       # 상담 잡지 않은 상태로 복귀 시킴
                calender[day+j] = 0
    
    plan(day + 1, pay)          # 해당 날은 상담잡지않고 다음 날로 넘긴 상황


N = int(input())
schedule = [0]

for i in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))

calender = [0] * (N+1)      # 상담 계획 기록지
result = 0                  # 최대 상담료

plan(1, 0)          # 재귀 호출

print(result)