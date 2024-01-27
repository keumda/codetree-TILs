class Student():
    def __init__(self, user_id='', level='1'):
        self.user_id = user_id
        self.level = level

b_id, b_level = input().split()
a = Student('codetree', '10')
b = Student()
b.user_id = b_id
b.level = b_level

print(f'user {a.user_id} lv {a.level}')
print(f'user {b.user_id} lv {b.level}')