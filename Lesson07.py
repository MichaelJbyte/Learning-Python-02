
# Modules

#   import math
#   import math as m

#   print(m.pi)
import string
import random
from math import e as math_e
import example
from math import pi


print(pi)


result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)

# Match-case Statements | alternative to using many 'elif' statements


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:  # Wildcard/'else' statement
            return "Not a valid day"


print(day_of_week(8))


def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:  # Wildcard/'else' statement
            return False


print(is_weekend("Monday"))


# Variable Scope | Where a variable is visible and accessible
# Scope Resolution | (LEGB) -> Local-Enclosed-Global-Built-in
# LEGB is similar to order of operations

def func1():
    x = 1  # Local
    print(x)


def func2():
    #   x = 2
    print(x)


def func3():
    x = 1  # Enclosed

    def func4():
        # x = 2  # Local
        print(x)
    func4()


x = 5  # Global

func1()
func2()
func3()


# from math import e as math_e vvv


def func5():
    print(math_e)  # Built-in


func5()


# if __name__ == __main__:
#                          | checks if script is being run directly
#                          | will only run main() doe if being run directly
#                          | useful when you have >1 python scripts.
#                          | Lets you borrow functions.

def fav_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("hi")
    fav_food("pizza")
    print("Goodbye")


if __name__ == '__main__':  # runs first
    main()


# Python Banking Program

def show_balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}")
    print("*******************")


def deposit():
    print("*******************")
    amount = float(input("Enter an amount to deposit: "))
    print("*******************")

    if amount < 0:
        print("*******************")
        print("That's not a valid amount")
        print("*******************")
        return 0  # prevents an: 'adding to null' error
    else:
        return amount


def withdraw(balance):
    print("*******************")
    amount = float(input("Enter amount to withdraw: "))
    print("*******************")

    if amount > balance:
        print("*******************")
        print("Insufficient funds")
        print("*******************")
        return 0
    elif amount < 0:
        print("*******************")
        print("Amount must be greater than 0")
        print("*******************")
        return 0
    else:
        return amount


def main():
    balance: float = 0
    is_running: bool = True

    while is_running:
        print("*******************")
        print("Banking Program")
        print("*******************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*******************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*******************")
            print("Please enter a valid choice")
            print("*******************")

    print("*******************")
    print("Thank you, have a nice day!")
    print("*******************")


if __name__ == '__main__':
    main()


# Slot Machine


def spin_row():
    symbols = ["@", "#",  "&",  "$", "%"]

    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print("**********")
    print(" | ".join(row))
    print("**********")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "@":
                return bet * 3
            case "#":
                return bet * 4
            case "&":
                return bet * 5
            case "%":
                return bet * 10
            case "$":
                return bet * 20
    return 0


def main():
    balance: int = 100

    print("----------------------")
    print("Welcome to PySlots")
    print("Symbols: @ # & % $")
    print("----------------------")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: $")

        if not bet.isdigit():
            print("!!!Please enter a valid number!!!")
            continue  # restarts the loop from the beginning

        bet = int(bet)

        if bet >= balance:
            print("!!!Insufficient funds!!!")
            continue

        if bet <= 0:
            print("!!!Bet must be greater than 0!!!")

        balance -= bet

        row = spin_row()  # returns list
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost")

        balance += payout

        play_again = input("Would you like to spin again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print("*************************************")
    print(f"Game over! Your balance is: {balance}")
    print("*************************************")


if __name__ == "__main__":
    main()


# Encryption program

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()


random.shuffle(key)

#   print(f"chars: {chars}")
#   print(f"key  : {key}")

# ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPTION
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
