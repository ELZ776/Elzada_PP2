# Parent class
class Person:
    def introduce(self):
        print("I am a person")

# Child class
class Student(Person):
    # Override parent method
    def introduce(self):
        print("I am a student")

# Create objects
p1 = Person()
s1 = Student()

# Call methods
p1.introduce()
s1.introduce()