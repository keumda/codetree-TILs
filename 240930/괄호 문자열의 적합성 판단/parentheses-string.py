s = input()
stack = []
isValid = True
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if len(stack) == 0:
            isValid = False
            break
        stack.pop()
if len(stack) > 0:
    isValid = False
if isValid:
    print('Yes')
else:
    print('No')