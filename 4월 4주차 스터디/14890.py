import sys
input = sys.stdin.readline
# 만약 높이의 차이가 2가 되는 순간 그 길은 쓸 수 없음
# 탐색은 행우선, 열우선 한번씩 돌려야 되고
# 탐색을 하는 시작 쪽이 작은 쪽인 경우
# -> 1칸 높은 칸을 만나면 그 전으로 돌아가서 경사로 길이만큼의 공간이 있나 체크
# 탐색을 하는 시작 쪽이 큰 칸인 경우
# -> 다음 나오는 작은 칸에서 탐색 계속 진행하면서
#   경사로 길이만큼의 공간이 있나 체크
# 경사로 놓은 곳을 체크하자(visited처럼)

N, L = map(int, input().split())
arr1 = [list(map(int ,input().split())) for _ in range(N)]
def change_arr(arr):
    return [list(row) for row in zip(*arr)]
# 전치 행렬
arr2 = change_arr(arr1)

def f(arr):
    count = 0
    for i in range(N):
        visited = [0] * N
        for j in range(1, N):
            now = arr[i][j-1]
            # 만약 바로 전의 칸과 현재 칸이 같으면 continue
            if arr[i][j] == now:
                continue
            
            # 칸의 높이 차이가 2이면 바로 break
            if abs(arr[i][j] - now) >= 2:
                break
            
            # 현재 칸이 바로 전의 칸보다 큰 경우
            elif arr[i][j] - now == 1:
                can = True
                for k in range(L):
                    if j-1-k < 0:   # 범위를 벗어나면
                        can = False
                        break
                    # 뒤의 조건은 내가 뒤로 가면서 체크하는데 경사로가 이미 놓아져 있으면 멈춘다.
                    if arr[i][j-1-k] != now or visited[j-1-k]:
                        can = False
                        break
                    
                # 만약 길이 안되면 다음 탐색으로 넘어간다.
                if not can:
                    break
                
            # 현재 칸이 바로 전의 칸보다 작은 경우
            elif now - arr[i][j] == 1:
                can = True
                for k in range(L):
                    if j+k >= N:
                        can = False
                        break
                    if arr[i][j+k] != arr[i][j]:
                        can = False
                        break
                    # 앞으로 체크하면서 가는 경우는 경사로 놓는 것을 체크하면서 간다.
                    visited[j+k] = 1
                if not can:
                    break
        else:
            count += 1 
            
    return count

temp1 = f(arr1)
arr2 = change_arr(arr1)
temp2 = f(arr2)
print(temp1+temp2)
