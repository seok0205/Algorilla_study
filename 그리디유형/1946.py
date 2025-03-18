# 각각의 다른 사람들보다 적어도 1개이상 좋아야됨
# 선발가능한 최대 인원의 수
T = int(input())
for t in range(T):
    # 지원자의 수
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]


    # 서류점수를 기준으로 정렬
    arr.sort()
    
    count = 0
    max_interview = float('inf')
    # 서류점수가 낮은 기준으로 정렬을 했기 때문에
    # 낮은 사람부터 앞에서 체크하다가
    # 그 사람보다 둘 다 큰 사람이 나오면 배제한다.
    # 이미 뒤에 사람들은 앞에 사람보다 최소 1개는 큰 상태이기 때문에
    # 뒤의 사람들은 상관이 없지만 앞에 이미 합격한 사람이 포함되지 못함
    for doc, interview in arr:
        if interview <= max_interview:
            max_interview = interview
            count += 1

    print(count)