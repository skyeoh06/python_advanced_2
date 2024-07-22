#1.3
#A few words on type hints: PEP 484
#In a nutshell, type hinting allows you to statically indicate the type information related to Python objects, which means that you can, for example, add type information to a function – 
#indicate the type of an argument the function accepts, or the type of the value it will return. Look at the following examples:

# No type information added:
def hello(name):
    return "Hello, " + name


# Type information added to a function:
def hello(name: str) -> str:
    return "Hello, " + name

#Type hinting is optional, which means PEP 484 does not obligate you to leave any static typing-related information in your code.
#The -> str annotation indicates, too, that the hello() function will return a value of type str, which of course is a string.

#1.4
#Docstrings – where and how?
#To be more precise – all public modules, functions, classes, and methods that are exported by a given module should have docstrings.
#docstrings are string literals that occur as the first statement in a module, function, class, or method.
#distinguish two kinds of such "extra dosctrings" – these are:

#attribute docstrings, which are located immediately after an assignment statement at the top level of a module (module attributes), class (class attributes), or the __init__ method definition of a class (instance attributes). 
#These are interpreted by the extraction tools, such as Docutils, as "the docstrings of the target of the assignment statement."
#additional dosctrings, which are located immediately after another docstring. 
#How to create docstrings
#Docstrings should be surrounded by triple double quotes ("""triple double quotes"""). For example:

def my_function():
    """I am a docstring."""
    ...


#If you need to use any backslashes in your docstrings, then you should follow the r"""raw triple double quotes""" format. 
#If you need to use Unicode docstrings, then follow the u"""Unicode triple-quote strings""" format.
#One-line vs. multi-line docstrings
#There are two forms of docstrings.
#one-line docstrings – they are used for simple and short descriptions, and should fit on one line;
#multi-line docstrings – they are used for more difficult cases, and should consist of a summary line followed by one blank line and a more elaborate description.
#One-line docstrings
#One-line docstrings should be used for rather simple, obvious, and short descriptions. They should take up one line only, and be surrounded by triple double quotes (the closing quotes should be on the same line as the opening quotes as this helps to keep the code clean and elegant).
#Important notes:

#a docstring should begin with an upper-case letter (unless an identifier begins the sentence) and end with a period;
#a docstring should prescribe the code segment's effect, not describe it. In other words, it should take the form of an imperative (e.g. "Do this", "Return that", "Compute this", "Convert that", etc.), not a description (e.g. "Does this", "Returns that", "Forms this", "Extends that", etc.).
def greeting(name):
    """Take a name and return its replicated form."""
    return name * 2

#a docstring should not just simply repeat the function or method parameters. 
def my_function(x, y):
    """Compute the angles and return a list of coordinates."""
...


#Do not use a blank line above or under a one-line docstring unless you're documenting a class, in which case you should put a blank line after all the docstrings that document it:
def calculate_tax(x, y):
    """I am a one-line docstring."""
    return (x+y) * 0.25

#Multi-line docstrings
Multi-line docstrings should be used for non-obvious cases and more detailed descriptions of code segments. They should have a summary line, similar to what a one-line docstring looks like, followed by a blank line and a more elaborate description. 
#The summary line may be located on the same line as the open triple double quotes, or put on the next line. The end quotes should be put on a separate line.
#Important notes:
#a multi-line docstring should be indented to the same level as the open quotes, for example:

def king_creator(name="Greg", ordinal="I", country="Neverland"):
    """Create a king following the article title naming convention.
    
    Keyword arguments:
    :arg name: the king's name (default: Greg)
    :type name: str
    :arg ordinal: Roman ordinal number (default: I)
    :type ordinal: str
    :arg country: the country ruled (default: Neverland)
    :type country: str
    """
    if name == "Voldemort":
        return "Voldemort is a reserved name."
    ...


