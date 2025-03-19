'''
D4 15761 크고 작은 이진수의 곱셈

1이 A개, 0이 B개 나타나는 길이가 A+B인 '1'로 시작하는 모든 이진수 가운데
가장 큰 것을 M, 가장 작은 것을 m이라고 함

M X m 의 이진수 표현에서 1이 몇 개 나타나는지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    
    max_num = '1' * A + '0' * B     # 주어진 조건에서 최대 수는 1이 모두 왼쪽에 몰려있어야함
    min_num = '1' + '0' * B + '1' * (A - 1)     # 최솟값은 첫자리만 1이고 나머지 1은 오른쪽에 몰려있어야함
    
    num = bin(int(max_num, 2) * int(min_num, 2))        # 2진수를 10진수 형태로 바꾼다음 곱하고 다시 2진수로 표현
    
    result = num.count('1')     # 0b가 앞에 붙지만 1의 개수만 세면 되므로 count로 1의 개수 세어줌
    
    print(f'#{tc} {result}')