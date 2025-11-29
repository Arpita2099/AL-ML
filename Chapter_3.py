# String in the Python Programming language.
# String is the data type, sequence of character.
# String is immutable.

# Strint can be printed by this way.
name='Arpita Sah'
Quote="This's me doing nothing."
what="""Hey,
I am here.
Where are you.
Am I know that you are near by me.
"""
print(name)
print(Quote)
print(what)

# How to do slicing in the string.
# Positive slicing in string of python.
nameslicing=name[0]
print(nameslicing)
print(name[0:6])
print(name[:6])

# Negative slicing the string of Python.
print(name[-1])
print(name[-4:-1])
print(name[-4:])

# Slicing with skip value in the string of Python.
# We can provide a skip value as a part of our slice like this:
print(name[0:6:2]) # Apt

# Some of the function of string in python:
# How to get the length of the string.
print(len(name))

# .endswith() function in string of python.
print(name.endswith("ah")) # True
print(name.endswith("ha")) # False

# .count() function in string of python.
print(name.count("a"))

#.startswith() function in string of python.
print(name.startswith('A')) # True
print(name.startswith('a')) # False

#.capitalize() function in string of python.
print(name.capitalize())

#.title() function in string of python.
print(name.title())

# .find() function in string of python.
print(name.find("a"))

# .lower() function in string of python.
print(name.lower())

# .upper() function in string of python.
print(name.upper())

# .replace function in string of python.
print(name.replace("Arpita","Ananya"))

# Escape sequence characters
# Sequence of the character after backslash "\" -Escape Sequence character.
# Escape Sequence characters comparise of more than one character but represent one character when used within the string.
# For instance; \n-newline, \t-tab, \;-singlequote, \ \-backslash, etc.
s="Arpita is very funny girl \nBut not a bad girl."
print(s)
a="Arpita is very funny girl \nBut not a bad \"girl\"."
print(a)

# Practice Set of Chapter-3
# Wite a python program to display a user entered name followed by Good Afternoon using input() function.
name=input("Enter your name: ")
print(f"Good Afternoon {name}.")

# Write a program to fill in a letter template given below with name and data.
letter='''Dear <|Name|>,
        You are selected!
        <|Date|>
'''
print(letter.replace("<|Name|>", "Arpita Sah").replace("<|Date|>","5 December 2025"))

# Write a program to detect double space in a string.
s="I  am  very honest  Girl."
print(s.find("  "))

# Replace the double space from problem 3 with single spaces.
print(s.replace("  "," "))

# Write a program to format the following letter using escape sequence characters.
# Letter="Dear Arpita, this python course is nice. Thanks!"
print(f"Dear Arpita,\nthis python course is nice.\nThanks!") 

