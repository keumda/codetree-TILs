n = int(input())
arr = list(map(int, input().split()))

def find_max(n):
    if n == 0:
        return arr[n]
    return max(find_max(n-1), arr[n-1])

print(find_max(n))