# 2447. 별 찍기 - 10
# TODO: 다시 풀기 (https://www.acmicpc.net/problem/2447)
def make_stars(n):
    if n == 3:
        return ["***", "* *", "***"]
    else:
        smaller_pattern = make_stars(n//3)
        top_bottom = [line * 3 for line in smaller_pattern]
        middle = [line + " " * (n//3) + line for line in smaller_pattern]

        return top_bottom + middle + top_bottom


N = int(input())
print('\n'.join(make_stars(N)))