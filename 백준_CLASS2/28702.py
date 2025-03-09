arr = []
for _ in range(3):
    arr.append(input().rstrip())

idx, temp = 0, 0
result = 0
for i in range(3):
    if arr[i] not in ['Fizz', 'Buzz', 'FizzBuzz']:
        temp = int(arr[i])
        idx = i
        break
    
result = temp + (3-idx)

if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)