import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
arr = [(i+1) for i in range(N)]
q = deque(arr)

result = []
while q:
    for _ in range(K-1):
        q.append(q.popleft())
        
    result.append(q.popleft())
    
print('<',end='')
for i in range(N-1):
    print(result[i],end= ', ')
print(result[-1],end='')
print('>')

    