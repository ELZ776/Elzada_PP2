# Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    # Parent method
    def printname(self):
        print(self.firstname, self.lastname)

# Child class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Call parent __init__
        self.graduationyear = year      # Child property

# Create object
x = Student("Mike", "Olsen", 2019)

# Print values
print(x.firstname)
print(x.lastname)
print(x.graduationyear)