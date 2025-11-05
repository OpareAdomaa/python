import random

print("Let's play Rock, Paper, Scissors.")

while True:
    Choices = ["Rock", "Paper", "Scissors"]
    Computer = random.choice(Choices)
    User = input("Enter your choice: ").capitalize()
    print(f"Computer chose: {Computer}")
    if User not in Choices:
        print("Invalid input. Try again.")
        continue
    if User == "Rock" and Computer == "Paper":
        print("Computer won! Try again.")
    if User == "Paper" and Computer == "Scissors":
        print("Computer won! Try again.")
    if User == "Scissors" and Computer == "Rock":
        print("Computerw won! Try again.")
    elif User == Computer:
        print("It's a tie! Let's go again.")
    else:
        print("You won! Congratulations! \nWould you like to play again? (Yes / No)")
        Play_Again = input().capitalize()
        if Play_Again == "No":
            break
        else:
            continue