n = int(input())

def find_nth(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (find_nth(n-1) * find_nth(n-2))%100
    
print(find_nth(n))