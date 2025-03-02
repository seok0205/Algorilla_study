T = int(input())
for t in range(1, T+1):
    # N의 배수로 수를 센다.
    N = int(input())
    # 이때까지 센 숫자들의 각 자리수가 0부터 9까지 모두
    # 나왔을때 몇번 수를 세야 되는가?
    count_set = set()
    num_list = []
    count = 0
    while len(count_set) < 10:
        num_list.append(N*(count+1))
        q = str(N * (count+1))
        count_set.update(q)
        count += 1
        
    result = num_list[-1]
    print(f'#{t} {result}')
