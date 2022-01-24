#Python Sets
#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
#Sets cannot have two items with the same value.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Get the Length of a Set
#To determine how many items a set has, use the len() method.
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set Items - Data Types
#Set items can be of any data type:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))


#The set() Constructor
#It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access Items
'''You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.'''

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#Add Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#Add Sets
#To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#Add Any Iterable
'''The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)




thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)




thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)



#Loop Items
#You can loop through the set items by using a for loop:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
#Join Sets
#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Keep All, But NOT the Duplicates
'''The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


#Set Methods
#Set add() Method
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#Set clear() Method

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

#Set copy() Method
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#Set difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#Set difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)


#Set discard() Method
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

#Set intersection() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#Set intersection_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# Set isdisjoint() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

#Set issubset() Method
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

#Set issuperset() Method
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

#Set pop() Method
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

#Set remove() Method
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)


#Set symmetric_difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#Set symmetric_difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#Set union() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)


#Set update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


