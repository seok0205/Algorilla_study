while True:
    N = input()
    if N == '0':
        break
    else:
        n = len(N)
        result = 'yes'
        for i in range(n//2):
            if N[i] != N[n-i-1]:
                result = 'no'
        print(result)