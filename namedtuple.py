from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'grade'])

s1 = Student('Ravi', 21, 'A')

print(s1)
print(s1.name)
print(s1.age)
print(s1.grade)