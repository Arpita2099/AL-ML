# Functions and Recursions

# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number.

# Syntax of function.
'''
def function():
    print("Hello Ji!")
This function can be called any number of times, anywhere in the program.
'''

# Function call
'''
Whenever we want to call a function, we put the name of the function followed by parentheses as following:
func()
'''

# Function Definition
'''
The part containing the exact set of instruction which are executed during the function call.
'''

#Types of Function:
'''
1. Built-in Functions (Already present in Python)
Examples of built-in functions includes len(), print(), range(), etc.
2. User define  function (Defined by the user)
Th efunction define by the user.
'''

# Average of three number.
# Function Definition
def avg():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    c=int(input("Enter a number: "))
    average=(a+b+c)/3
    print(average)
avg() # Function Call

# Write a program to greet a user with "Good day" using functions.
user=input("Enter your Name: ")
def good_day():
    print("Good Day",user)
good_day()
good_day()

# Functions with Argument.
'''
A function can accept some value it can work with. We can put these values in the parentheses.
A function can also return value as shown below:
'''
# For instance,
def good_day(name, ending):
    print("Good Day,"+name)
    print(ending)
good_day("Arpita", "Thank You")
good_day("Anaya", "Thank You")
good_day("Sabana", "Thanks")
