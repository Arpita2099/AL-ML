# Conditional Expression

# IF ELSE AND ELIF in Python
age=int(input("Enter your age: "))
if (age>=18):
    print("You are eligible to Vote and to get driving licence.")

num1=int(input("Enter any number: "))
num2=int(input("Enter any number: "))
if(num1>num2):
    print(f"{num1} is greater number.")
else:
    print(f"{num2} is greater number.")

marks=int(input("Enter your marks: "))
if marks>=90:
    print("A+")
elif marks>80:
    print("A")
elif marks>70:
    print("B+")
elif marks>60:
    print("B")
elif marks>50:
    print('C+')
elif marks>40:
    print("C")
else:
    print("Failed")

# Practice Set of Chapter-6
# Write a program to find the greater of four numbers entered by the user.
num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
num3=int(input("Enter number: "))
num4=int(input("Enter number: "))
if (num1>num2 and num1>num3 and num1>num4):
    print(f"{num1} is greater number.")
elif (num2>num3 and num2>num4):
    print(f"{num2} is greater number.")
elif (num3>num4):
    print(f"{num3} is greater number.")
else:
    print(f"{num4} is greater number.")

# Write a program to find out whether a student has passed or failed if it required total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
mark1=int(input("Enter mark of English in percentage: "))
mark2=int(input("Enter mark of Math in percentage: "))
mark3=int(input("Enter mark of Science in percentage: "))
total_percentage=(100*(mark1+mark2+mark3))/300
if(mark1>=33 and mark2>=33 and mark3>=33 and total_percentage>=40):
    print("You are Passed.")
else:
    print("Your are Failed.")


# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now","subscribe this", "click this". Write a program to detect these spams.
p1="Make a lot of money" 
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("Enter your comment: ")
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This comment is a spam.")
else:
    print("This comment is Safe.")


#  Write a program to find whether a given username contains less than 10 characters or not.
username=input("Enter the user name: ")
if (len(username)<10):
    print("Your username contain less than 10 character.")
else:
    print("Your username contain more  than 10 character.")

# Write a program which finds out whether a given name is present in a list or not.
l=["Arpita","Sabana","Anaya","Ananya","Pinky"]
name=input("Enter your name: ")
if(name in l) or (name.capitalize() in l.capitalize()) or (name.lower in l.lower()) or (name.upper in l.upper()):
    print("Your name is in the list.")
else:
    print("Your name is not in the list.")

# Writw a program to calculate the grade of student from his marks from the following scheme:
# 90-100=EX
# 80-90=A
# 70-80=B
# 60-70=C
# 50-60=D
# <50=F
mark=int(input("Enter your mark: "))
if(mark>=90 and mark<=100):
    grade="Excellent!"
elif(mark>=80 and mark<90):
    grade="A"
elif(mark>=70 and mark<80):
    grade="B"
elif(mark>=60 and mark<70):
    grade="C"
elif(mark>=50 and mark<60):
    grade="D"
elif (mark<50):
    grade="F"

print("Your grade is: ",grade)


# Write a program to find out whether a given post is talking about "Arpita"  or not. 
post="Hey, I am Arpita. I am here to do coding."
if("Arpita".lower() in post.lower() or "Arpita".upper() in post.upper() or "Arpita".capitalize() in post.capitalize()):
    print("This post is talking about Arpita.")
else:
    print("This post is not talking about Arpita.")
