n = int(input())

def find_cnt(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        n = n//2
    else:
        n = n*3+1
    return find_cnt(n) + 1

print(find_cnt(n))