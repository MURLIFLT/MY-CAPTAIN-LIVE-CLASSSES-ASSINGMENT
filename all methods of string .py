#Python Strings
#You can use double or single quotes:

print("Hello")
print('Hello')

#Assign String to a Variable
a = "Hello"
print(a)

#Multiline Strings
a = """welcome to goa"""
print(a)

#Or three single quotes
a = '''welcome to patna.'''
print(a)

'''Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.'''

a = "Hello, World!"
print(a[5])

'''Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.'''


for x in "cpu":
  print(x)
  
'''  String Length
To get the length of a string, use the len() function.'''


a = "Hello, World!"
print(len(a))


'''Check String
To check if a certain phrase or character is present in a string, we can use the keyword in.'''


txt = "The best things in life are free!"
print("free" in txt)

#Use it in an if statement:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
'''Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.'''

'''txt = "The best things in life are free!"
print("expensive" not in txt)'''


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Python - Slicing Strings

b = "Hello, World!"
print(b[2:5])


'''Slice From the Start
By leaving out the start index, the range will start at the first character:'''

b = "Hello, World!"
print(b[:5])

'''Slice To the End
By leaving out the end index, the range will go to the end:'''
b = "Hello, World!"
print(b[2:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

#Python - Modify Strings
#Upper Case

a = "Hello, guys!"
print(a.upper())

#Lower Case
a = "Hello, friends!"
print(a.lower())

'''Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.'''
a = " Hello, chiiti! "
print(a.strip()) 

#Replace String

a = "Hello, boy!"
print(a.replace("H", "J"))

'''Split String
The split() method returns a list where the text between the specified separator becomes the list items.'''


a = "Hello, mumbai!"
print(a.split(",")) 

'''String Concatenation
To concatenate, or combine, two strings you can use the + operator.'''

a = "Hello"
b = "prerna"
c = a + b
print(c)

a = "hello"
b = "saniya"
c = a + " " + b
print(c)

#String Format
age = 20
txt = "My name is murli, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape Characters

txt = "We are  \"playing\" hockey."
print(txt)

#\'	Single Quote
txt = 'It\'s alright.'
print(txt) 

#\\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt) 

#\n	New Line
txt = "Hello\nWorld!"
print(txt) 

#\r	Carriage Return
txt = "Hello\rWorld!"
print(txt) 


#\t	Tab
txt = "Hello\tWorld!"
print(txt) 

#\b	Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#\ooo	Octal value
txt = "\110\145\154\154\157"
print(txt) 

#\xhh	Hex value	
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 


#String Methods
# String capitalize() Method
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#String casefold() Method
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

#String center() Method

txt = "banana"

x = txt.center(20)

print(x)

#String count() Method
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


#String encode() Method


txt = "My name is Ståle"

x = txt.encode()

print(x)

#String endswith() Method
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

#String expandtabs() Method
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

#String find() Method

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#String format() Method
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#String index() Method
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#String isalnum() Method
txt = "Company12"

x = txt.isalnum()

print(x)

#String isalpha() Method
txt = "CompanyX"

x = txt.isalpha()

print(x)

#String isascii() Method
txt = "Company123"

x = txt.isascii()

print(x)

#String isdigit() Method
txt = "50800"

x = txt.isdigit()

print(x)

 #String isidentifier() Method
txt = "Demo"

x = txt.isidentifier()

print(x)


#String islower() Method
txt = "hello world!"

x = txt.islower()

print(x)

#String islower() Method

txt = "hello world!"

x = txt.islower()

print(x)


 #String isnumeric() Method
txt = "565543"

x = txt.isnumeric()

print(x)

#String isprintable() Method
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

#String isspace() Method
txt = "   "

x = txt.isspace()

print(x)

#String istitle() Method
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

#String isupper() Method
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#String join() Method
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#String ljust() Method
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

#String lower() Method
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#String lstrip() Method
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#String lstrip() Method
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#String maketrans() Method
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


#String partition() Method

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

#String replace() Method
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#String rfind() Method
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)


 #String rindex() Method
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

#String rjust() Method
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

#String rpartition() Method
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

#String rsplit() Method
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

#String rstrip() Method
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")


#String split() Method
txt = "welcome to the jungle"

x = txt.split()

print(x)

#String splitlines() Method
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

#String startswith() Method
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#String strip() Method
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#String swapcase() Method
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#String title() Method

txt = "Welcome to my world"

x = txt.title()

print(x)

#String title() Method
txt = "Welcome to my world"

x = txt.title()

print(x)

#String translate() Method
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


#String upper() Method
txt = "Hello my friends"

x = txt.upper()

print(x)


#String zfill() Method
txt = "50"

x = txt.zfill(10)

print(x)




