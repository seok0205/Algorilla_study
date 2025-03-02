T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input()))
    # 고용한 사람
    result = 0
    # 현재 박수치고 있는 사람
    count = 0
    for idx, num in enumerate(arr):
        if count < idx:
            result += idx - count
            count += idx - count
            count += num

        else:
            count += num
    
    print(f'#{t} {result}')