print("Hello World!")# This is m first step of codding in the python.
# In the python we save file as .py

# How does pip work: With the help of pip you can install any kind of module.
# We can install pip my writting pip install name_of_module.
# And after import you can get module intslled in your code.
import pyjokes
joke=pyjokes.get_joke()
print(joke)
# Pyjokes is ther module to print the jokes.

# As a calculator how you can use Python.
# In the terminal you can use Python as a calculator. 
# Steps are:
# First open the terminal and type Python3 and enter
# And you can write what you want to print then you can the output.

# Now taking about the comment in the Python.
# With the help of # you can add the comment in the Python and you can see example of comment in the python above.
#Also the shortcut key to print the comment is ctrl+forward slace.

# Some time we need to have the multi line comment and you can do by using """""". For instance,
"""
Hey!!
I am Arpita here.
Now I am doing coding in Python.
Help and motivate for coding in the Python.
"""
# So this is all about the comment in the Python.

# Now, moving towards the chapter-1 practise Set.
# Write a program to print the twinkle twinkle little star.....
print("""
    Twinkle, twinkle, little star,
    How I wonder what you are!
    Up above a world so high,
    Like a diamond in the sky.
      
    When the blazing sun is gone,
    When he nothing shines upon,
    when you show your little light,
    Twinkle, twinkle, all the night.
      
    Then the trav'ller in the darks,
    Thanks you for your tiny spark,
    He could not see which way to go,
    If you did not twinkle so.
      
    In the dark blue sky you keep,
    And often though my curtains peep,
    For you never shut your eye,
    Till the sun is in the sky.
      
    'Tis your bright and tiny spark,
    Lights the trav'ller in the dark,
    Tho I know not what you are,
    Twinkle, twinkle, little star.
""")
# Even with the help of triple double code and single code you can aslo print out the multiple lines in the print as you can see the example above how I used this to print the multiple lines poem in the print() function of the Python.

# Install an external module and perform an operation of your interest.
# Here I am going to install module pyttsx3 using the pip install.
# And here the way to go for it:
import pyttsx3 # This module will speak what I have written.
engine=pyttsx3.init()
engine.say("Hey, I am Arpita Sah. And I am here to docoding in the Python. And today, it's my first day i started coding in Python with the help of the youtube video of code with Harry. And I found it very interesting to continue my python learning with the youtube channel code with harry. And hope so, I will achive what I want in my life. Thank You!!!")
engine.runAndWait()

# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
import os

def print_directory_contents(path="."):# you can also write / in the place of .
    # Example 2: List a specific directory
    # Replace '/path/to/directory' with the actual directory path
    # print_directory_contents("/path/to/directory")
    """
    Print the names of files and directories in the given path.
    If no path is provided, it uses the current working directory.
    """
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Example 1: List current directory
    print_directory_contents()

import os
# Specify the directory you want to list.
directory_path='/'

# List all the files and directories in the specified path
contents= os.listdir(directory_path)

# Printeach file and directory name
for item in contents:
    print(item)


