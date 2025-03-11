# 최소힙(루트가 트리의 최소값을 가짐)
def in_heap(N):
    global last
    last += 1
    heap[last] = N
    c = last
    p = last // 2
    # 더이상 비교할 부모가 없거나
    # 부모가 자식보다 작이지면 비교 종료
    while p and heap[p] > heap[c]:
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c // 2

T = int(input())
for t in range(1, T+1):
    # 정점의 수
    N = int(input())
    arr = list(map(int,input().split()))
    heap = [0] * 1000000
    last = 0
    for i in range(N):
        in_heap(arr[i])
    result = 0
    # 마지막 노드의 조상번호를 타고 올라감
    c = last // 2
    # 더 이상 조상이 없으면 종료
    while c > 0:
        result += heap[c]
        c = c // 2
    print(f'#{t} {result}')