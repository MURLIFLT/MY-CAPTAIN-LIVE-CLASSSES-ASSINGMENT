#Python Lists
#List
thislist = ["murli", "branch:cseaiml", "2nd year"]
print(thislist)

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:
thislist = ["rohan", "manish ", "rohan", "saniya", "rahul"]
print(thislist)

#List Length
#To determine how many items a list has, use the len() function:
thislist = ["java", "liitle", "php","html"]
print(len(thislist))

#List Items - Data Types
#List items can be of any data type:
list1 = ["rohan", "moon", "tom"]
list2 = [100, 50, 75, 99, 39]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

#A list can contain different data types:
list1 = ["murli", 20, True,  "male"]

print(list1)

#type()
#From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["mohali", "dubai"]
print(type(mylist))

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list
thislist = list(("dubai", "mohali", "pune"))
print(thislist)

#Access Items
#List items are indexed and you can access them by referring to the index number:
thislist = ["mohan", "mohit", "mohika"]
print(thislist[2])

#Negative Indexing
thislist = ["shravan", "kannika", "suvan"]
print(thislist[-2])

""""Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items."""
thislist = ["bunty", "kancha", "suman", "shravan", "suvan", "mohika", "kannika"]
print(thislist[4:5])

thislist = ["mohika", "suvan", "suman", "shravan", "mohika", "bunty", "kancha"]
print(thislist[:4])

thislist = ["mohika", "suman", "mohit", "kannika", "omkar", "bunty", "shravan"]
print(thislist[2:])

'''Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:'''
thislist = ["VEDIKA", "MURLI", "YUG", "SUMO", "ADIL", "HANZU", "AYUSH"]
print(thislist[-4:-1])

'''Check if Item Exists
To determine if a specified item is present in a list use the in keyword'''
thislist = ["vedika", "eshita", "aditi"]
if "eshita" in thislist:
  print("Yes, 'eshita' is in the fruits list")
  
 # Python - Change List Items
#Change Item Value
thislist = ["MOHIKA", "SUMO", "SUMAN"]
thislist[1] = "VEDIKA"
print(thislist)


'''Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:'''

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["MOHIT", "KANNIKA"]
print(thislist)

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["suman"]
print(thislist)

'''Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.'''

#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "mohika")
print(thislist)

 #Add List Items
#Append Items
#to add an item to the end of the list, use the append() method:


#Using the append() method to append an item:

thislist = ["apple", "murli", "cherry"]
thislist.append("murlination")
print(thislist)


'''Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:'''


thislist = ["shravan", "banana", "cherry"]
thislist.insert(1, "suman")

'''Extend List
To append elements from another list to the current list, use the extend() method'''

#Add the elements of tropical to thislist:

thislist = ["apple", "suman", "cherry"]
tropical = ["mohika", "pineapple", "suvan"]
thislist.extend(tropical)
print(thislist)

'''Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).'''


#Add elements of a tuple to a list:

thislist = ["apple", "ironman", "cherry"]
thistuple = ("kiwi", "captain")
thislist.extend(thistuple)
print(thislist)



'''Remove List Items
Remove Specified Item
The remove() method removes the specified item.'''

thislist = ["apple", "vikram", "cherry"]
thislist.remove("vikram")
print(thislist)
print(thislist)



#The pop() method removes the specified

thislist = ["suman", "vikram", "shravan"]
thislist.pop(1)
print(thislist)

#The del keyword also removes the specified index:

thislist = ["apple", "ayush", "sakshi"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#note
thislist = ["apple", "banana", "cherry"]
del thislist
print("thislist")#this will cause an error because you have succsesfully deleted "thislist".



'''Clear the List
The clear() method empties the list.

The list still remains, but it has no content.'''


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Loop Lists
#Loop Through a List
#You can loop through the list items by using a for loop:


thislist = ["salman", "srk", "akki"]
for x in thislist:
  print(x)
  
''' Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.'''



thislist = ["murli", "manish", "varun"]
for i in range(len(thislist)):
  print(thislist[i])


'''Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.'''


#Print all items, using a while loop to go through all the index numbers

thislist = ["omkar", "suraj", "manohar"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


'''Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:'''

#A short hand for loop that will print all items in a list:

thislist = ["sakshi", "sam", "adil"]
[print(x) for x in thislist]


'''List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.'''


'''Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

'''Condition
The condition is like a filter that only accepts the items that valuate to True.'''
fruits = ["apple", "mohan", "shubhu", "kajal", "mausam"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

#Iterable
newlist = [x for x in range(22)]

print(newlist)

#Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]

print(newlist)

'''Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:'''
fruits = ["apple", "amrut", "mosambi", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

'''The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)


'''Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Sort the list alphabetically:'''

thislist = ["nobita", "hattori", "turing", "thor", "hulk"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


'''Sort Descending
To sort descending, use the keyword argument reverse = True:'''


#Sort the list descending:

thislist = ["java", "kaju", "cpp", "c", "dbms"]
thislist.sort(reverse = True)
print(thislist)


#Sort the list descending:

thislist = [200, 560, 658, 827, 203]
thislist.sort(reverse = True)
print(thislist)


'''Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):'''

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


'''Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:'''

thislist = ["raju", "sham", "riya", "baburao"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


'''Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.'''
#Reverse the order of the list items:

thislist = ["murli", "muls", "mu", "mui"]
thislist.reverse()
print(thislist)



'''Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().'''
#Make a copy of a list with the copy() method:

thislist = ["kk", "moh", "mohika"]
mylist = thislist.copy()
print(mylist)

'''Another way to make a copy is to use the built-in method list().
Make a copy of a list with the list() method:'''

thislist = ["jubin", "neha", "badsha"]
mylist = list(thislist)
print(mylist)



'''Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.'''
#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# you can use the extend() method, which purpose is to add elements from one list to another list:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# List append() Method
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

a = ["activa", "rangerover", "tata"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)


#List clear() Method
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)

#List copy() Method

fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)


#List count() Method

fruits = ["apple", "banana", "cherry"]

x = fruits.count("banana")

print(x)

fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = fruits.count(4)

print(x)


#List extend() Method
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)


#List index() Method
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)

print(x)


#List insert() Method
avengers = ['ironman', 'captain', 'thor']

avengers.insert(1, "hulk")

print(avengers)

#List pop() Method
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)


#emove() Method

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)


#List reverse() Method

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

# List sort() Method

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)


cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)


def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)



# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)


