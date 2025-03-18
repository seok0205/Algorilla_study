
def in_heap(num):
    global last, heap
    
    last += 1
    if last >= len(heap):
        heap.append(num)
    else:
        heap[last] = num
    
    c = last
    p = c // 2
    
    # 부모를 비교후 본인이 더 크면 본인과 부모를 바꿔준다.
    
    # 부모가 존재하고 내가 부모보다 작아질 때까지 반복
    while p and heap[c] > heap[p]:
        heap[c], heap[p] = heap[p], heap[c]
        c = p
        p = c // 2


def de_heap():
    # 루트의 원소를 임시저장
    # 가장 마지막 노드의 값을 루트에 올린다.
    # 아래로 내려가면서 루트가 아래의 값들보다 작으면 바꿔주면서 내려간다.
    global last, heap
    if last == 0:
        return -1
    
    temp = heap[1]
    heap[1] = heap[last]
    last -= 1
    
    p = 1
    c = p * 2
    
    while c <= last:
        # 오른쪽 자식이 있으면 왼쪽 자식과 오른쪽 자식을 비교후
        # 오른쪽 자식이 더 크면 자식 인덱스르 오른쪽으로 바꿔준다.
        # 만약 부모가 자식보다 작으면 그 자식과 바꿔준다.
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1

        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
        
    return temp
    
# 완전 이진 트리
T = int(input())
for t in range(1, T+1):
    # 연산 1 : 삽입
    # 연산 2 : 루트 출력
    # 출력할 루트가 없으면 -1 출력
    N = int(input())    # 연산의 수
    
    last = 0
    heap = [0]
    result = []
    for i in range(N):
        order = list(map(int, input().split()))
        if order[0] == 1:
            in_heap(order[1])
        else:
            result.append(de_heap())
            
    print(f'#{t}', *result)