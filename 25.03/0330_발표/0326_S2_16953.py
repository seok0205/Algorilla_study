'''
S2 16953 A -> B

정수 A를 B로 바꾸려한다. 가능한 연산은 다음 2가지
1. 2를 곱함
2. 1을 수의 가장 오른쪽에 추가함

A를 B로 바꾸는데 필요한 연산의 최솟값 구하라

첫째 줄에 A, B(1 <= A < B <= 10**9) 주어짐
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal(s, e, cnt):
    global result
    
    if s > e:               # 이미 목표값을 넘어섰다면 함수 종료
        return
    
    if s == e:                      # 목표값에 도달했다면 이때까지 연산횟수를 최솟값인지 판단
        result = min(result, cnt)
        return
    
    add_one = int(str(s) + '1')     # 숫자 뒤에 1을 붙이는 연산을 위한 과정
    
    cal(s*2, e, cnt+1)      # 2를 곱하거나
    cal(add_one, e, cnt+1)  # 1을 오른쪽 끝에 붙이거나


A, B = map(int, input().split())
result = float("inf")

cal(A, B, 0)        # A를 B로 만들기, 횟수는 0부터 시작

if result == float("inf"):      # 만약 최솟값을 갱신하지 못했으면
    result = -1                 # -1로 출력
else:
    result += 1                 # 최솟값 찾았으면 그 값에 1을 더해서 출력

print(result)