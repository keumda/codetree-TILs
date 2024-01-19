cur_str = input()

res = ''
for i, a in enumerate(cur_str):
    if (i+1) % 2 == 0:
        res += a

print(res[::-1])