'''
가장 높은 숫자 카드 뽑기
뽑고자 하는 카드가 포함된 행 선택 -> 선택된 행에서 가장 낮은 숫자 카드 뽑아야 함

3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''
# 쉽게 생각하면 각 행의 가장 작은 숫자를 모아 그 중 가장 큰 수를 구하면 되는데
# 나는 너무 돌아돌아 찾음

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

# not the smallest card row
target_row_idx = None
for i in range(N):
    max_among_smallest = 0
    if min(cards[i]) > max_among_smallest:
        max_among_smallest = min(cards[i])
        target_row_idx = i
print(target_row_idx)

print(min(cards[i]))