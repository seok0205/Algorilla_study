N = int(input())
a = N
nums = list(map(int,input().split()))
for num in nums:
    if num == 1:
        a-= 1
        
    else:
        for i in range(2, num):
            if num%i == 0:
                a -= 1
                break
print(a) 