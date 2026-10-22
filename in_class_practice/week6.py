'''def <function_name>(arg/perimeter list):
    pass
    positional (list order matters)

def get_name(first_name, last_name):
full_name = get_name(first_name, last_name)

Variable scope: The scope of a variable refers to the region of the code where the variable is accessible. In Python, variables can have different scopes, such as local, global, and nonlocal. Local variables are defined within a function and can only be accessed within that function. Global variables are defined outside of any function and can be accessed from anywhere in the code. Nonlocal variables are used in nested functions to refer to variables in the enclosing scope.

#global scope
global_variable = "I am the very model of a global variable"

def my_funk():
    #local scope
    local_variable = "I can't be seen outside of this function"
    print(local_variable)
    print(global_variable)

def greet(name, message):
    print(message, name)

greet(message="Hello", name="Alice")  # Using keyword arguments

python transformer.py --action upper --data"hello,world,python"

"first-name,last-name".split(",") #token/delimiter
["first-name", "last-name"]

#html<body> this would be a tokenizer for html tags, but it would be a bit more complex than just splitting on the < and > characters. You would need to account for attributes and nested tags as well.

#sys is a module in Python that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It allows you to access command-line arguments, manipulate the Python runtime environment, and perform various system-level operations.
import sys

print("Total arguments:", len(sys.argv))
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

total =0

for arg in
    sys.argv[1:]: 
        total +=int(arg)
print("Sum =", total)
#Argparse is a module in Python that provides a way to handle command-line arguments passed to a script. It allows you to define the expected arguments, their types, and help messages, making it easier to create user-friendly command-line interfaces.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help="Show output message")
#add different argument
parser.add_argument("-d", "--datestamp", action="store_true", help="Show datestamp")
args = parser.parse_args()

if args.Output:
    #print("Output:", args.Output)
    pass
if args.datestamp:
    #print("Datestamp:", args.datestamp)
    pass

python transformer.py --action upper --data "hello,world,python"

parser.add_argument("-a", "--action", required=True, help="transformer action upper | lower | title")
parser.add_argument("-d", "--data", required=True, help="Data to transform")

args = parser.parse_args()

if args.action:
    print(f"Action: {args.action}")
if args.data:
    print(f"Data: {args.data}")'''

