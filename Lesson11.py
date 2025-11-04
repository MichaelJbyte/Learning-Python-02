# Magic methods (dunder) __init__, __str__

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):  # equal
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):  # less than
        return self.num_pages < other.num_pages

    def __gt__(self, other):  # greater than
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch, and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 210)

print(book1)
print(book2)
print(book3)
print(book1 == book4)
print(book2 > book3)
print(book2 + book3)

print("Lion" in book3)
print(book1['title'])
print(book2['author'])
print(book4['num_pages'])
print(book3['audio'])


# @property | decorator (getter, setter, deleter)
# You can add logic when reading attributes when you try to get them.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property  # getter
    def width(self):
        return f"{self._width:.1f}cm"

    @property  # getter
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter  # setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than 0")

    @height.setter  # setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(3, 4)

rectangle.width = 0
rectangle.width = 5

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle._height)


# Decorator | extends the behavior of another function
# Adds something to a base function without changing it

def add_sprinkles(func):
    # wrapper is necessary otherwise the function will be called on its own
    def wrapper(*args, **kwargs):
        print("You add sprinkles: #")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge: ~")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"                        O\nHere is your {flavor} ice cream: V")


get_ice_cream("vanilla")


# Exception | ZeroDivisionError, TypeError, ValueError
#        try:
# Try some code
#        except Exception:
# Handle an Exception
#        finally:
# Do some clean up

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by 0")
except ValueError:
    print("Please enter a number")
except Exception:
    print("Something went wrong")
finally:  # always executes
    print("Do some cleanup here")
