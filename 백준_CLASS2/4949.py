dic = {')' : '(', ']' : '['}
def check():
        stack = []
        for word in arr:
            if word in ['(', '[']:
                stack.append(word)
                
            elif word in [')', ']']:
                if not stack or dic[word] != stack.pop():
                    return 'no'

            elif word == '.':
                if stack:
                    return 'no'
  
        return 'yes'
# 소괄호, 대괄호 2종류만 존재
while True:
    arr = list(input())
    if arr == ['.']:
        break
    a = check()
    print(a)