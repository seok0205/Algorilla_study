'''
D1 22375 스위치 조작

N개의 전등 설치. 각 전등은 1부터 N까지 번호가 있음
i번 스위치 조작 시 i번부터 N번까지의 전등의 켜짐/꺼짐 상태가 반대가 된다고 함
모든 전등의 현재 상태와 스위치 조작 후 상태가 주어지면 최소 몇 개의 스위치를 조작해야 하는지 구하는 문제

입력:
첫 줄 테스트케이스 개수
두번째 줄 스위치 개수 N
세번째, 네번째 줄 조작 전 스위치 상태, 후 상태 N개씩 주어짐
'''


def on_off(lst, idx):       # 스위치 조작 함수
    for i in range(idx, len(lst)):      # 스위치 누른 인덱스부터 끝까지
        if lst[i]:      # 1이면 0, 0이면 1로 변경
            lst[i] = 0
        else:
            lst[i] = 1
    return lst


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))
    result = 0

    for i in range(N):
        if before[i] != after[i]:       # 만약 같은 인덱스 자리가 다르면
            result += 1
            before = on_off(before, i)  # 스위치 누름

    print(f'#{tc} {result}')