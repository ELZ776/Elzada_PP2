# First parent class
class Father:
    def father_skill(self):
        print("I can drive")

# Second parent class
class Mother:
    def mother_skill(self):
        print("I can cook")

# Child class inherits from two parents
class Child(Father, Mother):
    def child_skill(self):
        print("I can study")

# Create object
c1 = Child()

# Call methods from all classes
c1.father_skill()
c1.mother_skill()
c1.child_skill()