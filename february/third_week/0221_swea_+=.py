# 1 2 3 : 1 + 2 = 3 -> 3 + 2 = 5 -> 5 + 3 = 8

T = int(input())
for t in range(1, T+1):

    A, B, N = map(int, input().split())

    answer = 0
    count = 0
    while True:
        answer = A + B
        count += 1
        if answer > N:
            break
        max_val = max(A, B)
        A = answer
        B = max_val

    print(count)