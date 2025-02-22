T = int(input())
for t in range(1, T+1):
    original = list(map(int, input()))
    len_original = len(original)

    default = [0] * len_original

    counts = 0
    idx = 0
    while True:
        if original == default:
            break
        if original[idx] != default[idx]:
            for i in range(idx, len_original):
                default[i] = default[i] ^ 1
            counts += 1
            continue
        else:
            idx += 1

    print(f"#{t} {counts}")