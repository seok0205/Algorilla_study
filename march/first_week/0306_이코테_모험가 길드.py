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

# 공포도가 제일 높은 사람을 기준으로 그룹을 결성하면 많은 그룹을 가지지 못하기 때문에
# 공포도가 제일 낮은 순으로 그룹 안에 넣고 그룹 다 차면 보내는 방식으로 해야 함
N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
group_count = 0
members_count = 0

for coward in sorted_arr:
    members_count += 1
    if members_count >= coward:
        group_count += 1
        members_count = 0

print(group_count)