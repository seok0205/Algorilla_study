'''
D2 1959 두 개의 숫자열

N개의 숫자로 구성된 숫자열 A와 M개의 숫자로 구성된 숫자열 B
A, B를 자유롭게 움직여 숫자들이 마주보는 위치 변경 가능
단, 더 긴 쪽의 양끝을 벗어나선 안됨
마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값 구하는 문제

제약:
N, M은 3이상 20이하
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if len(A) < len(B):                 # 길이가 더 긴 리스트, 짧은 리스트 구분
        short_lst, long_lst = A, B
    else:
        short_lst, long_lst = B, A
    
    max_sum = 0     # 최댓값 담을 변수 초기화
    
    for i in range(len(long_lst) - len(short_lst) + 1):     # 긴 리스트의 길이에서 짧은 리스트의 길이를 빼고 1을 더하면
        cur_sum = 0                                         # 배열 끝끼리 벗어나지 않는 선에서 마주보는 전체 경우의 수 구함
        for j in range(len(short_lst)):     # 짧은 리스트의 길이가 곱할 횟수
            cur_sum += short_lst[j] * long_lst[j+i]     # 경우의 수 하나 일때 곱의 합 누적
        if max_sum < cur_sum:       # 최댓값 유지 및 교체
            max_sum = cur_sum
    
    print(f'#{tc} {max_sum}')