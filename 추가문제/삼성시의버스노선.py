T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 버스 노선 번호 범위 A, B  
    P = int(input())    # 버스 정류장 개수
    C = [int(input()) for _ in range(P)]    # 버스 정류장 번호

    result = []

    for i in range(P):
        cnt = 0     # c 정류장을 다니는 버스 노선 개수

        for j in arr:
            A, B = j    # j = [A,B] -> 리스트 언패킹
            if A <= C[i] <= B:  # c 정류장이 A와 B 사이일 때
                cnt += 1    # 버스 노선 개수 +1
    
        result.append(str(cnt)) # 출력을 위해 문자열로 변경

    print(f'#{test_case} {" ".join(result)}')