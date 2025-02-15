T = int(input())
for t in range(1, T+1):
    num_of_lights = int(input())

    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    idx = 0
    count = 0
    while before != after:
        # compare = list(zip(before, after))

        before_val = before[idx]
        after_val = after[idx]

        if before_val != after_val:
            for i in range(idx, num_of_lights):
                before[i] = 1 if before[i] == 0 else 0
            count += 1
            # idx = 0
            if before == after:
                break
        else:
            idx += 1

    print(f"#{t} {count}")