#you should insert a blank line after all the multi-line docstrings that are documenting a class;
#class docstrings should also summarize its behavior as well as document the public methods and instance variables.
class Vehicle:
    """A class to represent a Vehicle.
    
    Attributes:
    -----------
    vehicle_type: str
        The type of the vehicle, e.g. a car.
    id_number: int
        The vehicle identification number.
    is_autonomous: bool
        self-driving -> True, not self-driving -> False

    
    Methods:
    --------
    report_location(lon=45.00, lat=90.00)
        Print the vehicle id number and its current location.
        (default longitude=45.00, default latitude=90.00)
    """
    
    def __init__(self, vehicle_type, id_number, is_autonomous=True):
        """
        Parameters:
        -----------
        vehicle_type: str
            The type of the vehicle, e.g. a car.
        id_number: int
            The vehicle identification number.
        is_autonomous: bool, optional
            self-driving -> True (default), not self-driving -> False
        """
        
        self.vehicle_type = vehicle_type
        self.id_number = id_number
        self.is_autonomous = is_autonomous
    
    def report_location(self, id_number, lon=45.00, lat=90.00):
        """
        Print the vehicle id number and its current location.
        
        Parameters:
        -----------
        id_number: int
            The vehicle identification number.
        lon: float, optional
            The vehicle's current longitude (default is 45.00)
        lat: float, optional
            The vehicle's current latitude (default is 90.00)
        """

    ...
    ...
    ...

#Docstring formatting types
#You may have noticed that we have used two different docstring formats for documenting the king_creator() function and the Vehicle class. The first type of formatting is called reStructuredText,
#The second example uses the NumPy/SciPy docstrings format,which is a combination of the Google docstrings format and the reStructuredText format.
#Both formatting types are good for the purposes of creating formal documentation, and both of them are supported by Sphinx, one of the most popular Python documentation generators.
#Sphinx is a great tool for creating documentation for software development projects. It uses reStructuredText as its markup language, and has a lot of useful features, such as supporting the HTML output format, automatic testing of code snippets, extensive cross-references, and a hierarchical structure, which lets you define a document tree. 

#1.6
#How to document a project
#Generally, a project should contain the following documentation elements:

#a readme, which provides a brief summary of the project, its purpose, and possibly some installation guidelines;
#an examples.py file, which is a script that demonstrates a few examples of how to utilize the project;
#a license in the form of a txt file (particularly important for Open Source and Public Domain projects)
#a how to contribute file which provides information about the possible ways of contributing to the project (shared, open source, and public domain projects).

#Linters and fixers
#what is a linter?
#it's a tool that helps you write your code, because it analyzes it for any stylistic anomalies and programming errors against a set of pre-defined rules. 
#The most popular linters are: Flake8, Pylint, Pyflakes, Pychecker, Mypy, and Pycodestyle (formerly Pep8) – the official linter tool to check Python code against PEP 8 conventions.
#A fixer, on the other hand, is a program that helps you fix these issues and format your code to be consistent with the adopted standards. The most popular fixers are: Black, YAPF, and autopep8.
#Most editors and IDEs (e.g. PyCharm, Spyder, Atom, Sublime Text, Visual Studio, Eclipse + PyDev, VIM, or Thonny) support linters, which means you can run them in the background as you write code. This makes it possible to detect, highlight, and identify many problem areas in your code, such as typos, wrong tabbing and indentation issues, function calls with the wrong number of arguments, stylistic inconsistencies, dangerous code patterns, and many more, 
#and automatically format your code to a pre-defined specification.

#1.7
#How to access docstrings
#We do it by using the Python __doc__ attribute – if any string literals are present after the definition of a function/module/class/method, then they are associated with the object as its __doc__ attribute, and this attribute provides the documentation of that object.
def my_fun(a, b):
    """The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.
    """
    return a*b

print(my_fun.__doc__)
>>
The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.

#But there's also another way to access the documentation strings – you can use the help() function. 
def my_fun(a, b):
    """The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.
    """
    return a*b

help(my_fun)
>>
Help on function my_fun in module __main__:

my_fun(a, b)
    The summary line goes here.
    
    A more elaborate description of the function.
    
    Parameters:
    a: int (description)
    b: int (description)
    
    Returns:
    int: Description of the return value.
