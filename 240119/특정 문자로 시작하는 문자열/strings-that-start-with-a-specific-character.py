n = int(input())
arr = []
for i in range(n):
    curr_str = input()
    arr.append(curr_str)
s_alphabet = input()

s_sum = 0
s_alphabet_cnt = 0

for s in arr:
    if s[0] == s_alphabet:
        s_alphabet_cnt += 1
        s_sum += len(s)

# '{:.2f}'.format(round(2606.89579999999, 2))
print(s_alphabet_cnt, '{:.2f}'.format(round(s_sum/s_alphabet_cnt, 2)))