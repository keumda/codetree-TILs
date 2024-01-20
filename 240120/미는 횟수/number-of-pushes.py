a = input()
b = input()

min_step = -1
for i in range(1, len(a)):
    temp_a = a[-i:] + a[:len(a)-i]
    if temp_a == b:
        min_step = i
        break

print(min_step)