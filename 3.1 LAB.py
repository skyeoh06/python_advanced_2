#Introduction to PEP 8
#Recommendations for Code Layout
#In this section, we’ll focus on style recommendations related to such things as:

#indentation, using tabs and spaces;
#line length, line breaks, and blank lines;
#source file encoding and module imports.
#Indentation
#The indentation level, understood as the leading whitespace (i.e., spaces and tabs) at the beginning of each logical line, is used to group statements.
#When writing code in Python, you should remember to follow these two simple rules:

#Use four spaces per indentation level, and;
#Use spaces rather than tabs.
# Good:

def my_function(x, y):
    return x * y

#Continuation lines
#Continuation lines (i.e., logical lines of code that you want to split because they’re too long or because you want to improve readability) are allowed if using parentheses/brackets/braces:
# Good:

my_list_two = [
    1, 2, 3,
    4, 5, 6,
]


def my_fun(
        a, b, c,
        d, e, f):
    return (a + b + c) * (d + e + f)

#Maximum Line Length and Line Breaks
#If possible, you should limit all lines to a maximum of 79 characters as this will help you avoid wrapping several lines of code. If line wrapping is inevitable, use Python’s implied line continuation from the previous page.
#Line breaks and operators
#Even though in Python you’re allowed to break code lines before or after binary operators (providing you do so consistently and that this convention has been used in your code before), 
#it is recommended that you follow Donald Knuth’s style suggestions and break before binary operators as this results in a more readable, eye-friendly code.
# Recommended

total_fruits = (apples
                + pears
                + grapes
                - (black currants - red currants)
                - bananas
                + oranges)


#Blank Lines
#Blank lines, called vertical whitespaces, improve the readability of your code.
#– two blank lines to surround top-level function and class definitions:
class ClassOne:
    pass


Class ClassTwo:
    pass


def my_top_level_function():
    return None

#– a single blank line to surround method definitions inside a class:

class MyClass:
    def method_one(self):
        return None

    def method_two(self):
        return None

#– blank lines in functions in order to indicate logical sections (sparingly). For example:

def calculate_average():
    how_many_numbers = int(input("How many numbers? "))
    
    if how_many_numbers > 0:
        sum_numbers = 0
        for i in range(0, how_many_numbers):
            number = float(input("Enter a number: "))
            sum_numbers += number

        average = 0
        average = sum_numbers / how_many_numbers

        return average
    else:
        return "Nothing happens."
      
#Default encodings
#It is recommended that you use Python’s default encodings (Python 3 -- UTF-8, Python 2 -- ASCII)
#PEP 8 states that “all identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words whenever feasible".

#You should always put imports at the beginning of your script, between module comments/docstrings and module globals and constants, respecting the following order:

#Standard library imports;
#Related third-party imports;
#Local application/library specific imports.
# Good:

import os
import sys

from subprocess import Popen, PIPE

#If possible, use absolute imports (i.e., imports that use absolute paths separated by full stops). For example:

import animals.mammals.dogs.puppies

#Recommendations for string quotes, whitespace, and trailing commas
#String quotes
#Python allows us to use single-quoted (e.g., 'a string') and double-quoted (e.g., "a string") strings. 
#Whitespace in expressions and statements
#PEP 8 contains a long section that shows examples of correct and incorrect uses of whitespace in code. Generally, you should avoid using too much whitespace, as it makes your code difficult to follow.
# Good:

my_list = (dog[2], 5, {"year": 1980}, "string")
if 5 in my_list: print("Hello!"); print("Goodbye!")

#In the case of a slice, the colon should have equal amounts of space on both sides (it should act like a binary operator) unless a slice parameter is omitted, in which case the space should be omitted, too.
# Good:

bread[0:3], roll[1:3:5], bun[3:5:], donut[1::5]

#Trailing commas
#Again, do not use excessive whitespace:

#after a trailing comma followed by a closing parenthesis, or
#immediately before an opening parenthesis that marks the beginning of the argument list of a function invocation, or
#immediately before an opening parenthesis that marks the beginning of indexing/slicing.
# Good:

my_tuple = (0, 1, 2,)
my_function(5)
my_dictionary['key'] = my_list[index]

#Don’t use more than one space before and after operators, e.g.:
# Good:

a = 1
b = a + 2
my_string = 'string' * 2

#Surround binary operators with a single space on both sides. 
# Good:

x = x + 3
x -= 1

x = x*2 - 1  # Use your own judgement.
x = (x-1) * (x+2)  # Use your own judgement.

