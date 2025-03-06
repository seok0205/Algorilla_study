

brackets = input()
stack = []
calc = []
answer = 1
for token in brackets:
    if token in '([':
        stack.append(token)

    elif token in ')]':
        if not stack:
            answer = 0
            break
        if all(isinstance(x, int) for x in stack):
            answer = 0
            break

        while stack:
            if stack and stack[-1] == '(' and token == ')':
                stack.pop()
                if calc:
                    stack.append(sum(calc) * 2)
                    calc.clear()
                else:
                    stack.append(2)
                break
            elif stack and stack[-1] == '[' and token == ']':
                stack.pop()
                if calc:
                    stack.append(sum(calc) * 3)
                    calc.clear()
                else:
                    stack.append(3)
                break
            elif stack and type(stack[-1]) is int:
                calc.append(stack.pop())

            elif stack and ((token == ')' and stack[-1] == '[') or (token == ']' and stack[-1] == '(')):
                answer = 0
                break

print(0 if answer == 0 or any(isinstance(x, str) and x in '([' for x in stack) else sum(stack))