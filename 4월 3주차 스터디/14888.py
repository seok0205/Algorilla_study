import sys
input = sys.stdin.readline
'''
N개의 수로 이뤄진 수열
N-1개의 연산자 (+, -, *, /)
주어진 순서를 바꾸지 않고 사이에 하나의 연산자를 넣어 수식만든다.
음수를 양수로 나눌때는 양수로 바꾸고 나눠준 몫을 음수로 바꾼다.
연산 결과 최대, 최소 구해라
'''
def div(x, y):
    if x < 0:
        return ((x * -1) // y) * -1
    return x // y

def cal(num, cnt):
    global min_val, max_val
    if cnt == N-1:
        min_val = min(num, min_val)
        max_val = max(num, max_val)
        return
    
    for i in range(4):
        if oper[i] == 0:
            continue
        oper[i] -= 1
        if i == 0:
            a = num + arr[cnt+1]
        elif i == 1:
            a = num - arr[cnt+1]
        elif i == 2:
            a = num * arr[cnt+1]
        else:
            a = div(num, arr[cnt+1])
        cal(a, cnt+1)
        oper[i] += 1

N = int(input())
arr = list(map(int, input().split()))
# +, -, *, / 의 갯수
oper = list(map(int ,input().split()))

min_val = 1e10
max_val = -1e10
cal(arr[0], 0)

print(max_val)
print(min_val)