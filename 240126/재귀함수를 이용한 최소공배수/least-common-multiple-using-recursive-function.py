n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(n, idx, prev):
    if n <= 1:
        return arr[n-1]
    if idx == n:
        return prev
    a, b = prev, arr[idx]
    curr_lcm = a * b // gcd(a, b)
    prev = curr_lcm
    idx += 1
    return lcm(n, idx, prev)

print(lcm(n, 1, arr[0]))