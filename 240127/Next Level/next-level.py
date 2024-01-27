class Student():
    def __init__(self, id, level='1'):
        self.id = id
        self.level = level

b_id, b_level = input().split()
a = Student('codetree', '10')
b = Student(b_id, b_level)

print(f'user {a.id} lv {a.level}')
print(f'user {b.id} lv {b.level}')