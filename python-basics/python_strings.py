#quotes inside quotes------------------------------------------------------------------------------------------------------------------------------
print("He's my friend") 

#assign string to a variable------------------------------------------------------------------------------------------------------------------------------
my_color = "mlue"
print(my_color)   

#multiline string-----------------------------------------------------------------------------------------------------------------
a = """ Atyrau is a city in Kazakhstan 
and the capital of Atyrau Region. Atyrau is
 a transcontinental city, at the mouth of the
   Ural River on the Caspian Sea, between Europe
     and Asia, 2,700 kilometres (1,700 miles) 
     west of Almaty and 351 kilometres 
     (218 miles) east of the Russian city of 
     Astrakhan. """
print(a)

#Strings are Arrays-----------------------------------------------------------------------------------------------------
b = "Hello, World!"
print(b[2:5]) #from 2, to 4(include)

b = "Hello, World!"
print(b[:5]) #from the start to 4(included)

b = "Hello, World!"
print(b[2:])#from 2 to the end

b = "Hello, World!"
print(b[-5:-2]) #from index -5 to -3

#Looping through a string-----------------------------------------------------------------------------------------------------
for x in "cat":
    print(x)

#String length-------------------------------------------------------------------------------------------------------------------------------
password = "12345678"
if len(password) >= 8:
    print("Password is valid")
else:
    print("Password is too short")

#Check string with in--------------------------------------------------------------------------------------------------------------------------
word = "apple"
if "a" in word:
    print("Letter 'a' is present")


#Check if NOT with 'not in----------------------------------------------------------------------------------------------------------------------
password = "secret123"
if " " not in password:
    print("Password has no spaces")

