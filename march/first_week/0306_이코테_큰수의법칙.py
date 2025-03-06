'''
5 8 3
2 4 5 4 6

4 7 2
3 4 3 4 3
'''

# 청크의 길이가 M보다 작을 때를 생각 못하고 막 더했음..

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
# 특정 인덱스의 수를 연속해서 K번 반복 가능 총 M번 더함
sorted_arr = sorted(arr)
first_big = sorted_arr[N-1]
second_big = sorted_arr[N-2]
count = 0
answer = 0

print(answer)