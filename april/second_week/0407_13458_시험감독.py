'''
필요한 감독관 수의 최솟값 구하기
'''

N = int(input())
people_lst = list(map(int, input().split()))
main_available, sub_available = map(int, input().split())
total = 0

for i in range(N):
    if people_lst[i] - main_available >= 0:
        total += 1
        people_lst[i] -= main_available
    else:
        total += 1
        people_lst[i] = 0

for i in range(N):
    necessary = people_lst[i] // sub_available if people_lst[i] % sub_available == 0 else people_lst[i] // sub_available + 1
    total += necessary

print(total)
