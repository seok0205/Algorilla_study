'''
S4 1244 스위치 켜고 끄기

1번부터 연속적으로 있는 스위치 존재
1은 킨것 0은 안킨것

어떤 사람에게 1이상 스위치 개수 이하인 자연수 분배

남자는 스위치 번호가 자신이 보유한 숫자의 배수면 그 스위치 상태 바꿈
여자는 자신이 보유한 수와 같은 번호가 붙은 스위치 중심으로 좌우 대칭이면서 가장많은 스위치를 포함한 구간 찾아 바꿈
구간에 속한 스위치는 항상 홀수. 좌우 대칭일때 값이 같아야 바꿈. 다르면 거기서 멈춤
'''

S = int(input())
switch_status = list(map(int, input().split()))

students = int(input())
for _ in range(students):
    X, N = map(int, input().split())
    
    if X == 1:
        for i in range(S):
            if (i+1) % N == 0:
                switch_status[i] = int(not switch_status[i])
        
    elif X == 2:
        idx = 0
        while True:
            if idx == 0:
                switch_status[N-1] = int(not switch_status[N-1])
            elif 0 <= N-1-idx < S and 0 <= N-1+idx < S:
                if switch_status[N-1-idx] == switch_status[N-1+idx]:
                    switch_status[N-1-idx] = int(not switch_status[N-1-idx])
                    switch_status[N-1+idx] = int(not switch_status[N-1+idx])
                else:
                    break
            else:
                break
            idx += 1

for i in range(S):
    print(switch_status[i], end=" ")
    if i % 20 == 19:
        print()