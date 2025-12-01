# Loop in Python
for i in range(1,6):
    print(i)

# Types of Loop
# While Loop
# In while loop, the condition is checked first. If it evaluated to true, the body of the loop is executed otherwise not!
# If the loopis entered, the process of [condition check & execution] is continued until the condition become False.
# Syntax of while loop.
'''
while(condition): # The block keeps executing until the condition is true 
    # Body of the loop
'''
# For instance, Write a program to print 1 to 50 using while loop.
'''i=1
while i<51:
    print(i)
    i=i+1 '''

i=0
while i<5:
    print("Arpita Sah")
    i+=1

# Write a program to print the content of list using while loop.
i=0
l=[1,3,4,5,6,9]
while i<len(l):
    print(l[i])
    i+=1

# For Loop
# A for loop is used to literate through a sequence like list, tuple, or string[iterables].
# Syntax of For loop:
''''
l=[1,3,5,6]
for item in l:
    print(item) # It will prints 1,3,5 and 6
'''

# Range function in Python.
# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop, and step-size as follows:
# Syntax:
'''
range(start,stop,steps_ize)
# step_size is usually not used with range()
'''
# For instance,
for i in range(2,20,2):
    print(i)

# For loop with else:
for i in range(1, 20):
    if i%2==0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")

# How to print the content of list using for loop.
l=[1,4,8,12,16,20]
for i in l:
    print(i)

# How to print the content of tuple using for loop.
t=(1,3,5,7,9,11)
for i in t:
    print(i)

# How to print the content of set using for loop.
s={2,4,6,8,10,12}
for i in s:
    print(i)

# How to iterate the string using for loop.
str="Arpita"
for i in str:
    print(i)

# Break statement in Python
for i in range(100):
    if i==30:
        break # Exit the loop now.
    print(i)

# Continue statement in Python
for i in range(10):
    if i==7:
        continue # Skip the iteration.
    print(i)

# Pass Statement in Python
for i in range(1,34,8):
    pass # Pass is a null statement in Python. It instructs to "do nothing"

# Practice Set of Chapter-7
# Write a program to print multiplication table of a given number using loop.
# Using while loop
i=1
n=32
while i<11:
    print(n,"*",i,"=",n*i)
    i=i+1
print("Using for loop for multiplication of tables")
# Using for loop
n=16
for i in range(1,11):
    print(n,"*",i,"=",n*i)

# Write a program to greet all the person name stored in a list "l" and which starts with S.
l=["Amar","Sohan","Sachin","Rahul"]
for i in l:
    print(f"Good Morning!{i}")

# Attempt problem 1 using while loop.
# Using while loop
i=1
n=32
while i<11:
    print(n,"*",i,"=",n*i)
    i=i+1

# Write a program to find the sum of first n natural number using while loop.
sum=0
i=1
n=int(input("Enter a number: "))
while i<=n:
    sum=sum+i
    i+=1
print(f"Sum of {n} natural number is {sum}")

# Write a program to calculate the factorial of a given number using loop.
f=1
n=int(input("Enter a number: "))
print("Factorial number is: ")
for i in range(1,n+1):
    f=f*i
print(f"Factorial of {n} is:{f}")

# Write a program to print multiplication table of n using for loops in reversed order.
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n,"*",11-i,"=",n*(11-i))