input_str = input()
sub_str = input()

def find_idx(input_str, sub_str):
    s_len = len(sub_str)
    for i in range(0, len(input_str)-s_len+1):
        if input_str[i:i+s_len] == sub_str:
            return i
    return -1

print(find_idx(input_str, sub_str))