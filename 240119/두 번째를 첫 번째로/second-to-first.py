cur_str = input()
first_char = cur_str[0]
second_char = cur_str[1]
str_arr = list(cur_str)

for i, c in enumerate(str_arr):
    if c == second_char:
        str_arr[i] = first_char

result_string = ''.join(str_arr)
print(result_string)