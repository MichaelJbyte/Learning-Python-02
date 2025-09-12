# Math, Arithmetic
import math

x = 3.14
y = 4
z = 5
a = 9.1

result = round(x)
result2 = abs(y)
result3 = pow(y, 3)
result4 = max(x, y, z)
result5 = min(x, y, z)
result6 = math.sqrt(a)
result7 = math.ceil(a) | rounds up
result8 = math.floor(a)  |  rounds down

print(result)

# Exercises

radius = float(input("Enter the radius of a circle: "))

circumference: float = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}")


radius = float(input("Enter the radius of a circle: "))

area: float = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 4)}cm^2")

# Area of a Triangle

side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))

side_c = math.sqrt(pow(side_a, 2) + pow(side_b, 2))

print(f"side C equals {side_c}")

# Python Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 1st number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not a valid unit")

# Temperature Conversion

t_unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if t_unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}F")
elif t_unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}C")
else:
    print(f"{t_unit} is an invalid unit of measurement")

# Conditional Expressions (Tenary)

new_num: int = 5
var1: int = 6
var2: int = 7
print("Positive" if new_num > 0 else "Negative")


result = "EVEN" if new_num % 2 == 0 else "ODD"
print(result)


max_num = var1 if var1 > var2 else var2
min_num = var1 if var1 < var2 else var2
print(max_num)


age: int = 13
status = "Adult" if age >= 18 else "Child"
print(status)


new_temp: int = 10
weather = "HOT" if new_temp > 20 else "COLD"
print(weather)


user_role: str = "guest"
access_lvl = "Full Access" if user_role == "admin" else "Limited Access"
print(access_lvl)

