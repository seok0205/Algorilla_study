import sys
def av1():
    return round(sum(arr)/N)

def av2(): 
    return arr[N//2]

def av3():
    count = 0
    max_len = 0
    for i in range(N-1):
        temp = 0
        t = 0
        while True:
            if arr[i+t] != arr[i+t+1]:
                break
            temp += 1
            t += 1
            if temp > max_len:
                max_len = temp
                count = arr[i]
            
    return count
    
def av4():
    return arr[-1] - arr[0]

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)
arr.sort()

print(av1())
print(av2())
print(av3())
print(av4())

# 다시 풀기
