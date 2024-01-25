n = int(input())

def seq(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return seq(n//3) + seq(n-1)

print(seq(n))