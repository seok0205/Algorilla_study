for _ in range(10):
    t, num_of_roads = map(int, input().split())
    input_arr = list(map(int, input().split()))

    nodes = [[] for _ in range(num_of_roads)]
    for i in range(0, len(input_arr), 2):
        nodes[i//2].append(input_arr[i])
        nodes[i//2].append(input_arr[i+1])

    adj_list = [[] for _ in range(100)]

    for v, w in nodes:
        adj_list[v].append(w)

    visited = [0] * 100
    stack = []

    v = 0
    answer = 0

    while True:
        if visited[v] == 0:
            visited[v] = 1
        if v == 99:
            answer = 1
            break
        for w in adj_list[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break


    print(f"#{t} {answer}")