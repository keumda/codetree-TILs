cur_str = input()
first_char = cur_str[0]
second_char = cur_str[1]

for i, c in enumerate(cur_str):
    if c == second_char:
        cur_str = cur_str[:i] + first_char + cur_str[i+1:]

print(cur_str)