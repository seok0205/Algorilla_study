# 유클리드 호제법
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a, b = map(int, input().split())

result1 = gcd(a, b)
result2 = result1 * (a//result1) * (b // result1)
print(result1)
print(result2)
