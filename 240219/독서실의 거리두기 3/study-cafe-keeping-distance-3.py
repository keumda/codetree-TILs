n = int(input())
str = input()

min_space = n
max_space = 0
end_idx = 0
cnt = 0
for i, s in enumerate(str[1:]):
    if s == '1':
        min_space = min(min_space, cnt)
        max_space = max(max_space, cnt)
        end_idx = i - 1
        cnt = 0
    else:
        cnt += 1
print(min(min_space+1, max_space//2+1))
# print(end_idx, min_space, max_space)