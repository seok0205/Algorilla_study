# 왜 try-except(EOFError)를 해야 하는지는 모르겠다.
# 요즘 어려운 문제를 풀어서 그런지 정답코드를 보고 따라치는 느낌이 많이 드는데 그게 도움이 될까? 못 풀면 그냥 넘겨?

while True:
    try:
        n = int(input())
        str = '1'
        while True:
            if int(str) % n == 0:
                print(len(str))
                break
            else:
                str += '1'
    except EOFError:
        break