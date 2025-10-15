# Python Object Oriented Programming
# -constructors are necessary for classes to create objects.
# --you should put class information into seperate files for readability.
# --The code below will represent the above info:
#       "from seperate_filename import Car"

class Car:  # This is an object
    def __init__(self, model, year, color, for_sale):  # This is a constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):  # This is a method
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("Exige", 2011, "grey", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1.model)
print(car3.year)
print(car2.color)
print(car2.for_sale)
car1.drive()
car2.drive()
car3.stop()
car1.describe()
car2.describe()


# class variables

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Vanisher", 22)
student2 = Student("Magdalena", 23)
print(student1.name)
print(student1.age)
print(Student.class_year)  # good practice
print(Student.num_students)


print(
    f"\nMy graduating class of {Student.class_year} has {Student.num_students} students.")


# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Mouse(Animal):
    def speak(self):
        print("Sqeek")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
mouse.eat()
cat.sleep()

mouse.speak()


# Multiple/Multilevel Inheritance

# "grandparent" classes vvv
class Creature:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# parent classes vvv


class Prey(Creature):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Creature):
    def hunt(self):
        print(f"{self.name} is hunting")

# children classes vvv


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()

rabbit.eat()
fish.sleep()


# Super()

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(
            f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()


class Square(Shapes):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(
            f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()


class Triangle(Shapes):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(
            f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()


circle = Circle(color="grey", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(circle.radius)
print(square.width)
print(triangle.color)

circle.describe()
square.describe()
triangle.describe()
