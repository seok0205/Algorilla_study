# on: 1 off: 0
# 000 -> 010 (idx 1부터 조작 - idx2 조작)

T = int(input())
for t in range(1, T+1):
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    count = 0



    print(f"#{t}")