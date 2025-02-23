'''
D2 21425 +=

x += y를 하면 x에 저장된 값이 y가 더해져 바뀜
현재 x에 저장된 값은 A, y에 저장된 값은 B. 연산을 원하는 순서대로 원하는 만큼
수행해 x, y 둘 중 하나 이상에 저장된 값이 N초과가 되게 하려고함. 연산을 합쳐 최소
몇 번 수행해야 하는지 계산하는 문제
'''

T = int(input())

for tc in range(1, T+1):
    A, B, N = map(int, input().split())
    
    result = 0
    
    while True:         # 한번 계산할때마다 x+=y를 할지 y+=x를 할지 판단해야함
        if B > A:       # A보다 B가 크면
            result += 1
            A += B      # A에다가 B를 더해가는 형식
        else:           # B가 A보다 더 크면
            result += 1
            B += A      # B에다가 A를 더해가는 형식
                
        if A > N or B > N:      # 두 수중 N을 초과하는 수가 생기면 while문 탈출
            break
    
    print(result)