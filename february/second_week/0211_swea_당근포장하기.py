# 조건
# 1. 대 중 소 상자로 구분해 포장
# 2. 같은 크기의 당근은 같은 상자에 들어있어야 함
# 3. 비어있는 상자가 있으면 안 됨
# 4. 한 상자에 N/2개 (N이 홀수면 소수점 버림) 를 초과하는 당근이 있어서도 안 됨
# 5. 각 상자의 개수 차이가 최소가 되는 것을 찾아야 함
# 6. 포장할 수 없을 경우 -1 출력 / 포장할 수 있으면 차이값 출력

T = int(input())
for t in range(1, T + 1):
    num_of_carrots = int(input())
    arr = list(map(int, input().split()))
    carrots_info = {}
    for size in arr:
        if size not in carrots_info:
            carrots_info[size] = 0
        carrots_info[size] += 1

    carrots_data = sorted([
        {
            "size": size,
            "amount": amount
        } for size, amount in carrots_info.items()
    ], key=lambda x: x['size'])

    # print(carrots_data)

    min_diff = None

    for i in range(1, num_of_carrots - 1):
        for j in range(1, num_of_carrots - i):
            small = sum([carrot_data['amount'] for carrot_data in carrots_data[:i]])
            # print("small : ", small)
            medium = sum([carrot_data['amount'] for carrot_data in carrots_data[i:i+j]])
            # print("medium : ", medium)
            large = sum([carrot_data['amount'] for carrot_data in carrots_data[i+j:]])
            # print("large : ", large)

            if max(small, medium, large) > num_of_carrots // 2:
                continue
            diff = max(small, medium, large) - min(small, medium, large)
            if min_diff is None:
                min_diff = diff
            else:
                min_diff = min(diff, min_diff)

    print(f"#{t}", min_diff if min_diff is not None else -1)
