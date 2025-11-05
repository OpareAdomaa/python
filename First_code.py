import random

print("Welcome to the guessing game.\nGoodluck!")

while True:
    try:
        secret = random.randint(1, 10)
        number = int(input("Enter a number between 1 & 10: "))
        
        if (number < 1 or number >10):
            print("Please follow the instructions.")
            continue  

        if ( number == secret):
            print("You beat us!! Well done.")
            break
        elif (number != secret):
            print("We beat you! Try again.")
    
    except ValueError:
        print("Please enter a valid number.")