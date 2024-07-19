#1.1
#The Zen of Python
#The Zen of Python is a collection of 19 aphorisms, which reflect the philosophy behind Python, its guiding principles, and design.
import this
>>
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

#What you see is a collection of some general truths for Python design rules and decision making. Even though the "poem" seems to be imbued with contradictions and allusions, 
#we assure you that the aphorisms are extremely practical and common sense, and you’re encouraged to accept them and implement in your code.

#1.2
#Beautiful is better than ugly
#Example: Write a program that calculates the hypotenuse of a right-angled triangle.
from math import sqrt

side_a = float(input("The length of the 'a' side: "))
side_b = float(input("The length of the 'b' side: "))
hypotenuse = sqrt(a**2 + b**2)

print("The length of the hypotenuse is", hypotenuse)

#1.3
#Explicit is better than implicit
#Example: Import apples and bananas from the fruit.py module.
from fruit import apples, bananas

apples(quantity=2, price=3.45)

#Therefore, it’s sometimes a good idea to add more verbosity to your code as it all counts towards readability. 
#Giving self-explanatory variable and function names, or adding more explicitness to imports or function arguments may be good practice.

#1.4
#Simple is better than complex
#Example: Sort the numbers list in ascending order.
numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
numbers.sort()

print(numbers)

#Remember: use appropriate tools adjusted to the specificity of your project.
#If you need to implement a more complex solution, divide problems into smaller, simpler parts.

#1.5
#Complex is better than complicated
# When your code gets big and too difficult to understand and grasp, divide it into well-separated parts, so that it’s easier to manage and handle.
#Example: Perform five additions of two numbers.
def addition(x, y):
    print(x, "+", y, "=", x+y)

for i in range(5):
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    addition(first_number, second_number)

#1.6
#Flat is better than nested
#Even though you can actually have any level of nested loops or if statements in Python, anything above three should be a clear signal that it’s maybe a good time to start refactoring your code.
#Flat code is more user-friendly, and becomes much easier to maintain. Remember this.
#Example: Display a message whether or not x is within the range from 4 to 6.
x = float(input("Enter a number: "))

if x >= 4 and x <=6:
    print("x is a number between 4 and 6.")
else:
    print("x is not a number between 4 and 6.")

#1.7
#Sparse is better than dense
#The easiest and most common way to introduce sparsity to your code is to introduce nesting. That’s probably why this aphorism comes right after the one which tells us to prefer flat code over nested code. 
#The key to readability is to strike a balance between the two: reduce nesting, then try to reduce density.
#Example: Print the message “Hello, World!” if the value passed to the x variable equals 1.
x = 1
if x == 1:
    print("Hello, World!")

#1.8
#Readability counts
#Giving meaningful names to variables, functions, modules, and classes; properly styling blocks of code; using comments where necessary; keeping your code neat and elegant –
#these all contribute to how readable and user-friendly your code is.
#Example: Write a program that calculates a product’s gross price.
# Calculates the gross price of products in Wonderland.

def calculate_gross_price(net_price):
    gross_price = net_price + (0.08 * net_price)
    return gross_price

#Remember: the readability of your code reflects how responsible a programmer you are. It not only reflects well on the quality of the code, it reflects well on its author.

#1.9
#Special cases aren't special enough to break the rules...
#Discipline, consistency, and compliance with standards and conventions are all important elements in professional and responsible code development. 
#There should be no exceptions that allow us to break the principles governing best coding practices.
#Example: Write a function that multiplies two numbers and a function that adds two numbers.
def multiply_two_numbers(first_number, second_number):
    return first_number * second_number

print(multiply_two_numbers(7, 9))


def add_two_numbers(first_number, second_number):
    return first_number + second_number

print(add_two_numbers(7, 9))

#1.10
#...Although, practicality beats purity
#If you need to write an 85-character long line of code because splitting it into two separate lines affects readability, do it. 
#If you need to keep compatibility with previously written code and use CamelCase instead of snake_case, do it. Rules sometimes have to be broken, exceptions have to be made.

#1.11
#Errors should never pass silently...
#The Python language provides a very good mechanism for error handling, with a number of built-in exceptions, and a great toolset for creating user-defined exception handling systems.
#he Zen of Python gently reminds us that if a block of code is unable to perform its function and work in the way that is expected by the programmer, it should terminate the program and/or loudly announce that something has gone wrong (i.e., raise an exception) rather than continue running without interruption.
#A program that crashes is easier to debug than a program that silences an error. Raising an exception draws your attention to the issue and provides important information about what happened and why. 
#An improved version, handling a specific kind of an error:
try:
    print(1/0)
except ZeroDivisionError:
    print("Don't divide by zero!")

#Well, naturally there may be situations where you don’t want to shout “Hey! There’s an error!” but rather handle it in a subtle way and not necessarily make a fuss about it.
#Analyze the code below in which we handle an exception by adding a default value:
try:
    number = int(input("Enter an integer number: "))
except:
    number = 0

#1.12
#In the face of ambiguity, refuse the temptation to guess.
#Another thing is that you should avoid writing ambiguous code, which means you should leave no room for guessing. Give your variables self-commenting names, and leave comments where necessary.

#1.13
#There should be one – and preferably only one – obvious way to do it
#The guideline also reminds us that it’s a good idea to follow the language use standards and conventions.
#Finally, the aphorism works as a gentle indication of yet another important piece of advice: where possible, it’s good to remember that each function, each class, each method – each entity – should have a single cohesive responsibility. 

#1.14
#Now is better than never
#Before you actually get down to doing these things – writing your code – you may have forgotten the ideas or information you need to do it well.

#1.15
#If the implementation is hard to explain, it's a bad idea
#Everything and anything that can be explained in words can be translated into code, and eventually turned into a well-operating computer program.\

#1.16
#Namespaces are one honking great idea – let's do more of those!
#Python provides a good, well-organized namespace mechanism to manage the availability of identifiers that you want to use and avoid conflicts with already existing names across different scopes.
#What is a namespace? Generally speaking, it’s “a mapping from names to objects”  implemented in Python in the form of a dictionary.
#whenever you define a variable, Python “remembers” two things: the variable’s identifier, and the value you pass to it.
#Functions, classes, objects, modules, packages… they’re all namespaces.
#*Using the global keyword before a global variable inside the function is a mechanism that allows you to alter that variable, even though it resides in a different scope (bad practice).
#Use the namespaces to make your code clearer and more readable. For example, do this:
from instruments import guitars

guitars.fender(page)
guitars.ibanez(vai)
