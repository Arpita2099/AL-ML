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
