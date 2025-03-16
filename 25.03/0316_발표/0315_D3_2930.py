'''
D3 2930 힙

힙은 최댓값 혹은 최솟값 찾아내는 연산 빨리 하기 위한 자료 구조
완전 이진트리를 기본으로 한 자료구조, 다음 속성 만족
"A가 B의 부모노드이면, A의 키값과 B의 키값 사이에는 항상 일정한 대소관계가 성립"

부모 자식만 성립, 형제 노드 사이는 관계가 정해지지 않음
부모노드 키값이 자식노드 키값보다 항상 크거나 같은 힙을 최대 힙
부모노드 키값이 자식노드 키값보다 항상 작거나 같은 힙을 최소 힙

힙의 루트노드는 힙을 구성하는 키값 중 최댓값 혹은 최솟값을 가지게 됨
본 문제에선 최대힙을 올바르게 구현하였는지 확인

연산 1. 자연수 x 삽입
연산 2. 최대 힙의 루트 노드의 키값을 출력, 해당 노드 삭제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

# from collections import deque


# def heap(d):
#     if d > len(tree)//2:
#         return
    
#     heap(d*2)
#     heap(d*2+1)
    
#     if d*2-1 < len(tree):
#         if tree[d-1] < tree[d*2-1]:
#             tree[d-1], tree[d*2-1] = tree[d*2-1], tree[d-1]
    
#     if d*2 < len(tree):
#         if tree[d-1] < tree[d*2]:
#             tree[d-1], tree[d*2] = tree[d*2], tree[d-1]


def heappush(n):
    heap.append(n)
    cur_node = len(heap) - 1                # 추가한 노드의 인덱스를 구함
    while cur_node > 0:                     # 현재 노드가 인덱스 0(root)에 도달하면 종료
        p_node = (cur_node - 1) // 2        # 추가한 노드의 부모 노드를 구함
        if heap[p_node] < heap[cur_node]:
            heap[p_node], heap[cur_node] = heap[cur_node], heap[p_node]
            cur_node = p_node               # 추가한 노드의 인덱스를 갱신
        else:
            break


def heappop():
    if not heap:        # 힙에 아무것도 없으면 -1 반환
        return -1
    elif len(heap) == 1:            # 힙의 길이 1이면 그냥 pop()하면 루트 노드 값 도출됨
        return heap.pop()

    pop_data, heap[0] = heap[0], heap.pop()         # 원래 루트 노드 기억, 힙의 최상위에 끝의 노드 설정
    cur, c_node = 0, 1                              # 첫 시작 부모 노드와 자식 노드 인덱스 값
    while c_node < len(heap):                       # 자식 노드가 힙의 전체 길이보다 작을때만 실행(이진 트리 끝까지 실행)
        s_node = c_node + 1                         # 형제 노드의 인덱스
        if s_node < len(heap) and heap[c_node] < heap[s_node]:      # 자식노드가 존재하고, 형제노드가 더 크면
            c_node = s_node                                         # 비교 대상을 형제노드로 변경
        if heap[cur] < heap[c_node]:                                # 부모노드와 비교후
            heap[cur], heap[c_node] = heap[c_node], heap[cur]       # 부모노드가 더 작으면 두 노드 값 교체
            cur = c_node                                            # 비교했던 자식노드가 다음 부모노드
            c_node = cur * 2 + 1                                    # 자식노드는 부모노드가 된 현재 노드 넘버(인덱스)의 두배(인덱스라서 +1 해줘야함)
        else:                                                       # 다음 존재하지 않으면 중단
            break
    return pop_data         # 원래 루트 노드의 값을 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    # result = []
    # tree = deque()
    
    # for _ in range(N):
    #     info = input()
        
    #     if info[0] == '1':
    #         cal, num = map(int, info.split())
    #     else:
    #         cal = int(info)
        
    #     if cal == 1:
    #         tree.append(num)
    #     else:
    #         if len(tree) >= 1:
    #             heap(1)
    #             result.append(tree.popleft())
    #         elif len(tree) == 0:
    #             result.append(-1)
            
    # print(f'#{tc} {" ".join(map(str, result))}')
    
    result = []
    heap = []
    
    for _ in range(N):
        info = input()
        
        if info[0] == '1':
            cal, num = map(int, info.split())
        else:
            cal = int(info)
        
        if cal == 1:        # 1번 연산이면 heappush()
            heappush(num)
        else:               # 2번 연산이면 heappop() 하고, 반환받은 값을 result에 추가
            result.append(heappop())
            
    print(f'#{tc} {" ".join(map(str, result))}')