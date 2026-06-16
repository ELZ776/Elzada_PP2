age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Positive or Negative
number = -5
if number > 0:
    print("Positive")
else:
    print("Negative or Zero")

# Login status
is_logged_in = True
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in")

# Username validation
username = ""
if username:
    print("Username accepted")
else:
    print("Username cannot be empty")

# Even or Odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

age = 10
if age > 0:
    if age < 6:
        print("You are in preschool.")
    else:
        if age <= 12:
            print("You are in primary school.")
        else:
            if age <= 18:
                print("You are in high school.")
            else:
                print("You are an adult.")