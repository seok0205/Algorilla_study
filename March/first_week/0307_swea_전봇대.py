T = int(input())
for t in range(1, T+1):
    lines_num = int(input())
    lines = []
    answer = 0
    for i in range(1, lines_num+1):
        A, B = map(int, input().split())
        for prev_a, prev_b in lines:
            if (A > prev_a and B < prev_b) or (A < prev_a and B > prev_b):
                answer += 1

        lines.append((A, B))
    print(f"#{t} {answer}")