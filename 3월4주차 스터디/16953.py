import sys
a, b = map(int, sys.stdin.readline().split())

def recur(a, cnt):
    global count

    if a == b:
        count = min(cnt, count)
        return
    
    if a > b:
        return
    
    recur(a*2, cnt+1)
    recur(a*10+1, cnt+1)        

    return -1


count = 1e8
recur(a, 0)
if count == 1e8:
    print(-1)
else:
    print(count+1)