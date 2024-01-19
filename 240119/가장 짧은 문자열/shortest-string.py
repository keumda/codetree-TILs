min_size = 20

for _ in range(3):
    curr_str = input()
    if len(curr_str) < min_size:
        min_size = len(curr_str)

print(min_size)