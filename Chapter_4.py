# List in Python.
l=["Apple","Mango",10, 34.5, False, "Arpita"]
print(l[0])
l[0]="Orange"
print(l)

# List slicing
print(l[1:4])
print(l[0:])

# append function in list
l.append("Ananya")
print(l)

# sort function in list
l1=[1,2,4,5,6,8,9,92,89]
l1.sort()
print(l1)

# reverse function in list
l1.reverse()
print(l1)

# insert function in list
l1.insert(3,45)
print(l1)

# pop function in list
l1.pop(3)
print(l1)
print(l1.pop()) # If you will not give any index than it will delete the last index of the list with the help of pop function in list.
print(l1) 

# Tuple 
# Tuple is immutable means you cannot change tuple elements.
a=(1,2,3,4,5)
print(type(a))

# Empty tuple
a=()
print(type(a))

# Simple element in tuple
a=(23,)
print(type(a))

p=("Arpita",45,78.09,True)
r=p*3
print(r)
n=p.count(45)
print(n)
x=p.index(45)
print(x)
# Length of the tuple.
print(len(p))

# Practice Set of Chapter-4
# Write a program to store seven fruits in a list entered by the user.
fruits=[]
f1=input("Enter fruit name:")
fruits.append(f1)
f2=input("Enter fruit name:")
fruits.append(f2)
f3=input("Enter fruit name:")
fruits.append(f3)
f3=input("Enter fruit name:")
fruits.append(f3)
f4=input("Enter fruit name:")
fruits.append(f4)
f5=input("Enter fruit name:")
fruits.append(f5)
f6=input("Enter fruit name:")
fruits.append(f6)
f7=input("Enter fruit name:")
fruits.append(f7)
print(fruits)

# Write a program to accept marks of students and display them in a stored manner.
marks=[]
m1=int(input("Enter mark here: "))
marks.append(m1)
m2=int(input("Enter mark here: "))
marks.append(m2)
m3=int(input("Enter mark here: "))
marks.append(m3)
m4=int(input("Enter mark here: "))
marks.append(m4)
m5=int(input("Enter mark here: "))
marks.append(m5)
m6=int(input("Enter mark here: "))
marks.append(m6)
marks.sort()
print(marks)

# Check that a tuple cannot be changed in Python.
'''a=(12,True,"Arpita")
a[2]="Ananya"
print(a)

It will give error like this because tuple cannot be changed because it is immutable.
    a[2]="Ananya"
    ~^^^
TypeError: 'tuple' object does not support item assignment
'''

# Write a program to sum a list with 4 number.
l=[20,10,30,40]
print(sum(l))

# Write a program to count the number of zeros in the following tuple:
a=(7,0,8,0,0,9)
c=a.count(0)
print(c)