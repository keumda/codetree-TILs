a = input()
b = input()

a_int = ''
b_int = '' 
for c in a:
    if c.isdigit():
        a_int += c
for c in b:
    if c.isdigit():
        b_int += c

print(int(a_int)+int(b_int))