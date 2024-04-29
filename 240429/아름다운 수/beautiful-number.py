n = int(input())
cnt = 0
res = []

def is_beautiful(num):
    str_num = str(num)
    l_idx, r_idx = 0, 0
    while True:
        if l_idx >= len(str_num):
            break

        curr = str_num[l_idx]
        r_idx = l_idx + int(curr)

        if r_idx > len(str_num):
            break

        for r in range(l_idx, r_idx):
            # print(l_idx, r_idx, r_idx)
            if curr != str_num[r]:
                return False
        l_idx = r_idx

    if r_idx == len(str_num):
        return True
    else:
        return False

def count():
    num = ""
    global cnt
    for d in res:
        num += str(d)
    if is_beautiful(int(num)):
        # print(num)
        cnt += 1

def choose(curr):
    if curr == n + 1:
        count()
        return
    else:
        for j in range(1, 5):
            res.append(j)
            choose(curr + 1)
            res.pop()
        return

choose(1)
print(cnt)