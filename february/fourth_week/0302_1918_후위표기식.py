# infix = input()
# postfix = ''
# stack = []
# icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
# isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
# for token in infix:
#     if token == ')':
#         while stack:
#             if stack[-1] == '(':
#                 stack.pop()
#                 break
#             postfix += stack.pop()
#     elif token in '+-*/(':
#         while stack and isp[stack[-1]] >= icp[token]:
#             postfix += stack.pop()
#         stack.append(token)
#     else:
#         postfix += token
# while stack:
#     postfix += stack.pop()
# print(postfix)


icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
stack = []
infix = input()
postfix = ''
for token in infix:
    if token.isnumeric():
        postfix += token
    elif token == ')':
        while stack:
            op = stack.pop()
            if op == '(':
                break
            else:
                postfix += op
    else:
        while stack and icp[token] <= isp[stack[-1]]:
            postfix += stack.pop()
        stack.append(token)

while stack:
    postfix += stack.pop()

print(postfix)


output = []
for token in postfix:
    if token.isnumeric():
        output.append(int(token))
    elif token in '+-*/':
        if len(stack) < 2:
            print("error")
            break
        right = output.pop()
        left = output.pop()
        if token == '+':
            output.append(left + right)
        elif token == '-':
            output.append(left - right)
        elif token == '*':
            output.append(left * right)
        elif token == '/':
            if right == 0:
                print("error")
                break
            else:
                output.append(left // right)

result = output.pop()
if output:
    print("error")
else:
    print(result)