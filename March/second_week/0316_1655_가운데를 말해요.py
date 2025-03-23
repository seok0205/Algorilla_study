'''
7
7
5
2
10
-99
1
2
'''

import heapq
import sys

N = int(sys.stdin.readline())
leftheap = []  # 최대힙으로
rightheap = [] # 최소힙으로
for _ in range(N):
    node = int(sys.stdin.readline())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -node)
        # print('left : ', leftheap)
        # print('right : ', rightheap)
    else:
        heapq.heappush(rightheap, node)
        # print('left : ', leftheap)
        # print('right : ', rightheap)

    if rightheap and -leftheap[0] > rightheap[0]:
        left_val = heapq.heappop(leftheap)
        right_val = heapq.heappop(rightheap)

        heapq.heappush(rightheap, -left_val)
        heapq.heappush(leftheap, -right_val)
        #
        # print('left : ', leftheap)
        # print('right : ', rightheap)

    print(-leftheap[0])
