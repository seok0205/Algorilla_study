'''
G4 14500 테트로미노

폴리오미노는 크기가 1x1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음 조건을 만족.
1. 정사각형은 서로 겹치면 안됨
2. 도형은 모두 연결되어 있어야 함
3. 정사각형의 변끼리 연결되어 있어야 함. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안됨

정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 함.

NxM인 종이 위에 테트로미노 하나를 놓으려고 하고, 종이는 1x1 크기의 칸으로 나누어져 있고, 각각의 칸에 정수가 쓰여 있음.
테트로미노를 하나 놓았을 때, 놓인 칸에 쓰인 수들의 합이 최대로 되야 함.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 됨.

입력:
N, M : 세로, 가로
종이에 쓰여진 숫자들 배열 형태로 주어짐

출력:
테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

# import heapq                  # 처음에 최대 힙 구현. 반례 모두 통과하지만 시간 초과 발생. 힙 정렬을 지속하다 보니 누적되어 많은 시간이 걸림.

# def search(x, y):
#     global result
    
#     heap = []
#     visit = [[0] * M for _ in range(N)]
#     heapq.heappush(heap, (-paper[x][y], x, y, 1))
#     visit[x][y] = paper[x][y]
    
#     while heap:                       # 최대 힙
#         num_sum, target_x, target_y, cnt = heapq.heappop(heap)        # 첫 좌표 힙팝
        
#         if cnt == 1 and result - 3000 > -num_sum:             # 혼신의 가지치기
#             continue
        
#         if cnt == 2 and result - 2000 > -num_sum:
#             continue
        
#         if cnt == 3 and result - 1000 > -num_sum:
#             continue

#         if cnt == 4:                                  # 4칸 찾으면 최댓값 비교
#             result = max(result, -num_sum)
#             continue
            
#         if cnt >= 5:                  # 5번째 값이 올라오면 넘김. 최대 4칸까지만 찾아야함
#             continue
        
#         for k in range(4):
#             next_x = target_x + di[k]
#             next_y = target_y + dj[k]
            
#             if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
#                 continue
            
#             new_sum = -num_sum + paper[next_x][next_y]        # 새로운값 얻고
            
#             if visit[next_x][next_y] == 1:            # 최댓값 저장 안되었다면
#                 continue
            
#             visit[next_x][next_y] = 1             # 최대값 넣고 힙푸쉬
#             heapq.heappush(heap, (-new_sum, next_x, next_y, cnt+1))


di = [0, 1, 0, -1]      # ㅜ 모양 블록에 쓸 델타
dj = [1, 0, -1, 0]


def sad(x, y):
    global result
    
    num_lst = [paper[x][y]]     # 중앙 좌표 리스트에 넣어줌. 항상 들어가는 값.
    
    for k in range(4):      # 한 좌표 중심으로 4방향의 값을 한 리스트에 넣음.
        a = x + di[k]
        b = y + dj[k]
        
        if a < 0 or a >= N or b < 0 or b >= M:      # 범위 벗어나면 0 추가
            num_lst.append(0)
            continue
        
        num_lst.append(paper[a][b])     # 범위 내면 종이에 적힌 값 추가
    
    if sum(num_lst) < result:       # 리스트 전체 합이 이미 구한 최댓값보다 작으면 함수 종료
        return
    
    for i in range(1, 5):           # 인덱스 1부터 4까지 담긴 값들은 한번씩 ㅜ 블록에 포함되지 않음. ㅗ, ㅏ, ㅓ, ㅜ 이므로 중앙 좌표 빼고 나머지 좌표는 모두 한번씩 빠질때가 있음. 
        sub_sum = num_lst[0]        # 몯든 조합에는 중앙 값. num_lst[0] 값은 들어감!
        for j in range(1, 5):
            if i != j:
                sub_sum += num_lst[j]       # 합 누적 후, result와 값 비교
        result = max(result, sub_sum)


def search(a, b, cnt, total):       # 나머지 블록들 찾는 함수. ㅜ 모양 빼고는 dfs를 활용해서 구할 수 있음.쭉 이어가며 탐색할수 있기 때문!
    global result
    
    if cnt == 4:                    # 4칸 찾으면 결과 비교후 종료
        result = max(result, total)
        return
    
    for k in range(4):      # 4방향 탐색
        x = a + di[k]
        y = b + dj[k]
        
        if x < 0 or x >= N or y < 0 or y >= M:      # 범위 이탈 시 다음칸 탐색
            continue
        
        if visit[x][y]:     # 이미 방문한 곳이면 넘어감
            continue
        
        visit[x][y] = 1     # 방문 표시
        search(x, y, cnt + 1, total + paper[x][y])      # 방문한 상태에서 탐색
        visit[x][y] = 0     # 방문한 상태에서 함수 실행했으니, 방문 표시 풀기(다른 칸들의 탐색을 위해서!)

            
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        visit[i][j] = 1     # 첫칸은 무조건 포함되므로 고정으로 1로 만들어주고,
        search(i, j, 1, paper[i][j])        # 블록들을 탐색한 뒤,
        sad(i, j)
        visit[i][j] = 0     # 고정 값 풀기

print(result)