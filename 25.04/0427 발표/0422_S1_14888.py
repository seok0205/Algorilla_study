'''
S1 14888 연산자 끼워넣기

N개의 수로 이루어진 수열이 주어짐.
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어짐. (+, -, *, //)

수와수 사이에 하나씩 연산자를 넣어서 수식하나 만들 수 있음.
주어진 수의 순서를 바꾸는 건 안됨.

우선순위 무시하고 앞에서부터 진행해야함.
음수를 양수로 나눌 땐 C++14 기준 따름(양수를 바꾼뒤 몫을 취하고, 그 몫을 음수로 바꿈)

N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 문제

입력:
첫째 줄에 수의 개수 N
둘째 줄에 수열
셋째줄에는 합이 N-1인 4개의 정수. 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal(num, cnt, cal_idx):
    '''
    사칙연산 하는 dfs 함수

    num : 이때까지 연산으로 나온 숫자
    cnt : 연산 횟수(즉, 연산자를 쓴 횟수와, 다음 계산할 nums의 인덱스로 통용)
    cal_idx : 연산자 인덱스
    '''
    global min_result, max_result       # 최솟값 최댓값

    if cnt == N-1:                          # 만약 연산자 기호 모두 다 썼다면, 최종값 비교 후 함수 종료
        min_result = min(min_result, num)
        max_result = max(max_result, num)
        return

    if calculator[cal_idx] == 0:            # 중간에 해당 연산자 횟수가 남아있지 않다면 함수 종료
        return

    if cal_idx == 0:            # cal_idx에 따라 연산할 방식이 다름
        num += nums[cnt+1]
    elif cal_idx == 1:
        num -= nums[cnt+1]
    elif cal_idx == 2:
        num *= nums[cnt+1]
    elif cal_idx == 3:
        if num >= 0:
            num //= nums[cnt+1]
        else:
            num = -(abs(num) // nums[cnt+1])

    calculator[cal_idx] -= 1        # 계산한 연산자 횟수 없애주고
    cal(num, cnt+1, 0)              # 4가지 연산자 모두 계산한 뒤
    cal(num, cnt+1, 1)
    cal(num, cnt+1, 2)
    cal(num, cnt+1, 3)
    calculator[cal_idx] += 1        # 다른 경우의 수들을 위해 다시 복구


N = int(input())
nums = list(map(int, input().split()))
calculator_lst = list(map(int, input().split()))

min_result = 1000000000         # 문제에서 최대 최소가 10억과 -10억.
max_result = -1000000000

for i in range(4):              # 시작 연산자 정하기. 횟수가 있어야 시작 가능.
    calculator = calculator_lst[:]
    if calculator[i]:
        cal(nums[0], 0, i)

print(max_result)
print(min_result)