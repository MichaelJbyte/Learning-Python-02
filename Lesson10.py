# Polymorphism
from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):

    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)
        #   self.radius = radius


#   circle = Circle()  # a circle is both a circle and a shape. (Poly)

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(shape.area())


# "Duck Typing"
# 'If it looks like a duck, and quacks like a duck, it must be a duck'

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF")


class Cat(Animal):
    def speak(self):
        print("MEOW")


class Car:

    alive = False

    def speak(self):
        print("HONK")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


# Static methods | belong to classes, not objects

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):  # no self variable
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")


print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


# Class methods

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name}, {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"\


    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_avg_gpa())
