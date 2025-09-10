# Review

first_name: str = "Vanisher"
email: str = "vanisher@gmail.com"
gpa: float = 3.98
age: int = 25
is_student: bool = False

#   print("I like music")
#   print("It's really fun")

#   print(f"\nHello {first_name}")
#   print(f"Your email is: {email}")
#   print(f"Your GPA is {gpa}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

# Type Casting

gpa = int(gpa)
#   print(gpa)

age = float(age)
#   print(age)

# Input()

#   input_name: str = input("What is your name? ")
#   input_age: int = input("What is your age? ")

#   input_age = int(input_age) + 1

#   print(f"Hello {input_name}")
#   print(f"You are {input_age} years old next year")

# Exercise 1 & 2

#   print("We are going to find the area of a Rectangle")
#   length: str = input("What is the length: ")
#   width: str = input("What is the width: ")

#   area: int = int(length) * int(width)

#   print(f"\nThe area is {area}")

#  item: str = input("What item would you like: ")
#  price: float = float(input("What is the price: $"))
#  quantity: int = int(input("How many would you like: "))
#  total: float = price * quantity

#  print(f"You have bought {quantity} x {item}/s")
#  print(f"Your total is: ${total}")

# Madlibs

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
