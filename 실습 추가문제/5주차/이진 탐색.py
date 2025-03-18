def binary_search(num):
    global count
    flag = None
    
    l = 0
    r = len(A)
    while l <= r:
        m = (l+r) // 2
        if A[m] == num:
            count += 1
            return
        
        elif A[m] > num:
            if flag == 'L':
                return
            flag = 'L'
            r = m - 1
            
        elif A[m] < num:
            if flag == 'R':
                return
            flag = 'R'
            l = m + 1


# 서로 다른 정수 N개 주어지면 정렬해서 A리스트에 저장
# B에 저장된 M개의 정수에 대해 A에 들어 있는 수인지 이진탐색 통해 확인
# 양쪽을 번갈아 확인하는 경우만 count
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    count = 0
    for num in B:
        binary_search(num)
    print(f'#{t} {count}')