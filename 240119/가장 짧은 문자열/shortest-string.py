min_size = 20
max_size = 0

for _ in range(3):
    curr_str = input()
    if len(curr_str) < min_size:
        min_size = len(curr_str)
    if len(curr_str) > max_size:
        max_size = len(curr_str)

print(max_size - min_size)