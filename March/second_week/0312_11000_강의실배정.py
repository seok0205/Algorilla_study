'''
6
1 10
2 3
2 3
2 3
2 3
3 4

3
1 10
2 4
4 5
'''

# TODO: 풀이중

import heapq

N = int(input())
time_table = [list(map(int, input().split())) for _ in range(N)]
time_table.sort(key=lambda x: (x[0], x[1]))

heap = [time_table[0][1]]   # time table 값 하나 중 end
for i in range(1, N):
    if heap[0] <= time_table[i][0]:   # heap 에 있는 time table end 값과 time table에 있는 다음 값의 start 비교
        heapq.heappop(heap)
    heapq.heappush(heap, time_table[i][1])
print(len(heap))


