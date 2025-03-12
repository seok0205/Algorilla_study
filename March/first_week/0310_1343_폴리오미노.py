P = input()
answer = ''
i = 0
while i < len(P):
    if P[i:i+4] == 'XXXX':
        answer += 'AAAA'
        i += 4
    elif P[i] == '.':
        answer += '.'
        i += 1
    elif P[i:i+2] == 'XX':
        answer += 'BB'
        i += 2
    else:
        answer = -1
        break
print(answer)
