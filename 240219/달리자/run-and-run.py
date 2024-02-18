n = int(input())
st_arr = list(map(int, input().split()))
end_arr = list(map(int, input().split()))

res = 0
for i in range(n):
    if st_arr[i] > end_arr[i]:
        num = st_arr[i] - end_arr[i]
        st_arr[i] -= num
        st_arr[i+1] += num
        res += num
print(res)