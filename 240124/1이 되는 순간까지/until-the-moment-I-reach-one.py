n = int(input())

def find_cnt(n, cnt):
    if n == 1:
        return cnt
    if n%2 == 0:
        return find_cnt(n//2, cnt+1)
    else:
        return find_cnt(n//3, cnt+1)

print(find_cnt(n, 0))