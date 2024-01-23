a, o, c = tuple(input().split())

def add(a, b):
    print('{} + {} = {}'.format(a, b, a + b))
def subtract(a, b):
    print('{} - {} = {}'.format(a, b, a - b))
def multiply(a, b):
    print('{} * {} = {}'.format(a, b, a * b))
def divide(a, b):
    print('{} / {} = {}'.format(a, b, a // b))

if o == '+':
    add(int(a), int(c))
elif o == '-':
    subtract(int(a), int(c))
elif o == '*':
    multiply(int(a), int(c))
elif o == '/':
    divide(int(a), int(c))
else:
    print(False)