#Don’t surround the = operator with spaces if it’s used to indicate a keyword argument/default value, e.g.:
# Good:

def my_function(x, y=2):
    return x * y

#Recommendations for using comments
#There are a few rules you should follow when leaving comments in code:

#Write comments that will not contradict the code or mislead the reader. They’re much worse than no comment at all.
#Update your comments when your program gets updated.
#Write comments as complete sentences (capitalize the first word if it’s not an identifier, and end your sentence with a full stop). 
#When writing block comments with multi-sentence comments, use two spaces after each full stop ending a sentence, except after the final sentence.
#Write comments in English.
#Comments should consist of no more than 72 characters per line.

#Block comments
#Block comments are usually longer, and you should use them to explain sections of code rather than particular lines. 
#Generally, block comments:

#should refer to the code that follows them;
#should be indented to the same level as the code they describe.
def calculate_product():
    # Calculate the average of three numbers obtained from the user. Then 
    # multiply the result by 4.17, and assign it to the product variable.
    #
    # Return the value passed to the product variable and use it
    # for the subsequent x to y calculations to speed up the process.
    sum_numbers = 0
    
    for number in range(0, 3):
        number = float(input("Enter a number: "))
        sum_numbers += number
    
    average = (sum_numbers / 3) * 4.17
    product = average
    return product

x = product * 1.73
y = x ** 2
x_to_y = (x*y) / 1.05

#Inline comments
#Inline comments are comments that are written on the same line as your statements. They should address or provide further explanation to a single line of code or a single statement. You should not overuse them.
#Generally, inline comments should be:

#separated by two (or more) spaces from the statement they address;
#used sparingly.
counter = 0     # Initialize the counter.

#Documentation strings, or docstrings as they’re often called, let you provide descriptions and explanations for all public modules, files, functions, classes, and methods you use in your code. You should use them in this context.
# A multi-line docstring:

def fun(x, y):
    """Convert x and y to strings,
    and return a list of strings.
    """
    ...


# A single-line docstring:

def fun(x):
    """Return the square root of x."""
    ...

#Naming conventions
#Naming styles
#There are many different naming styles used in programming, for example:

#a – single lowercase letter
#A – single uppercase letter

#Naming conventions – recommendations
#When giving a name to a variable, you should use a lowercase letter or word(s), and separate words by underscores, e.g., x, var, my_variable. The same convention applies to global variables.
#Functions follow the same rules as variables, i.e., when giving a name to a function, you should use a lowercase letter or word(s) separated by underscores, e.g., fun, my_function.
#When giving a name to a class, you should adopt the CamelCase style, e.g., MySampleClass, or if there's only one word, start it with a capital letter, e.g., Sample.
#When giving a name to a method, you should use a lowercase word or words separated by underscores, e.g., method, my_class_method. You should always use self for the first argument to instance methods, and cls for the first argument to class methods.
#When giving a name to a constant, you should use uppercase letters and separate words by underscores, e.g., TOTAL, MY_CONSTANT.
#When giving a name to a module, you should use a lowercase word or words, preferably short, and separate them with underscores, e.g., samples.py, my_samples..
#When giving a name to a package, you should use a lowercase word or words, preferably short ones. You shouldn't separate words, e.g., package, mypackage.
#Type variable names should follow the CamelCase convention and be short, e.g., AnyStr, or Num.
#When giving a name to an exception, you should follow the same convention as with classes (bear in mind that exceptions should actually be classes), i.e., use the CamelCase style.
#Note: You can use a different style, e.g., mixed case (mySample) for functions and variables, but only if this helps to retain backwards compatibility, and if that's the prevailing style.

#Programming recommendations
#– make comparisons to the None object with the use of is or is not, not with the (in)equality operators (== and !=), e.g.:
# Good:

if x is None:
    print("A")

#– do not use the (in)equality operators when comparing Boolean values to True or False. Again, use is or is not instead:
# Good:

my_boolean_value = 2 > 1
if my_boolean_value is True:
    print("A")
else:
    print("B")

  # Better:

my_boolean_value = 2 > 1
if my_boolean_value:
    print("A")
else:
    print("B")

#– for readability purposes, use the is not operator instead of not … is:
# Good:

if x is not None:
    print("It exists")

#– when you want to “catch" an exception, refer to specific exceptions rather than use the bare except: clause only:
try:
    import my_module
except ImportError:
    my_module = None

#– when checking for prefixes or suffixes, use the ''.startswith() and ''.endswith() string methods, as they’re cleaner and less error prone. Generally, it’s better to use string methods over importing the string module.
# Good:

if name.startswith('Adam'):
    # do something
