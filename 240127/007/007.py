secret, loc, time = input().split()

class App:
    def __init__(self, secret, loc, time):
        self.s = secret
        self.l = loc
        self.t = time

a = App(secret, loc, time)
print('secret code :', a.s)
print('meeting point :', a.l)
print('time :', a.t)