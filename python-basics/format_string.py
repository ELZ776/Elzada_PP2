#Basic f-strings with Variables----------------------------------------------------------------------------------------------------------------------
age = 20
txt = f"I am {age} years old"
print(txt)

#rMultiple Placeholders-------------------------------------------------------------------------------------------------------------------------------
name = "Elzada"
age = 20
txt = f"My name is {name} and I am {age} years old"
print(txt)

#Formatting Numbers (.2f for decimals)--------------------------------------------------------------------------------------------------------------------------
number = 42.5678
txt = f"The number is {number:.2f}"
print(txt)

#Math Operations in f-strings--------------------------------------------------------------------------------------------------------------------------
score1 = 85
score2 = 95
txt = f"Average score: {(score1 + score2) / 2}"
print(txt)