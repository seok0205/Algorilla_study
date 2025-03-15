'''
완전이진트리
루트는 항상 1

9
1 * 2 3
2 + 4 5
3 - 6 7
4 / 8 9
5 2
6 6
7 4
8 8
9 7

9
1 * 2 3
2 + 4 5
3 - 6 7
4 / 8 9
5 2
6 6
7 4
8 8
9 *

9
1 * 2 3
2 2 4 5
3 - 6 7
4 / 8 9
5 2
6 2
7 7
8 8
9 7

'''

def is_valid(node):
    if node <= num_nodes:   # 완전이진트리이므로 해당 노드가 트리 안에 있을 때만 체크하려면 node <= num_nodes 해야 함
        left_child = is_valid(node * 2)
        right_child = is_valid(node * 2 + 1)
        # 해당 노드가 리프노드이면 자기 값 리턴
        if left_child is None and right_child is None:
            return nodes[node]
        # 자식이 숫자가 아니거나 부모가 연산자가 아니라면 연산이 불가능하므로 False 리턴
        if type(left_child) is not int or type(right_child) is not int or type(nodes[node]) is int:
            return False
        else:
            # 계산이 가능하다면 (자식이 숫자, 부모가 연산자)
            # 계산은 따로 안 해도 되는데 부모가 연산자일 때 계산이 가능하도록 숫자로 바꾸는 과정
            nodes[node] = left_child + right_child

        return nodes[node]   # 리프노드가 아닐 때 계산된 값을 리턴해줘야 부모 노드가 이 자식 노드 값으로 계산이 가능함


for t in range(1, 11):
    num_nodes = int(input())
    nodes = [0] * (num_nodes + 1)
    left_child_idxs = [0] * (num_nodes + 1)
    right_child_idxs = [0] * (num_nodes + 1)
    answer = 0
    for _ in range(num_nodes):   # 여기 for loop은 다 입력값 받는 부분
        input_data = input().split()
        node_idx = int(input_data[0])
        if len(input_data) >= 2:
            nodes[node_idx] = int(input_data[1]) if input_data[1].isnumeric() else input_data[1]
            if len(input_data) == 3:
                left_child_idxs[node_idx] = int(input_data[2])
            if len(input_data) == 4:
                left_child_idxs[node_idx] = int(input_data[2])
                right_child_idxs[node_idx] = int(input_data[3])

    if is_valid(1):
        answer = 1

    print(f"#{t} {answer}")
