n = int(input())

def find_sum_divide(n):
    s = 0
    for i in range(n+1):
        s += i
    return s//10

print(find_sum_divide(n))