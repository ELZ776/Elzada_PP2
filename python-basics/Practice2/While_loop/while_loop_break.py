# While Loop with Break
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Stop searching when target is found
numbers = [3, 7, 12, 18, 25]
i = 0
while i < len(numbers):
    if numbers[i] == 18:
        print("Number found!")
        break
    print("Checking:", numbers[i])
    i += 1
    
#Example
    secret = 13
while True:
    guess = int(input("Guess the secret number (between 1 and 20): "))
    if guess == secret:
        print("Correct! You guessed it.")
        break
    else:
        print("Try again.")