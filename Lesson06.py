# Iterables

fruits = {"apple", "orange", "banana", "coconut"}

my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}

for fruit in fruits:
    print(fruit)

for key, value in my_dictionary.items():
    print(key, value)


name = "Vanisher"

for char in name:
    print(char, end=" ")

# Membership Operators | in/not in

word: str = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


students = {"patrick", "spongebob", "sandy"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} is NOT a student")
else:
    print(f"{student} is a student")


grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


email = "vanisher@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# List Comprehension

#       doubles = []

#       for value in range(1, 11):
#           doubles.append(value * 2)

#       print(doubles) | vvv concise version

doubles = [value * 2 for value in range(1, 11)]

triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)


fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruit_chars)


numbers = [1, -2, 3, -4, 5, -6]
pos_nums = [num for num in numbers if num >= 0]
neg_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]


print(odd_nums)


new_grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in new_grades if grade >= 60]
print(passing_grades)
