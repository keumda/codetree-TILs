n = int(input())
cnt = 0
res = []

def is_beautiful():
    l_idx = 0
    while l_idx < n:
        curr = res[l_idx]
        r_idx = l_idx + curr

        if r_idx - 1 >= n:
            return False

        for r in range(l_idx, r_idx):
            if curr != res[r]:
                return False
        l_idx = r_idx
    return True

def count():
    global cnt
    if is_beautiful():
        cnt += 1

def choose(curr):
    if curr == n + 1:
        count()
        return
    for j in range(1, 5):
        res.append(j)
        choose(curr + 1)
        res.pop()
        
choose(1)
print(cnt)