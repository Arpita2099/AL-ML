# This chapter will explain about the variable and data type in the Python.
# Variable: Variable is simple a kind of container where we store different value. For instance,
a=5
b=10
print(a+b)

x="Arpita"
Y="Sah"
print(x)
print(Y)

# Data Types in the Python
# Primarily these are the following data types in the Python.
# Integer
c=78
d=2
print("The multiplication of two integer:",c*d)

# Floating point numbers
p=1.5
q=5.5
print("The sum of two float number:",p+q)

# String
r="Hello"
s="World"
print("This is the string types of data type:",r+s)

# Boolen
print("This is the Boolen types of the data type",True)
print(False)

# None
print("This is none types of the data type:",None)

# There are some of the rules for defining variable name and they are:
# A variable name can contain alphabets, digits, and underscores.
# A variable name can only start with an alphabet and underscores.
# A variable name can't start with a digit.
# No while space is allowed to be used inside a variable name.
# Examples of a few variable names are : arpita, one5, one_only, etc.

# Operators in the Python:
# Arithmetic operators: +, -, *, /, etc.
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Assignment operators: =, +=, -=, etc.
p=10-8
print("p=",p)
q=9
p+=6
print("p=",p)

# Comparison operators:==,>,<,>=,<=,etc.
a=9
b=10
print(a==b)
print(a>b)
print(b>=a)
print(a<=b)
print(a<b)
print(a!=b)

# Logical operators: and, or, not.
t=True and True
print(t)
f=True and False
print(f)
a=not True
print(a)
b=True or False
print(a)

# Type() function and typecasting in the Python.
# type() function is used to find the data type of given variable in the python.
# For instance,
z=30
print(type(z)) # It will provide the data type of z as a integer.

# And by using the type() function you can find out the data types of any variables in the pytjon.
a=45.8
print(type(a)) # It will give the data type float.

s="Arpita"
print(type(s)) # It will give the data type string
print(type(True)) # It will give the data type boolen.

# Typecasting in the Python.
a=31.8
print(type(int(a)))
print(a)

a="32.8"
print(type(float(a)))

# Input function in the Python.
a=input("Enter first number:")
b=input("Enter second number: ")
print("The first number is: ",a)
print("The secon number is: ",b)
print(a+b)
# In this above input program you can see that only giving then input to any variable than it will take input as string so while doing the addition of 1 and twi it will return 12 rather than 3 because it will add the  two string not the integer though you have given the integer. So, to make it integer you have to give int before integer. For instance,
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
sum=num1+num2
print("The sum of two number is: ",sum)
# So, in this way you can take input in the python programming language.

# Now, come to the chapter two practice set.

# Write a python program to add two numbers.
a=12
b=13
print("Add two number is: ", a+b)

# Write a python program to find remainder when a number is divided by 2.
num=23
print("Remander of number divided by 2: ",num%2==0)

# Check the type of variable assigned using input() function.
s=input("Enter any thing: ")
print(type(s))

# Use comparison operator to find out whether a given variable a is greater than b or not. Take, a=34 and b=80.
a=34
b=80
print(a>b)

# Write a Python Program to find an average of two numbers entered by the user.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
sum=num1+num2
avg=sum/2
print("The average of two numbers is: ",avg)

# Write a python program to calculate the square of a number entered by the user.
number=int(input("Enter any number: "))
print("The square of number is: ",number**2)
