s = input()
stack = []
isValid = True
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) < 1:
            isValid = False
            break
        else:
            pair = stack.pop()
            if pair != ')':
                isValid = False
                break
if len(stack) > 0:
    isValid = False
if isValid:
    print('Yes')
else:
    print('No')