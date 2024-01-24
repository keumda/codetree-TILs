a, b, c = list(map(int, input().split()))

def find_digit_sum(n):
    if n < 10:
        return n
    return n%10 + find_digit_sum(n//10)

print(find_digit_sum(a*b*c))