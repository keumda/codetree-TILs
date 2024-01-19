string = input()

for i, c in enumerate(string):
    if 'a'<= c and 'z' >= c:
        string = string[:i]+ c.upper() + string[i+1:]
    else:
        string = string[:i]+ c.lower() + string[i+1:]

print(string)