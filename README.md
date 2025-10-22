# Learning-Python-02
Learning python through a full course tutorial. [9/9/25 - Present]

This repository will document the process of my python learning through the use of a full course available [**HERE**](https://www.youtube.com/watch?v=ix9cRaBkVe0) on YouTube.  
Below will hold my notes taken for each day and will contain any code I type alongside the course.

## Day 1 [9/9/25]

Today's lesson is review on variables, typecasting, and user input. I end by performing multiple exercises regarding these topics.

### Code Used: [Review01.py](Review01.py)

### Notes:

N/A. All review.

---

## Day 2 [9/11/25]

Today I practiced with arithmetic and math functions, if statements, and user inputs. I also learned more about conditional expressions. I performed a variety of exercises surrounding these topics.

### Code Used: [Review02.py](Review02.py)

### Notes:

* Make sure to properly order your if statements to prevent overlapping statements.
* When using an if statement and a boolean together, you do not need to write a condition for the boolean.
* When creating a condition to test if an interger is between two others, you write it like this: '12 > x > 5'

---

## Day 3 [9/16/25]

Today I learned about frequently used string methods along with string indexing. I also learned about multiple formatting flags. Lastly I reviewed and practiced with while loops. I used all of this newfound knowledge to create a compound interest calculator.

### Code Used: [Lesson01.py](Lesson01.py)

### Notes:

N/A.

---

## Day 4 [9/18/25]

Today I reviewed for loops and nested loops. I also learned about the differences and uses of lists, tuples, and sets. I performed a couple of exercises regarding these topics.

### Code Used: [Lesson02.py](Lesson02.py)

### Notes:

* the 'dir()' function allows you to look at attributes of lists, tuples, and sets.
* the 'help()' function is just like '--help' for Linux.

---

## Day 5 [9/23/25]

Today I practiced with many exercises regarding new syntax I learned such as 2D lists/tuples and dictionaries. 

### Code Used: [Lesson03.py](Lesson03.py)

### Notes:

* Try and always use tuples. They are faster. If you need interchangeable variables, then use a list.
* You use the same curly brackets '{}' for both dictionaries and sets.

---

## Day 6 [9/25/25]

Today I learned about using the random function and made two python coded games using this function.

### Code Used: [Lesson04.py](Lesson04.py)

### Notes:

* N/A

---

## Day 7 [9/30/25]

Today I start by using what I learned about the random function last time to create a dice roller. Following this exercise, I overview custom functions and return statements. The different types of arguments such as: positional, default, keyword, and arbitrary are also learned and used in additional exercises.

### Code Used: [Lesson05.py](Lesson05.py)

### Notes:

* Default arguments should always be in front of any other argument. (This applies to *args and **kwargs as well)
* '**kwargs' stands for: keyword arguments.
* keyword arguments are useful for better readability and are useful for appending any extra arguments.
* The asterik '*' is referred to as the unpacking operator in python.

---

## Day 8 [10/02/25]

Today I reviewed the concepts of iterables variables and membership operators (in/not in). I finished the lesson by better understanding how and when to use list comprehensions.

### Code Used: [Lesson06.py](Lesson06.py)

### Notes:

* When you want to get the values of a dictionary in python, you must use the bulit-in '.values()' method and append it to your dictionary.
* When you want both the keys and values, you must use the '.items()' function. Below will be an example:
###
    > for key, value in my_dictionary.items():
    > print(key, value)

---

## Day 9 [10/07/25]

Today I learned how to use Match-case statements along with creating your own modules. I also learned about the LEGB order for variables and both the use and purpose of the 'if _name_ == _main_' statement. I put all of these skills to use by creating a banking program, a slot machine program, and an encryption program.

### Code Used: [Lesson07.py](Lesson07.py)

### Notes:

* The pipe operator '|' is used as an 'or' statement for Match-Case Statements.
* A module is a file which contains code that you can use for a program. (import)
* To make your own module you must make a seperate python file(similar to a class)
* Dunder means double underscore (__)
* The 'if _name_ == _main_' line allows you to borrow functions from another python script. This setup will not run all the code in said python script and will allow you to just call and borrow a function. (Pretty much standard in java but you have to write it out for python)
* The above line is good practice for readability, leaving no global variables, and avoiding any unintentional executions.

---

## Day 10 [10/09/25]

Today I...

### Code Used: [Lesson08.py](Lesson08.py)

### Notes:

* Since the backslash character is technically an escape character when used in a string, you must use double backslash '\\' to print one.
* " ".join(hint)

---

## Day 11 [10/14/25]

Today I learned all about the fundamentals of Object Oriented Programming (OOP). The different operators and structures were reviewed and used in multiple examples. Class variables and inheritance, which regard OOP, were also learned. Lastly the super() method was learned and used.

### Code Used: [Lesson09.py](Lesson09.py)

### Notes:

* Python Object Oriented Programming (OOP) is a concept which structures coding around objects. Objects can have various attributes (variables) and methods (functions). Basically coding with classes.
* The dot operator '.' is used and know as the Attribute Access Operator. This dot allows you to print certain attributes found in an object defined in a class.
* Class variables are defined out of the constructor, acting as a global variable for classes. They're accessible to all objects defined in the class.
* Inheritance allows a second class to obtain class variables from a first class by calling on it.
* **_Multiple Inheritance:_** This is when a child class inherits attributes from two parent classes. 'C(A, B)'
  **_Multilevel Inheritance:_** This is when a parent class inherits from another parent class.
* If you are not assigning any attributes for a method, you do not need a constructor.
* **_Method Overriding:_** If a child class shares a method name with a parent class, the child method will override and be used.

---

## Day 12 [10/21/25]

Today I began by learning about polymorphism and duck typing. They are both used to classify objects and classes. I ended by clarifying the different types of methods for OOP. This being: class methods, static methods, and instance methods.

### Code Used: [Lesson10.py](Lesson10.py)

### Notes:

* Polymorphism in coding is when an object can be considered multiple other objects all at once.
* 'Duck Typing' is when an object has a minimum number of necessary attributes to be considered another object/class.
* If an object can have the same variables/perform the same, it can be considered another object.
* To use a static method, you will not need to create an object, since it is not tied to one. You can instead used the class name as such in the lesson file:
###
    > Employee.is_valid_position("Cook")

* '@classmethod' is the example of something called a ** _Decorator_**.
* The purpose of a class method: A class method allows you to access and/or modify class data, such as class variables.
### Keyboard Shortcut (VSCode): 'Ctrl + D' while highlighting a word will allow you to edit multiple words of the same instance.

