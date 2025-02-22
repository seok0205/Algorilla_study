T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split()) # N: 상자 개수, Q: 작업 횟수
    # L, R (i번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경)
    task = [list(map(int, input().split())) for _ in range(Q)]

    boxes = [0] * (N+1)

    for i in range(1, Q+1):
        L, R = task[i-1]
        for j in range(L, R+1):
            boxes[j] = i

    print(f"#{t}", *boxes[1:])