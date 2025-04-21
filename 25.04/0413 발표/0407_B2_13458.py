'''
B2 13458 시험 감독

총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있음.
i번 시험장에 있는 응시자의 수는 A명.

감독관은 총감독관, 부감독관 두명 존재.
총감독관은 한 시험장에서 감시 가능한 응시자 수가 B명, 부감독관은 C명.

각각 시험장에 총감독관은 오직 한명만 있어야 하고, 부감독관은 여러명 있어도 됨.
각 시험장마다 응시생을 모두 감시해야 함. 이때, 필요한 감독관의 수의 최솟값을 구하는 문제.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0

for i in range(N):
    superviser = 1          # 총감독관은 1명 필수
    students = A[i] - B     # 총감독관의 감시 가능한 인원 뺀인원
    
    if students > 0:        # 나머지 감시해야할 인원이 존재한다면
        if students / C > students // C:            # 부감독관 필요한 명수 구하기(딱 나눠지지않고 소수점이 나온다면 부감독관이 1명 더 필요함)
            superviser += (students // C + 1)
        elif students / C == students // C:         # 나누어 떨어지면 그대로 더하기
            superviser += students // C
    
    result += superviser    # 반마다 나온 결과값 result에 더해주기
    
print(result)       # 최종 필요한 감독관 수