# Dictionary in Python Programming.
# Dictionary is a collection of keys-value pairs.
# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.

marks={
    "Arpita":99,
    "Sabana":100,
    "Pinky":100
}
print(marks)
print(type(marks))
print(marks["Arpita"])

# Method of Dictonary
# items(): Returns a list of (key, value) tuples.
print(marks.items())
# keys(): Return a list containing dictionary's keys.
print(marks.keys())
# keys(): Return a list containing dictionary's values.
print(marks.values())
# update(): Updates the dictionary with supplied key-value pairs.
marks.update({"Pinky":99})
print(marks)
# get(): Returns the value of the specified keys (and value is returned).
print(marks.get("Sabana"))

# Differences betweeen these two:
print(marks.get("Sabana")) # If this does not have this keys than it will return none
print(marks["Sabana"]) # While, it will return the error.
# So, this is the difference between the above.

# Set in Python.
# Set is a collection of non-repetitive elements.
# Sets are unordered.
# Sets are unindexed.
# There is no way to change items in sets.
# Sets cannot contain duplicate value.

s={1,5,10,15,20}
print(type(s))

# For making the empty set.
a=set() # Don't use s={} as it will create an empty dictionary.
print(type(a))

# Sets cannot contain duplicate value.
s={1,2,3,4,4,4,2,1,5}
print(s)

s={"Arpita", True, 12, 45,90}
print(type(s))

# add() function in set.
s.add(6)
print(s,type(s))

# Finding the length of the set.
print(len(s))

# remove(): Updates the set s and remove the given value from s.
s.remove(True)
print(s)

# pop(): Remove an library element from the set and return the element removed.
s.remove(45)
print(s)

# clear(): empties the set.
s.clear()
print(s)

# union(): Returns a new set with all items from both sets.
a={1,2,3,4,5}
b={2,4,6,8,10}
u=a.union(b)
print(u)

# intersection(): Returns a set which contains only item in both sets.
i=a.intersection(b)
print(i)

# Practice set of Chapter-5
# Write a program to create a dictionary of Nepali words with values as their English translation. Provide user with an option to look it up!
Translate={
    "Bhat":"Rice",
    "Dahi":"Curd",
    "Chini":"Sugar"
}
print(Translate)
print(type(Translate))

# Write a program to input eight numbers from the user and display all the unique numbers(once).
s=set()
n=input("Enter number 1: ")
s.add(int(n))
n2=input("Enter number 2: ")
s.add(int(n2))
n3=input("Enter number 3: ")
s.add(int(n3))
n4=input("Enter number 4: ")
s.add(int(n4))
n5=input("Enter number 5: ")
s.add(int(n5))
n6=input("Enter number 6: ")
s.add(int(n6))
n7=input("Enter number 7: ")
s.add(int(n7))
n8=input("Enter number 8: ")
s.add(int(n8))
print(s)

# Can we have set with 18(int) and  '18'(str) 12as value in it?
# Yes we can. For instance,
s={18,'18'}
print(s,type(s))

# What will be the length of following set s:
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))