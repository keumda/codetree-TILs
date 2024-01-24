n = int(input())

def addup(n):
    if n == 1:
        return 1
    return addup(n-1) + n

print(addup(n))