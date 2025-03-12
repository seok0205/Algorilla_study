'''
100 50
output = 48

2 4
output = 2
'''

N, M = map(int, input().split())
if N == 1:
    print(1)
elif N == 2:
    print(min((M+1) // 2, 4))
else:
    if 1 <= M <= 6:
        print(min(4, M))
    elif M > 6:
        print(5 + (M-7))