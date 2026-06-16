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
    pass

# Create child object
x = Student("Mike", "Olsen")

# Call inherited method
x.printname()