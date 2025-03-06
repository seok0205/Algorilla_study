'''
모험가 N명
공포도가 X -> X명 이상 참여해야 함
여행 떠날 수 있는 그룹의 최대값
공포도가 제일 높은 사람과 그 사람과 공포도가 비슷한 사람들로 그룹 구성? sort?
5
2 3 1 2 2

6
1 3 4 3 3 3
'''

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
count = 0
idx = N - 1
while idx >= 0:
    coward = sorted_arr[idx]
    if coward > len(sorted_arr):
        idx -= 1
        continue
    else:
        for _ in range(coward):
            idx -= coward
        count += 1
print(count)