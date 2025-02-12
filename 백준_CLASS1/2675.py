T = int(input())
for t in range(T):
    n, word = input().split()
    N = int(n)
    new_word = ''
    for i in range(len(word)):
        new_word += word[i]*N
    print(new_word)
