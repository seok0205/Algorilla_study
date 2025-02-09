T = int(input())

for t in range(1, T + 1):
    N = int(input())
    sequence = input().strip()

    max_count = 0
    current_count = 0

    for bit in sequence:
        if bit == "1":
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 0

    if current_count > max_count:
        max_count = current_count

    print("#" + str(t), max_count)
