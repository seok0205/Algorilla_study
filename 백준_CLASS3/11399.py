import sys
# N명의 사람 줄 서있다.
# i번째 사람이 인출하는데 P분 걸림
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
result = 0
for i in range(N):
    result += sum(arr[:i+1])
print(result)