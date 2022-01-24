#step funtion in for loop
for x in range(0, 12, 2):
  print(x)


# add the values in tuples
ekdvs2 = ("suman","","devika","kanchan","anish","sahib")
p_l = list(ekdvs2)
p_l.append("shravan")
ekdvs2 = tuple(p_l)
print(ekdvs2)


# We can create an infinite loop using while statement. If the condition of while loop is always True
#we get an infinite loop.
while True:
   num = int(input("Enter an integer: "))
   print("The double of",num,"is",2 * num)