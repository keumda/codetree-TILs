n = int(input())

def multiply_digit(n):
    if n < 10:
        return n**2
    return (n%10)**2 + multiply_digit(n//10)


print(multiply_digit(n))