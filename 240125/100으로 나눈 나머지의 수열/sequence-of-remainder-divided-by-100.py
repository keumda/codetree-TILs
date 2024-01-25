n = int(input())

def find_nth(first, second, n, cnt):
    if n == 1:
        return 2
    if n == 2:
        return 4
    curr = first * second % 100
    first = second
    second = curr
    if cnt == n:
        return curr
    else:
        return find_nth(first, second, n, cnt+1)
    
print(find_nth(2, 4, n, 3))