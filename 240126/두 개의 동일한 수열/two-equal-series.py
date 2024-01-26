n = int(input())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

a_seq.sort()
b_seq.sort()

flag_string = 'Yes'
for i in range(n):
    if a_seq[i] != b_seq[i]:
        flag_string = 'No'
print(flag_string)