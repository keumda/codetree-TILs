k, n = map(int, input().split())
res = []

def print_res():
    for d in res:
        print(d, end=" ")
    print()

def choose(curr):
    if curr == n + 1:
        print_res()
        return
    else:
        for j in range(1, k+1):
            res.append(j)
            choose(curr + 1)
            res.pop()
        return

choose(1)