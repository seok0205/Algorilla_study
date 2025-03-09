def post_order(i):
    if i:
        if left[i]:  # 왼쪽 자식 방문
            post_order(left[i])
        if right[i]:  # 오른쪽 자식 방문
            post_order(right[i])

        # 현재 노드가 연산자라면 연산 수행
        if isinstance(tree[i], str):  
            if tree[i] == '+':
                tree[i] = tree[left[i]] + tree[right[i]]
            elif tree[i] == '-':
                tree[i] = tree[left[i]] - tree[right[i]]
            elif tree[i] == '/':
                tree[i] = tree[left[i]] / tree[right[i]]  # 실수 연산
            elif tree[i] == '*':
                tree[i] = tree[left[i]] * tree[right[i]]


T = 10
for t in range(1, 1+T):
    # 정점의 수
    N = int(input())
    # 입력을 문자열로 받음
    arr = [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    
    for i in range(N):
        if arr[i][1].isnumeric():
            tree[i+1] = int(arr[i][1])  # 숫자일 경우 int 변환
        else:
            tree[i+1] = arr[i][1]  # 연산자 저장
            left[i+1] = int(arr[i][2])  # 왼쪽 자식
            right[i+1] = int(arr[i][3])  # 오른쪽 자식
         
    post_order(1)  # 후위 순회로 연산 수행
    result = int(tree[1])  # 정수로 변환하여 출력

    print(f'#{t} {result}')
