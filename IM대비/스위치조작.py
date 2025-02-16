# i번 스위치를 조작시
# i번부터 N번까지 전등 상태 변경
# 현재 상태와 조작 후 상태가 주어지면 최소 몇 개의 스위치 조작?
T = int(input())
for t in range(1, T+1):
    N = int(input())
    s_switch = list(map(int, input().split()))
    e_switch = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if s_switch[i] != e_switch[i]:
                for k in range(i, N):
                    s_switch[k] = s_switch[k] ^ 1
                count += 1
                break
        else:
            break
    print(f'#{t} {count}')