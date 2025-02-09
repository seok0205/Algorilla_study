'''
D3 6485 삼성시의 버스 노선

1에서 5000까지 번호가 있는 장소 존재. 이곳을 다니는 N개의 노선 존재.
i번째 노선은 번호가 A이상, B이하인 장소만 다니는 노선.
P개의 장소에 대해 각 장소에 몇 개의 노선이 다니는지 구하는 문제

입력:
N = 노선 갯수(정수)
Ai, Bi = N개의 줄만큼 노선의 출발 Ai, 도착점 Bi(정수)
P = 해당되는 노선 갯수 구할 장소의 개수(정수)
Cj = P개의 줄만큼 장소 Cj(정수)
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    route = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    place = [int(input()) for _ in range(P)]
    
    result = [0 for _ in range(len(place))]     # 장소마다 지나는 노선 갯수 저장할 결과값
    
    for i in range(len(place)):
        for j in range(len(route)):
            if place[i] in range(route[j][0], route[j][1]+1):   # 만약 해당 장소가 노선의 경로 중간에 있다면
                result[i] += 1      # 해당 장소의 result 값 1 증가
    
    for i in range(len(result)):    # 출력문
        if i == 0:
            print(f'#{tc} {result[i]}', end=' ')
        elif i == len(result) - 1:
            print(f'{result[i]}')
        else:
            print(f'{result[i]}', end=' ')
