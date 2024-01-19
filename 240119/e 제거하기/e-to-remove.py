string = input()

for i, s in enumerate(string):
    if s == 'e':
        string = string[:i] + string[i+1:]
        break

print(string)