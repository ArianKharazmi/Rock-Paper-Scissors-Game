import random

user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]

options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit the Game: ").lower()
    if user_input == "quit":
        break

    if user_input not in options:
        continue
        print("Please type in a valid answer.")

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_guess = options[random_number]
    print("Computer chose", computer_guess + ".")

    if user_input == computer_guess:
        print("Draw! No winner selected.")
        draw += 1
        continue

    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_guess == "papers":
        print("You won!")
        user_wins += 1

    else:
        print("You lost to the computer!")
        computer_wins += 1

print("You won", user_wins, "times!")
print("The computer won", computer_wins, "times!")
print("Goodbye!")