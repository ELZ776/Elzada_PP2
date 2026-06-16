# Class variable example
class Student:
    school = "KBTU"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

s1 = Student("Ashley", 18)
s2 = Student("Emil", 19)

print(s1.name, s1.age, s1.school)
print(s2.name, s2.age, s2.school)

# Change class variable
class Student:
    school = "MNU"

    def __init__(self, name):
        self.name = name

s1 = Student("Ashley")
s2 = Student("Tobias")


Student.school = "KBTU"


print(s1.name, s1.school)
print(s2.name, s2.school)

# Instance variable vs class variable
class Student:
    university = "MNU"  # Class variable

    def __init__(self, name, gpa):
        self.name = name  # Instance variable
        self.gpa = gpa    # Instance variable


s1 = Student("Ashley", 3.5)
s2 = Student("Emil", 3.0)

print(s1.name, s1.gpa, s1.university)
print(s2.name, s2.gpa, s2.university)