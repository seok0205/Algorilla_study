from collections import deque
# 위에서 부터 1 부터 N 까지의 수의 카드 존재
# 버리고 뒤로 보내고 반복
# 마지막에 남는 카드?
N = int(input())

q = deque()
for i in range(1, N+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(*q)