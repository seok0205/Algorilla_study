'''
N개의 양의 정수가 주어짐. 최댓값 위치, 취솟값 위치 차이를 절대값을로 출력
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    min_num = a[0]  # 최솟, 최댓값 저장
    max_num = a[0]
    min_index = 0   # 최솟, 최댓값 있는 인덱스 저장
    max_index = 0

    for i in range(N):
        if a[i] < min_num:  # 최솟값과 인덱스 같이 저장 =가 없어 맨 처음 등장한 최솟값이 쭉 저장
            min_index = i
            min_num = a[i]
        if a[i] >= max_num: # 최댓값과 인덱스 같이 저장 =가 없어 맨 마지막 등장한 최댓값이 쭉 저장
            max_index = i
            max_num = a[i]

    result = abs(max_index - min_index) # 차를 구하고, 절댓값 변환

    print(f'#{tc} {result}')