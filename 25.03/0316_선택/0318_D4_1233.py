'''
D4 1233 사칙연산 유효성 검사

사칙 연산으로 구성된 식은 이진 트리로 표현 가능
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의
결과를 사용해서 해당 연산자를 적용

사칙연산 +, -, /, *와 양의 정수로만 구성된 임의의 이진 트리가 주어질 때,
이 식의 유효성을 검사하는 프로그램 작성(적절한 식인지 확인)

계산 가능하면 1, 불가능 시 0 출력, 0으로 나누는 경우 고려 X
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal(idx):
    global result
    
    if len(edge[idx]) == 2:     # 갈 수 있는 간선이어야 두 수와 연산자를 사용할 수 있음
        cal(edge[idx][0])
        cal(edge[idx][1])
    else:                       # 만약 길이가 안되는데(무조건 숫자가 존재해야함) 해당 노드에 있는 값이 연산자면 사칙연산이 불가능함. 
        if tree[idx] not in "+-*/":
            return
        else:
            result = 0
            return
    
    if tree[idx] in '+-*/':     # 만약 연산자가 있으면 해당 연산자는 계산한 값으로 바뀔 것임
        tree[idx] = '1'         # 계산 유효성만 판단하면 되므로 연산자가 아닌 값으로 바꿔줌
        return

for tc in range(1, 11):
    N = int(input())
    tree = [0]
    edge = [0]
    for _ in range(N):
        info = list(map(str, input().split()))
        tree.append(info[1])
        edge.append(list(map(int, info[2:])))
    
    result = 1      # 조건에 걸리는 게 없으면 그대로 1출력
    cal(1)
    
    print(f'#{tc} {result}')