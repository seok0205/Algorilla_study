'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
> 3

4
1 4
3
1 2
1 3
3 4
> 2

9
8 6
8
1 2
1 3
2 7
2 8
2 9
4 5
4 6
9 4
> 4
'''

def dfs(node, count):
    global flag

    if node == target2:
        flag = True
        print(count)
        return

    for next_node in nodes[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, count + 1)



total = int(input())
target1, target2 = map(int, input().split())
num_edges = int(input())
nodes = [[] * (total + 1) for _ in range(total + 1)]
visited = [False] * (total + 1)
for _ in range(num_edges):
    parent, child = map(int, input().split())
    nodes[parent].append(child)
    nodes[child].append(parent)
# print(nodes)
visited[target1] = True
flag = False
dfs(target1, 0)
if not flag:
    print(-1)

'''
            1          4
        2      3      5 6
       7 8 9


          1         
      2       3    
    7 8 9           
        4
       5 6
'''
