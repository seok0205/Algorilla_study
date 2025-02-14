T = int(input())
for t in range(1, T+1):

    N = int(input())
    cards = list(input().split())

    middle = N // 2 if N % 2 == 0 else N // 2 + 1

    first_deck = cards[:middle]
    second_deck = cards[middle:]
    first_len = len(first_deck)
    second_len = len(second_deck)

    print(first_deck)
    print(second_deck)

    result = []

    i = 0
    while i < N:
        if first_len > i:
            result.append(first_deck[i])

        if second_len > i:
            result.append(second_deck[i])

        i += 1

    print(f"#{t}", *result)