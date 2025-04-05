import sys
input = sys.stdin.readline
# 한 번 입은 옷조합은 절대 다시 입지 않음
T = int(input())
for t in range(T):
    n = int(input())
    cloth_dic = {}
    for _ in range(n):
        cloth, kind = list(input().split())
        if kind in cloth_dic.keys():
            cloth_dic[kind].append(cloth)
        else:
            cloth_dic[kind] = [cloth]
    
    keys = list(cloth_dic.keys())
    values = list(cloth_dic.values())
    result = 0
    for i in range(len(keys)):
        result += len(values[i]) * len(keys)
        print(values[i])
    print(result)