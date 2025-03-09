a, b, v = map(int, input().split())

count = 0
c = a - b
result = (v-b) // c if (v-b) % c == 0 else (v-b) // c + 1
print(result)