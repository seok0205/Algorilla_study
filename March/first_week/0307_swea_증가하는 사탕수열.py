'''
각 상자가
1. 비어있지 않고
2. 순증가하게 (1 < 2 < 3)
하기 위해 최소 몇 개의 사탕을 먹어야 하는지 구하기
조건 만족 못할 경우 -1 출력

먼저 조건이 이미 부합할 수도 있으니까 그것 확인 후 아니라면
마지막에서 두 번째 것 부터 조건이 맞을 때 까지 (= 마지막 값보다 작을 때까지) 1 빼고 조건 맞는지 확인하고
그 다음으로 가서 조건이 맞을 때까지 빼고 조건 맞는지 확인하고

4
3 2 1
1 2 3
3 5 5
5 6 6

'''

def is_ascending(num1, num2):
    return num2 > num1

def is_more_than_zero(A, B, C):
    return A > 0 and B > 0 and C > 0

T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())
    answer = 0
    if not is_more_than_zero(A, B, C):
        answer = -1
    else:
        if A < B < C:
            answer = 0
        else:
            while not is_ascending(B, C):
                B -= 1
                if B <= 0:
                    answer = -1
                    break
                answer += 1
            while not is_ascending(A, B):
                A -= 1
                if A <= 0:
                    answer = -1
                    break
                answer += 1

    print(f"#{t} {answer}")