import sys
input = sys.stdin.readline
'''
N x N 크기의 도시
각 칸은 빈 칸, 치킨집, 집 3가지 중 하나
0 : 빈 칸, 1 : 집, 2 : 치킨집
(r, c) = (1, 1)부터 시작
치킨 거리 => 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리 => 모든 집의 치킨 거리의 합
거리는 |x1 - x2| + |y1 - y2|로 구한다.
도시에 있는 치킨집 중에서 최대 M개를 고르고 나머지는 모두 폐업 시켜야 함.
어떻게 폐업시키면 도시의 치킨 거리가 가장 작게 될지 구하라
'''
def cal(info):
    total = 0
    for i, j in homes:
        min_dis = float('inf')
        for k in info:
            r, c = stores[k]
            dis = abs(i-r) + abs(j-c)
            min_dis = min(min_dis, dis)
        total += min_dis
    return total      
        
def make_comb(cnt, nums):
    global result
    
    if len(nums) == M:
        dis = cal(nums)
        result = min(result, dis)
        return  
       
    if cnt == count:
        return
    
    nums.append(cnt)
    make_comb(cnt+1, nums)
    nums.pop()
    make_comb(cnt+1, nums)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = 0
stores = []
homes = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            count += 1
            stores.append((i, j))
        if arr[i][j] == 1:
            homes.append((i, j))

result = float('inf')
make_comb(0, [])

print(result)