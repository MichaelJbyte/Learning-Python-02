# Dice Roller
import time
import random

# dictionary made of key value pairs, value is a tuple
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total: int = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

#    for die in range(num_of_dice):
#       for line in dice_art.get(dice[die]):
#           print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()


for die in dice:
    total += die
print(f"Total: {total}")

# Functions


def happy_birthday(name: str, age: int):
    print("Hey!")
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")


happy_birthday("Vanisher", 19)


def display_invoice(username: str, amount: float, due_date: str):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("Vanisher", 100.01, "11/11")

# Return


def create_name(first: str, last: str):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("vanisher", "imaginal")
print(full_name)

# Default Arguments


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500, 0.1, 0))


# default args should be after positional args.


def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")


count(30, 15)

# Keyword Arguments


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


# positional args are always first
hello("Hello", first="Vanisher", title="Dr.", last="Imaginal")

for x in range(1, 11):
    print(x, end=" ")  # 'end=' is a keyword arg.

print("1", "2", "3", "4", "5", sep="-")  # 'sep=' is a keyword arg.


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1, area=562, first=805, last=4521)

print(phone_num)


# Arbitrary Arguments | *args, **kwargs
#   * unpacking operator
#   *args puts all arguments into tuple. | passes non-keyword arguments
#   *kwargs puts all arguments into dictionary. | passes keyword arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name("Dr.", "James", "Vanisher", "John", "III")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="Michigan",
              zip="54321")

# keyword args should always be behind directional args


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} #{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Vanisher", "Imaginal", "III",
               street="123 Fake St.",
               apt="101",
               city="Detroit",
               state="MI",
               zip="54321")
