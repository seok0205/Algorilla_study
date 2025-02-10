"""
G5 12865 평범한 배낭

여행을 감. N개의 물건이 존재. 각 물건은 W의 무게와 V의 가치를 지님.
해당 물건을 가져가면 V만큼 즐길 수 있는 것. 최대 K만큼의 무게를 넣을 수 있는 배낭.
최대한 V를 높이는 배낭에 넣을 수 있는 물건들의 가치의 최댓값 구하는 문제

입력:
N : 물품의 수(100 이하), K : 버틸 수 있는 무게(100,000 이하)
W : 물건의 무게(100,000 이하), V : 물건의 가치(1,000 이하)

출력:
가치합의 최댓값
"""

N, K = list(map(int, input().split()))
inven = list()
bag = {0: 0}

for i in range(N):
    W, V = list(map(int, input().split()))
    inven.append([W, V])

inven.sort(reverse=True)

for weight, value in inven:
    tmp = dict()
    for bag_w, bag_v in bag.items():
        next_v = bag_v + value
        next_w = bag_w + weight

        # dict.get으로 키(next_v)에 해당하는 값 반환, 존재 안하면 k+1 반환
        if bag.get(next_v, K+1) > next_w:
            tmp[next_v] = next_w
    # update로 키값 쌍 추가, 이미 존재하면 새 값 업데이트
    bag.update(tmp)
print(max(bag.keys()))