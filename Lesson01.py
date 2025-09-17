# String Methods

name = input("Enter your full name: ")

result: int = len(name)
result2: int = name.find("M")  # finds first occurance
result3: int = name.rfind("i")  # finds last occurance
result4: str = name.capitalize()  # Will only upper the first letter
result5: str = name.upper()  # .lower() does the opposite
result6: bool = name.isdigit()  # returns if a string ONLY contains digits
# returns if a string ONLY has alphabetical letters.
result7: bool = name.isalpha()

# print(result5)

phone_num = input("Enter your phone #: ")

result8: int = phone_num.count("-")
result9: str = phone_num.replace("-", " ")  # very useful
print(result9)

help_func = help(int)
print(help_func)

# String Exercise

username = input("Enter a valid username: ")

if len(username) > 12:
    print("Username is too long")
elif not username.isalpha():  # is False or username.isdigit(): # Checks for numbers and spaces
    print("Username cannot contain any spaces or numbers")
else:
    print(f"{username} is a valid username")

# String Indexing

#    index ct:     0123 4567 89...
credit_num: str = "1234-4685-9261-5738"

print(credit_num[2])
print(credit_num[0:4])  # index format - [start : end : step]
print(credit_num[5:9])
print(credit_num[5:])
print(credit_num[-1])
print(credit_num[::2])  # prints every other character
print(credit_num[::3])

last_digits: int = credit_num[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse: str = credit_num[::-1]  # will reverse string
print(reverse)

# Format Specifiers:
#         :.#f adds a decimal count
#         :# adds a dedicated amount of spaces before the object
#         :0# pads the spaces with 0's.
#       :<# aligns to the left
#       :^# aligns to the center
#       :># aligns to the right
#         :+ displays plus for any pos. values
#         :, separates thousands with ,
#         :+ displays plus for any pos. values

price1: float = 3.14159
price2: float = -987.65
price3: float = 12.34
price4: float = 3000.141823

print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:010}")

print(f"Price 4 is ${price1:<10}")
print(f"Price 5 is ${price1:^10}")
print(f"Price 6 is ${price1:>10}")

print(f"Price 7 is ${price1:+}")
print(f"Price 8 is ${price4:+,.2f}")

# while loops

new_name = input("Enter your name: ")

while new_name == "":
    print("You did not enter your name")
    new_name = input("Enter your name: ")
print(f"Hello {new_name}")


age: int = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative")
    age: int = int(input("Enter your age: "))
print(f"You are {age} years old")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print("bye bye")


num_range: int = int(input("Enter a number between 1-10: "))

while num_range < 1 or num_range > 10:
    print(f"{num_range} is not valid")
    num_range: int = int(input("Enter a number between 1-10: "))
print(f"Your number is {num_range}")

# Python compund interest calculator

principle: int = 0
rate: int = 0
time: int = 0

while principle <= 0:
    principle: float = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate: float = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero")

while time <= 0:
    time: int = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time cannot be less than or equal to zero")

total: float = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")


# Python compund interest calculator (allows 0's)

principle: int = 0
rate: int = 0
time: int = 0

while True:
    principle: float = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cannot be less than zero")
    else:
        break

while True:
    rate: float = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than zero")
    else:
        break

while True:
    time: int = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cannot be less than zero")
    else:
        break

total: float = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
