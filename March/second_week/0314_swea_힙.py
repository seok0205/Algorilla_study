'''
2
3
1 1
2
2
5
1 3
1 5
2
1 1
2
'''
# heap 직접 구현
def enq(node):
    global last

    last += 1
    heap[last] = node

    child = last
    parent = child // 2

    while parent and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

def deq():
    global last

    tmp = heap[1]
    if last == 0:
        return -1
    else:
        heap[1] = heap[last]
        last -= 1

    parent = 1
    child = parent * 2
    while child <= last:
        if child + 1 <= last and heap[child] < heap[child+1]:
            child += 1
        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
            parent = child
            child = parent * 2
        else:
            break

    return tmp

T = int(input())
for t in range(1, T+1):
    num_calc = int(input())
    heap = [0] * (num_calc + 1)
    last = 0
    answer = []
    for _ in range(num_calc):
        input_data = input().split()
        if input_data[0] == "1":
            enq(int(input_data[1]))
        else:
            answer.append(deq())

    print(f"#{t}", *answer)

# heapq 사용
import heapq

T = int(input())
for t in range(1, T+1):
    num_calc = int(input())
    heap = []
    last = 0
    answer = []
    for _ in range(num_calc):
        input_data = input().split()
        if input_data[0] == "1":
            heapq.heappush(heap, -int(input_data[1]))
        else:
            try:
                answer.append(abs(heapq.heappop(heap)))
            except:
                answer.append(-1)

    print(f"#{t}", *answer)