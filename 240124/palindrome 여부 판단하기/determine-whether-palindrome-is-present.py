a = input()

def is_panlindrome(s):
    if s[::-1] == s:
        print('Yes')
    else:
        print('No')

is_panlindrome(a)