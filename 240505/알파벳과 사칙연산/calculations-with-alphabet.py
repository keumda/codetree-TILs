formula = input()

alph = []
match_alph = ['a', 'b', 'c', 'd', 'e', 'f']
alpha_map =  {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
res = list()

def choose(idx):
    if idx == len(match_alph):
        calculate()
        return
    else:
        for j in range(1, 4 + 1):
            alpha_map[match_alph[idx]] = j
            choose(idx + 1)
        return

def calculate():
    idx = 0
    curr = formula[idx]
    while True:
        
        sigh = formula[idx+1]
        second = formula[idx+2]

        if type(curr) is str:
            curr = alpha_map[curr]
        if sigh == '*':
            val = curr * alpha_map[second]
        if sigh == '+':
            val = curr + alpha_map[second]
        if sigh == '-':
            val = curr - alpha_map[second]

        curr = val
        idx += 1

        if idx + 2 >= len(formula):
            res.append(curr)
            break
        
if len(formula) == 1:
    print(4)
else:
    choose(0)
    print(max(res))