T = int(input())
for t in range(1,T+1):
    N = int(input())   # 리스트의 길이
    num_list = list(map(int, input().split()))    # 숫자를 받은 리스트

    max_idx = 0
    min_idx = 0
    for i in range(len(num_list)):
        if num_list[i] == max(num_list):
            max_idx = i   # 최댓값이 중복되면 더 큰 인덱스를 지정

    for i in range(len(num_list)):        
        if num_list[i] == min(num_list):
            min_idx = i
            break          # 최소값이 중복되면 더 작은 인덱스를 지정
    diff = max_idx - min_idx
    if diff < 0:           
        diff = min_idx - max_idx
    print(f'#{t} {diff}')





