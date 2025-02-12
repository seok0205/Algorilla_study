T = int(input())
for t in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    result = ''
    for i in range(5):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])
    
    c = 0  # 열 관리
    while c < max_len:
        for i in range(5):
            if c < len(arr[i]):
                result += arr[i][c]
        c += 1
    print(f'#{t} {result}')








            