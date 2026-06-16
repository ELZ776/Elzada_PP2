fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
subjects = ["Math", "Physics", "Python", "Chemistry"]
for subject in subjects:
    if subject == "Python":
        print("Found Python!")
        break
    print("Checking:", subject)