'''
N개의 시험장, i번 시험장에있는 응시자수는 A명
총 감독관이 관리 가능한 사람 : B명
부 감독관                   : C명
총감독관은 1명, 부감독관은 여러명 상관없음
응시생을 모두 감시해야됨
감독관의 수 최솟값
'''
import sys
input = sys.stdin.readline
# 시험장의 개수
N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for i in range(N):
    count += 1
    temp = arr[i] - B
    if temp > 0:
        if temp % C > 0:
            count += temp // C + 1
        else:
            count += temp // C
print(count)