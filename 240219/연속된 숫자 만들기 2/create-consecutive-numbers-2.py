a, b, c = tuple(map(int, input().split()))


if abs(a-b) == 1 and abs(b-c) == 1:
    print(0)
else:
    if abs(a-b) == 2 or abs(b-c) == 2:
        print(1)
    else:
        print(2)