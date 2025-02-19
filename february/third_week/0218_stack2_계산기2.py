
for t in range(1, 11):
    N = int(input())
    expression = input()
    operator_stack = []
    priority = {"+": 1, "*": 2}
    postfix = ""
    for token in expression:
        if token.isnumeric():
            postfix += token
        else:
            while operator_stack and priority[operator_stack[-1]] >= priority[token]:
                postfix += operator_stack.pop()
            operator_stack.append(token)

    while operator_stack:
        postfix += operator_stack.pop()

    output_stack = []
    for token in postfix:
        if token.isnumeric():
            output_stack.append(int(token))
        else:
            right = output_stack.pop()
            left = output_stack.pop()
            if token == "+":
                output_stack.append(left+right)
            elif token == "*":
                output_stack.append(left*right)

    print(f"#{t}", *output_stack)