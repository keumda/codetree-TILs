n = int(input())

s = 0
for i in range(n):
    s += int(input())

s_str = str(s)
print(s_str[1:]+s_str[:1])