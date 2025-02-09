def bus_routes():
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())  # 버스 노선 수
        count = [
            0
        ] * 5001  # 각 정류장이 몇 개의 버스 노선에 포함되는지 저장하는 배열 (1부터 5000까지, 0번은 사용 안함)

        # 각 버스 노선에 대해
        for _ in range(N):
            A, B = map(int, input().split())  # 버스 노선의 구간 (Ai ~ Bi)
            for i in range(A, B + 1):  # Ai부터 Bi까지 모든 정류장 번호에 대해
                count[i] += 1  # 해당 정류장에 이 버스 노선이 다닌다고 카운트

        P = int(input())  # 요청된 정류장 수
        result = []  # 결과를 저장할 리스트

        # 각 요청된 정류장에 대해
        for _ in range(P):
            C = int(input())  # 요청된 정류장 번호
            result.append(str(count[C]))  # 해당 정류장에 다니는 버스 노선의 개수

        # 출력 형식에 맞게 결과 출력
        print(f"#{t} {' '.join(result)}")


# 문제를 푸는 함수 호출
bus_routes()
