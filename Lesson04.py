# Random Numbers
import time
import random

options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A", ]

dice: int = random.randint(1, 20)
dice2: float = random.random()  # returns from 0-1
option = random.choice(options)
random.shuffle(cards)

print(cards)

# Number Guessing Game

lowest_num: int = 1
highest_num: int = 200
answer: int = random.randint(lowest_num, highest_num)
guesses: int = 0
is_running: bool = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

    if guess < lowest_num or guess > highest_num:
        print("That number is out of range")
        print(
            f"Please select a number between {lowest_num} and {highest_num}")
    elif guess < answer:
        print("Too low! Try again!")
    elif guess > answer:
        print("Too high! Try again!")
    else:
        print(f"CORRECT! The answer was {answer}")
        print(f"Number of guesses: {guesses}")
        is_running = False

else:
    print("Invalid guess")
    print(f"Please select a number between {lowest_num} and {highest_num}")

# Rock, Paper, Scissors
#   import random

game = ("rock", "paper", "scissors")
running: bool = True

print("Lets play Rock, Paper, Scissors!")

while running:

    player = None
    computer = random.choice(game)

    while player not in game:  # similar to a filter
        player = input("Make a decision (rock, paper, scissors): ")

    # countdown
    for x in reversed(range(1, 4)):
        print(f"{x}...")
        time.sleep(1)

    print(f"You throw {player}...")
    print(f"I throw {computer}!")

    if player == computer:
        print("Its a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You Lose!")

    if not input("Play Again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
