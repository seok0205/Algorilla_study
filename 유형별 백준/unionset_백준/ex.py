import sys
input = sys.stdin.readline
# sys.stdin = open("graph.txt", "r")

#union_find
# 크루스칼
def find_set(x):
    #경로압축
    if x != par[x]: #부모가 다르면
        par[x] = find_set(par[x])
    return par[x]

def union(a,b): 
    ref_a = find_set(a) #대표자 저장
    ref_b = find_set(b)

    if ref_a == ref_b: #사이클 방지
        return
    
    #연결 규칙 : 작은 쪽 부모를 큰쪽으로
    if ref_a < ref_b:
        par[ref_a] = ref_b
    else:
        par[ref_b] = ref_a

V,E = map(int, input().split()) #정점수V 간선수E
edge = [] #간선 저장

for i in range(E):
    A,B,C = map(int, input().split()) 
    #간선정보_정점AB 가중치C
    edge.append((C,A,B)) #가중치 기준으로 튜플 저장

par = [i for i in range(V+1)] #부모 저장_재귀형식

edge.sort(key= lambda x : x[0]) # 가중치 기준 오름차순

cnt = 0     # 현재까지 선택한 간선의 수
result = 0  # MST 가중치의 합

for c,a,b in edge:
    if find_set(a) == find_set(b): #두 정점이 다른 집합에 있으면면
        continue
    else:
        union(a, b)
        result += c #가중치 합산
        cnt += 1 #간선수 증가

    if cnt == V - 1:  # 모든 정점이 연결되면 종료
        break

print(result)
