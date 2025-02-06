'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면 그 수를 한수라 함.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말함.
N이 주어질 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하라.
'''

N = input()

if int(N) < 100:
    result = int(N)
else:    
    result = 99
    for i in range(100, int(N)+1):
        num = list(str(i))
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            result += 1

print(result)