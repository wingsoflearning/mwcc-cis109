#Importing modules in Python
#import (name of the module) as (name you want to use in your code)

#From is the keyword used to import specific functions or classes from a module. It allows you to access only the required components of a module, rather than importing the entire module.
#from (name of the module) import (name of the function) as (name you want to use in your code)

#Main Entry Point: The main entry point of a Python program is the point where the program starts executing. It is typically defined by the `if __name__ == "__main__":` statement, which allows you to specify code that should only run when the script is executed directly, rather than when it is imported as a module.
def main():
    print("Hello World")

if __name__ == "__main__":
    main()

#Getting Help: In Python, you can get help on modules, functions, and classes using the built-in `help()` function. For example, calling `help(str)` will provide information about the string class and its methods. You can also use the `dir()` function to list the attributes and methods of an object or module.
help(str)

#built in modules: Python comes with a standard library of built-in modules that provide various functionalities, such as math, random, datetime, and more. You can import and use these modules in your code to perform specific tasks without having to write the code from scratch.
datetime (Basic date and time types)
math (Mathematical functions)
os (Miscellaneous operating system interfaces)
random (Generate pseudo-random numbers)
sys (System-specific parameters and functions)
zipfile (Read and write ZIP files)

#Third party modules: Third-party modules are external libraries or packages that are not included in the Python standard library. They can be installed using package managers like pip and provide additional functionality for various tasks, such as web development, data analysis, machine learning, and more. Examples of popular third-party modules include NumPy, Pandas, Requests, Flask, and Django.
numpy (Numerical computing)
pandas (Data manipulation and analysis)
pytest (Testing framework)
requests (HTTP library, interface with restful APIs)

#before using third-party modules, you need to install them using pip. You can do this by running the command `pip install <module_name>` in your terminal or command prompt. Once installed, you can import and use the module in your Python code.

pip install 

username: email.hotmail.com
