'''
높이가 B 이상인 탑 중 최소 높이와 B간 차이 출력

1
5 16
1 3 3 5 6
'''

def find_shortest(idx, path=[], total_height=0):
    global shortest_height

    if total_height >= B:
        shortest_height = min(shortest_height, total_height)
        # print(path)
        return

    if idx >= N:
        return

    if total_height >= shortest_height:
        return

    find_shortest(idx+1, path + [people_heights[idx]], total_height + people_heights[idx])

    find_shortest(idx+1, path, total_height)


T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())  # N: 사람 수, B: 만들어야 하는 높이
    people_heights = list(map(int, input().split()))  # 사람들 키
    shortest_height = float('inf')
    selected = [0] * (N+1)
    find_shortest(0)

    print(f"#{t} {abs(shortest_height - B)}")
