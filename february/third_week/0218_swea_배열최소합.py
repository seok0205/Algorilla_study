'''

3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''

def permutation(i, n, sum_val=0):
    global min_sum

    if i == n:
        if min_sum > sum_val:
            min_sum = sum_val
    elif min_sum < sum_val:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            permutation(i+1, n, sum_val + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [num for num in range(N)]
    min_sum = float('inf')
    permutation(0, N)

    print(f"#{t} {min_sum}")