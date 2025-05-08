'''
K 세대 드래곤 커브는 K-1 세대 드래곤 커브를 끝 점 기준으로 90도 시계 방향 회전시킨 다음
그것을 끝 점에 붙인 것이다.
100 x 100인 격자 위에 드래곤 커브가 N개 있다.
이때, 크기가 1 x 1인 정사각형의 네 꼭짓점(변이 아닌것에 주의)이 모두 드래곤 커브의 일부인
정사각형의 개수를 구해라
'''
import sys
input = sys.stdin.readline
'''그럼 우선 주어진 정보의 드래곤 커브들을 보두 맵에 놓자
근데 어떻게 놓을거임?
모든 칸들에 방향마다 [0, 0, 0, 0]과 같이 배열을 부여해서
3개 이상 들어가면 counting
세대별로 2의 제곱승으로 선의 길이가 늘어남

1. 위로 가는거에서 왼쪽으로 가는거
2. 왼쪽 -> 아래
3. 위 -> 왼
4. 오 -> 위
다음 세대로 넘어가면 역순으로 방향을 +1해서 이동하네?
그러면 세대별로 stack에 쌓으면서 pop을 해주면서 이동하면 되겠는데?
그러고 다음걸 새로운 스택에 넣어야됨
경로만 있으면 된다 -> 그러면 드래곤 커브들을 전부 찍어두고
꼭짓점이 아닌 칸들을 순회하면서 칸을 돌때마다 4가지 꼭짓점을 모두 체크
모든 꼭짓점에서 커브가 지나간 흔적이 있으면 count
'''
# 우상좌하
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
# 드래곤 커브의 개수
N = int(input())
# 드래곤 커브의 정보
# x, y : 시작점, d : 방향, g : 세대
# 0~3 : 오른쪽에서 시작해서 반시계방향
arr = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr.append([x, y, d, g])
    
dragon = [[0] * 101 for _ in range(101)]
# 여기부터는 드래곤 커브의 경로 찍기
def dragoncurve(x, y, d, g):
    # 모든 경로를 찍어두자!
    # 0세대인 경우 1가지로 끝
    way = [d]
    
    # 세대별로 역순으로 방향을 +1해서 저장하면 됨
    for i in range(g):
        for j in range(len(way)-1, -1, -1):
            way.append((way[j]+1) %4)

    dragon[y][x] = 1
    # 모아둔 경로들로 dragon좌표 찍기
    for w in way:
        x += dr[w]
        y += dc[w]
        dragon[y][x] = 1

for x, y, d, g in arr:
    dragoncurve(x, y, d, g)

result = 0
# 칸들의 기준으로 4방향의 꼭짓점이 모두 체크되어 있어야함
for i in range(100):
    for j in range(100):
        if dragon[i][j] and dragon[i][j+1] and dragon[i+1][j] and dragon[i+1][j+1]:
            result += 1
            
print(result)
    
        