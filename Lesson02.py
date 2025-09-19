# For loops

import time
for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!")

for x in range(1, 11, 3):
    print(x)


credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# Countdown Timer (Exercise)


my_time: int = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):  # Another way to count backwards
    seconds: int = x % 60
    # the modulus stops the parameter from going above the number
    minutes: int = int(x / 60) % 60
    hours: int = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Time is up.")

# nested loops

rows: int = int(input("Enter the number of rows: "))
columns: int = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()  # prints a new line


# Lists, Sets, Tuples
#   Lists []: Ordered and changeable.
#   Sets {}: Unordered; cannot be altered; Cannot have dupes.
#   Tuples (): Ordered; cannot be altered; Faster


# Lists ________________________

fruits = ["apple", "orange", "banana", "coconut"]
fruits[0] = "pineapple"
fruits.append("watermelon")
fruits.remove("watermelon")
fruits.insert(0, "peach")


# print(fruits.index("pineapple"))
# print(fruits.count("pineapple"))
#   fruits.clear()
#   fruits.reverse()
#   fruits.sort()
# print(dir(fruits))
# print(helpr(fruits))
print(len(fruits))  # prints number of elements in list


print(fruits[:3])
print(fruits[:: 2])  # every other index

for fruit in fruits:
    print(fruit)

# Sets ________________________
# Cannot use indexing
# shares clear(), len()

proteins = {"eggs", "chicken", "beef", "nuts"}

proteins.add("walnuts")
proteins.remove("eggs")
proteins.pop()  # removes whatever element is first
proteins.add("walnuts")  # wont add it.

print(proteins)

# Tuples ________________________
# shares len(),

colors = ("blue", "red", "green", "yellow", "blue")


print(colors.count("blue"))
print(colors.index("blue"))
print(colors)
