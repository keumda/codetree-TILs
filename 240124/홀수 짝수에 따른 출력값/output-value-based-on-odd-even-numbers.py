n = int(input())

def find_sum(n):
    if n%2 == 1:
        if n == 1:
            return 1
    else:
        if n == 2:
            return 2
    return n + find_sum(n-2)

print(find_sum(n))