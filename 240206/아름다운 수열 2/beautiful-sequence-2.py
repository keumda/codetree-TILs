n, m = tuple(map(int, input().split()))
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))
b_seq.sort()

cnt = 0
for i in range(n-m+1):
    a_arr = a_seq[i:i+m]
    a_arr.sort()
    if a_arr == b_seq:
        cnt += 1
print(cnt)