# 조건
# 1. 대 중 소 상자로 구분해 포장
# 2. 같은 크기의 당근은 같은 상자에 들어있어야 함
# 3. 비어있는 상자가 있으면 안 됨
# 4. 한 상자에 N/2개 (N이 홀수면 소수점 버림) 를 초과하는 당근이 있어서도 안 됨
# 5. 각 상자의 개수 차이가 최소가 되는 것을 찾아야 함
# 6. 포장할 수 없을 경우 -1 출력 / 포장할 수 있으면 차이값 출력

# 8개 -> 1/1/6, 1/2/5, 1/3/4, 2/2/4, 2/3/3,
# 11223 -> 1,1 / 2,2 / 3

# TODO: 푸는 중~~~~

def make_groups(num):
    groups = []
    for i in range(1, num - 2):
        alpha = 0
        for j in range(1, num - 1 - alpha):
            group = [0, 0, 0]
            group[0] = i
            if 8 - i - j <= 0:
                break
            group[1] = j
            group[2] = num - i - j
            alpha += 1
            groups.append(group)

    idx = 0
    while idx < len(groups):
        if max(groups[idx]) > num // 2:
            groups.pop(idx)
            continue
        idx += 1

    return groups

print(make_groups(8))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    counts = [0 for _ in range(30)]

    for num in arr:
        counts[num] += 1
    print(counts)
    max_duplicates = max(counts)
    min_diff = N
    groups = make_groups(N)
    for group in groups:
        a = group[0]
        b = group[1]
        c = group[2]
        if max_duplicates not in (a, b, c):
            answer = -1
            break
        else:
            idx = 0
            while a > 0:
                if counts[idx] > 0:
                    counts[idx] -= 1
                    a -= 1
                    continue
                idx += 1

            while b > 0:
                if counts[idx] > 0:
                    counts[idx] -= 1
                    b -= 1
                    continue
                idx += 1

            while c > 0:
                if counts[idx] > 0:
                    counts[idx] -= 1
                    c -= 1
                    continue
                idx += 1

        if sum(counts) == 0:
            answer = max(group) - min(group)
            if answer < min_diff:
                min_diff = answer

    print(f"#{t} {answer}")

# groups = []
# # arr = [1,2,3,4,5,6,7,8]
# for i in range(1, 8-2):
#     alpha = 0
#     for j in range(1, 8-1-alpha):
#         group = [0, 0, 0]
#         group[0] = i
#         if 8-i-j <= 0:
#             break
#         group[1] = j
#         group[2] = 8-i-j
#         # print(group)
#         alpha += 1
#         groups.append(group)
#
# idx = 0
# while idx < len(groups):
#     if max(groups[idx]) > 8 // 2:
#         groups.pop(idx)
#         continue
#     idx += 1
#
# print(groups)



