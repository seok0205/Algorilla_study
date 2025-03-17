'''
임의의 두 정점의 가장 가까운 공통 조상 찾고
그 정점을 루트로 하는 서브트리 크기 (정점 총 개수) 출력 (공통조상번호, 서브트리 총 정점 개수 출력)
루트 정점은 항상 1
정점 번호는 1 ~ V까지의 정수
'''
from collections import deque


def find_ancestor(node_idx):
    ancestor = []
    idx = node_idx
    distance = 0
    while nodes[idx] != 0:
        idx = nodes[idx]
        distance += 1
        ancestor.append((distance, idx))

    return ancestor


def find_subtree_amount(node_idx):
    global count
    Q = deque()
    Q.append(node_idx)
    while Q:
        curr = Q.popleft()
        if left_child[curr]:
            count += 1
            Q.append(left_child[curr])
        if right_child[curr]:
            count += 1
            Q.append(right_child[curr])


T = int(input())
for t in range(1, T + 1):
    num_nodes, num_edges, node1, node2 = map(int, input().split())
    nodes = [0] * (num_nodes + 1)  # child idx, parent value
    left_child = [0] * (num_nodes + 1)
    right_child = [0] * (num_nodes + 1)
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        parent = arr[i]
        child = arr[i + 1]
        nodes[child] = parent
        if not left_child[parent]:
            left_child[parent] = child
        else:
            right_child[parent] = child

    node1_ancestor = find_ancestor(node1)
    node2_ancestor = find_ancestor(node2)
    node_ancestor = node1_ancestor + node2_ancestor
    node_ancestor.sort(key=lambda x: (x[0], x[1]))
    # print(node_ancestor)
    same_parent_idx = 0
    distance_diff = float('inf')
    total_distance = float('inf')
    for i in range(len(node_ancestor)):
        for j in range(i+1, len(node_ancestor)):
            if node_ancestor[i][1] == node_ancestor[j][1] and node_ancestor[i][0] + node_ancestor[j][0] < total_distance:
                same_parent_idx = node_ancestor[i][1]
                total_distance = node_ancestor[i][0] + node_ancestor[j][0]

    count = 1
    find_subtree_amount(same_parent_idx)
    print(f"#{t} {same_parent_idx} {count}")
