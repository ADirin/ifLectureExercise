# Lecture assignment1 Try the following code:
x = 1
print(x != 2)
print(x != 1)

# Lecture assignment1 Try the following code:
a = 1
b = 2
print("does a == b? What result do you get")
# print(a==b)

a = b
print("does a == b? What result do you get")
# print(a==b)

# Lecture assignment 3
print("the results for: ", 1 < 2 and 3 < 4)
print("the results for: ", 1 > 2 or 3 < 4)

# Lecture assignment 4
a = 2
b = 2
if a + b == 4:
    print("2+2 is 4")
    print("arithmetic works")

# Does the code ever execute else statment?
if a + b == 4:
    print("2+2 is 4")
    print("arithmetic works")
else:
    print("2 and 2 is not 4")
    print("Big Brother wins.")

#Lecture assignment 5
num = 15
if num < 10:
 print ("number is less than 10")
elif num > 10:
 print ("number is greater than 10")
else:
 print ("number is equal to 10")

# Lecture assignment 6
want_cake = str(input("do you want cake: yes / no"))
have_cake = str(input("do you have cake: yes / no"))
if want_cake == "yes":
    print ("We want cake...")
    if have_cake == "no":
         print ("But we don't have any cake!")
elif have_cake == "yes":
    print ("And it's our lucky day!")
else:
    print ("The cake is a lie.")
