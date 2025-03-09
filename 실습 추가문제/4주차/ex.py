# 최대 힙은 루트의 값이 그 트리에서
# 가장 큰 값이라는 것만 증명되어있음
# 따라서 디큐를 할 때에 루트의 값만 추출을 하는 형식으로
# 트리가 빌때까지 디큐를 하면 내림차순 정렬이 됨!
last = 0
def enq(n):
    global last     # 정점 인덱스 (현재의 트리에서 마지막 정점에 넣을거임)
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key추가
    
    c = last        # 자식 정점 번호
    p = c // 2       # 완전 이진 트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:  # 부모가 있고 부모가 자식보다 작으면
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
        
def deq():
    global last
    # 어떠한 위치를 삭제 시키든 최대힙의 형태를 유지시킬거임
    temp = heap[1]          # 힙의 루트값을 임시저장, 현재의 루트 값을 리턴할거임
    heap[1] = heap[last]    # 루트에 삭제할 노드의 키를 넣음
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2
    while c <= last:
        # 만약 오른쪽 자식이 존재하고 
        # 오른쪽 자식이 왼쪽 자식보다 크면 
        # 부모와 비교할 대상을 오른쪽 자식으로 지정
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1
        # 만약 자식이 부모보다 크면 바꿔준다.
        if heap[p] < heap[c]:
            heap[p] , heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:       # 자식이 부모보다 작으면 종료
            break
    return temp
heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
print(heap)
while last:
    print(deq())