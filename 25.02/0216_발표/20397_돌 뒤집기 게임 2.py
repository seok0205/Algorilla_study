T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone_lst = list(map(int, input().split()))
    
    for _ in range(M):
        i, j = map(int, input().split())
        x = i - 1
        
        for k in range(1, j+1):
            if 0 <= x-k < N and 0 <= x+k < N and stone_lst[x-k] == stone_lst[x+k]:
                if stone_lst[x-k]:
                    stone_lst[x-k] = stone_lst[x+k] = 0
                else:
                    stone_lst[x-k] = stone_lst[x+k] = 1
                    
    print(f'#{tc} {" ".join(map(str, stone_lst))}')