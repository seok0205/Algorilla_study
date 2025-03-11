from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
 

def shoot(cnt, remains, now_arr):
    global min_blocks
    global check
    check += 1
    if cnt == N or remains == 0:  # 구슬을 모두 발사 or 남은 벽돌이 0이면
        # 최소값 갱신 후 종료
        min_blocks = min(min_blocks, remains)
        return
 
    # 한 줄 씩 떨구자
    for col in range(W):
        # 방법1 (원본을 복사해두고, 다시 되돌리는 방법)
        # 1. col 위치에 떨구기 전 상태를 복사 (얕은 복사 주의)
        # 2. 원본 리스트의 col 위치에 떨구기
        # 3. cnt+1 번 상태로 이동 (다음 재귀 호출)
        # 4. 떨구기 전 상태로 복구
         
        # 방법2 (복구 시간이 없으니 더 효율적이다!)
        # 1. col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트에 col 위치에 떨구기
        # 3. cnt+1 번 상태로 이동 + col 위치에 떨군 상태를 함께 전달
        copy_arr = [row[:] for row in now_arr]
         
        # col 위치에 구슬 떨어뜨리기
        # 구슬을 쏘는 열에서 가장 위를 찾기
        row = -1
        for r in range(H):
            if copy_arr[r][col]:  # 벽돌이 있으면
                row = r
                break
         
        if row == -1:  # 벽돌이 없는 열이면 다음 열 확인하기
            continue
 
        # 깨질 벽돌들을 리스트에 담아야함
        # 행, 열, 숫자
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1   # 남은 벽돌들을 계산할 변수
        copy_arr[row][col] = 0      # 구슬이 처음 만나는 벽돌 자리
 
        # 주변 벽돌들이 깨짐
        while q:
            r, c, p = q.popleft()
            for k in range(1, p):  # 숫자 만큼 반복하면서 벽돌들이 깨짐
                for i in range(4):
                    ny = r + (dy[i] * k)
                    nx = c + (dx[i] * k)
 
                    if ny < 0 or ny >= H or nx < 0 or nx >= W:  # 범위 계산
                        continue
 
                    if copy_arr[ny][nx] == 0:
                        continue
 
                    q.append((ny, nx, copy_arr[ny][nx]))    # 다음 벽돌 추가
                    copy_arr[ny][nx] = 0                    # 벽돌 깨짐
                    now_remains -= 1                        # 숫자 감소
 
        # 빈칸을 메꿔주어야 한다
        for c in range(W):
            idx = H - 1  # 벽돌이 위치할 index
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1
 
        shoot(cnt + 1, now_remains, copy_arr)
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
 
    # 1. 최소 벽돌
    # 2. 현재 벽돌이 다 깨지면 더 이상 할 필요 없음. -> 현재 벽돌 수를 관리하자.
    # 3. N 번 굴리면 끝난다.
    #  - 0번부터 시작, N번 까지 반복
    #  - 무조건 모두 굴려보아야 정답이 나온다. (DFS)
    #  - 한 번 굴렸을 때 벽돌들이 연쇄로 깨진다
    #    - 현재 기준으로 퍼져나가면서 탐색한다 (BFS)
 
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el:
                blocks += 1
    check = 0
    shoot(0, blocks, arr)
 
    print(f'#{tc} {min_blocks}')

    print(check)
