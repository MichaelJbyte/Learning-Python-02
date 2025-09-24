# Shopping Cart Program

foods = []
prices = []
total: float = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("----- YOUR CART -----")

for food in foods:
    print(food, end=", ")

for price in prices:
    total += price

print()
print(f"YOUR TOTAL: ${total}")

# 2D Lists (2D Arrays)

fruits = ["apple", "orange", "banana", "coconut"]
veggies = ["celery", "carrots", "potatoes"]
meat = ["chicken", "meat", "turkey"]


groceries = [fruits, veggies, meat]

# Also works:
groceries2 = [["apple", "orange", "banana", "coconut"],
              ["celery", "carrots", "potatoes"],
              ["chicken", "meat", "turkey"]]

print(groceries[0][2])

for collection in groceries:
    for food in collection:
        print(food, end=" | ")

# Keypad (Exercise)

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for key in row:
        print(key, end=" ")
    print()

# Python Quiz Game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             " How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ",)

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num: int = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("\n--------------RESULTS---------------")
print(f"The quiz is over | YOUR SCORE = {score}")
if score >= 4:
    print("Good Job!")
else:
    print("Oooh, Try Again.")

# Dictionary | ordered and changeable. No dupes.

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#   print(help(capitals))
print(capitals.get("India"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()  # removes the most recent addition
#   capitals.clear()
c_keys = capitals.keys()
values = capitals.values()
items = capitals.items()  # resembles a 2D list

print(capitals)
print(c_keys)
print(values)
print(items)

for key in c_keys:
    print(key)

for value in values:
    print(value)

for key, value in items:
    print(f"{key}: {value}")

# Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25, }

cart = []
total: int = 0

print("-------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}| ${value:.2f}")
print("-----------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" | ")

print(f"\nTotal is: ${total:.2f}")
