n = int(input())
base = list(input().split())
# cnt = 0
# for i in range(n-1):
#     if arr[i] > arr[i+1]:
#         temp = arr[i]
#         arr[i] = arr[i+1]
#         arr[i+1] = temp
#         cnt += 1
#     for j in range(1, n):
#         if arr[j-1] > arr[j]:
#             temp = arr[j]
#             arr[j] = arr[j-1]
#             arr[j-1] = temp
#             cnt += 1
# print(arr, cnt)
cnt = 0

#삽입정렬 알고리즘이 효율적일 것
for i in range(1, n): #범위 증가
    for j in range(i, 0, -1): #범위 체크, i~1까지
        if ord(base[j-1]) > ord(base[j]): #작은 게 앞으로
            base[j-1], base[j] = base[j], base[j-1]
            cnt += 1
        else:
            break
# print(base)
print(cnt)