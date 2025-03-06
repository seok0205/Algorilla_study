infix = input()
postfix = ''
stack = []
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
for token in infix:
    if token == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break
            postfix += stack.pop()
    elif token in '+-*/(':
        while stack and isp[stack[-1]] >= icp[token]:
            postfix += stack.pop()
        stack.append(token)
    else:
        postfix += token
while stack:
    postfix += stack.pop()
print(postfix)