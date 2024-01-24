n = int(input())

def print_seq(n):
    if n == 0:
        return
    print_seq(n-1)
    print(n, end=' ')

def print_reverse(n):
    if n == 0:
        return
    print(n, end=' ')
    print_reverse(n-1)

print_seq(n)
print()
print_reverse(n)