n = input()

def convert_binary(num):
    coverted = 0
    for i in num:
        coverted = (coverted * 2) + int(i)
    return coverted

max_num = '0'
for i in range(1, len(n)):
    changed_n = list(n)
    changed_n[i] = str(abs(int(n[i]) - 1))
    changed_n = ''.join(changed_n)
    if convert_binary(changed_n) > convert_binary(max_num):
        max_num = changed_n
print(convert_binary(max_num))