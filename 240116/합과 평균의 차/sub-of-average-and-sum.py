arr = list(map(int, input().split()))

s = sum(arr)
av = s / len(arr)
sub = s - av

print(s)
print(int(av))
print(int(sub))