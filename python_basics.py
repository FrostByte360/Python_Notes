#NOTES

print ("Hello, World!")
# This is my first Python program.


# VARIABLES
#=======================================================================================================================

# A variable is a reusable container for value. There are four basic data types:
# # int, string, float, and char.
# the variable behaves as if it was the value that it contains.

# string       value
#   v            v
full_name = "Mark Garcia"

# To print a string variable, the easiest way is to use an 'f' string.
# 'f' means format. Using an 'f' string, we can insert a variable wherever we would like.
# In order to insert the variable inside the print statement, place the variable name
# within the curly braces.

print (f"Hello, {full_name}.") # PRINTS "Hello, Mark Garcia."

#  int    value
#   v       v
legal_age = 21
print (f"I am {legal_age} years old.") # PRINTS "I am 21 years old."

#   float      value
#     v          v
general_average = 8.4
print (f"I have a grade of {general_average}.") # PRINTS "I have a grade of 8.4."

#    bool        value
#     v            v
isStillAStudent = True # True and False must need to be capitalized
print (f"Am I still a student? That is {isStillAStudent}.") # PRINTS "Am I still a student? That is True}."


# BASIC ARITHMETIC
#=======================================================================================================================

# In basic arithmetic, we have the following operators:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division (returns a float/fractional value)
# //  Integer Division (returns a whole numbered value)
# %   Modulus Operator (returns the remainder)

pie_slices = 6
print(f"I have a total of {pie_slices} pie slices.") # PRINTS "I have a total of 6 pie slices."

pie_slices += 6 # This is an augmented assignment operator. This can be interpreted as pie_slices = pie_slices + 6
print(f"I now have have a total of {pie_slices} pie slices.") # PRINTS "I now have have a total of 12 pie slices."

pie_slices -= 3
print(f"My friends ate some slices. I now have have a total of {pie_slices} pie slices.")
# PRINTS "My friends ate some slices. I now have a total of 9 pie slices."

pie_slices *= 3
print(f"Luckily my mom bought some more. Now I have {pie_slices} pie slices.")
# PRINTS "Luckily my mom bought some more. Now I have 27 pie slices."

pie_slices /= 3
print(f"My friends decided to get some more, and now I have approximately {pie_slices} pie slices.")
# PRINTS "My friends decided to get some more, and now I have approximately 9.0 pie slices."

pie_slices //= 3
print(f"My friends decided to get some more, and now I have {pie_slices} pie slices.")
# PRINTSMy friends decided to get some more, and now I have 3.0 pie slices.

pie_slices %= 3
print(f"I finally finished the whole pie. I now have a total of {pie_slices} pie slices. Since there's nothing left"
      f"anymore.")
# PRINTS "I finally finished the whole pie. I now have a total of 0.0 pie slices. Since there's nothing left anymore."


# TYPECASTING
#=======================================================================================================================
# Typecasting is the process of converting a variable from one data type to another. We have various functions to
# convert a variable or a value to a string(), int(), float(), or bool().

name = "John Doe"
age = 25
grade = 3.2
is_Student = True

# You could get the datatype of a variable or value by using the type function, then passing the variable or value like
# so, [  type(name)  ]. However, no output will be displayed. A print statement is needed; a value will be returned once
# the type function is within the print statement.

print(type(name))
print(type(age))
print(type(grade))
print(type(is_Student))
# The following will PRINT:
# <class 'str'>; the name variable is a string.
# <class 'int'>; the age variable is an integer.
# <class 'float'>; the grade variable is a float.
# <class 'bool'>; the student variable is a boolean.

# Converting the grade variable into an integer (float to int).

grade = int(grade)
print(grade)
# PRINTS 3

# Converting the age into a floating point number.

age = float(age)
print(age)
# PRINTS 25.0

# Converting the age into string.

another_age_variable = 30
another_age_variable = str(another_age_variable)
print(another_age_variable)
# In order to prove that the integer value was converted into a string datatype value, a type() function can be used.
print(type(another_age_variable))
# PRINTS "<class 'str'>"

# Converting the name variable into a boolean.
name = bool(name)
print(name)
# PRINTS "True"
# However, if the string variable is empty or null, the output will return false.
# this is useful for checking if the user has typed their name as an input or not.


# USER INPUT
#=======================================================================================================================
# In order to accept user input, an input() function is used.

fruit = input("Enter your favorite fruit: ")
print(fruit)
# PRINTS "Oranges"

print(f"That's nice. I see you like {fruit}. Awesome!")
# PRINTS "That's nice. I see you like Orange. Awesome!"

age = input("How old are you? ")
print(f"Damn, you are {age} years old.")
# PRINTS "Damn, you are 25 years old."

# User inputs are always of the string datatype. Typecasting may be used for other datatypes.

yet_another_age_variable = int(input("How old are you again? "))
yet_another_age_variable += 1

print(f"Oh, wait, you're turning {yet_another_age_variable} years old next year. Neat.")
# PRINTS "Oh, wait, you're turning 22 years old next year. Neat."



# IF STATEMENTS
#=======================================================================================================================
# If statements execute basic decision-making; a code is executed only IF a condition is true (if, elif, else).

userAge = int(input("Enter your age: "))

if userAge >= 1000:
    print(f"What the hell-???")
elif userAge >= 18:
    print(f"You are of legal age.")
elif userAge < 0:
    print(f"You are not of this world.")
elif userAge == 0:
    print(f"Seriously?")
else:
    print(f"You are not of legal age.")

# If the condition is true in which the user inputs an integer greater than 18, it will PRINT "You are of legal age."
# otherwise, "You are not of legal age." will be printed instead.
# The order of the if-else statements matter in Python.

ageOfAPerson = int(input("Enter your age: "))
doTheyHaveATicket = True
ticketPrice = 10.00

if ageOfAPerson >= 65:
    print("You are a senior citizen.")
    print(f"The ticket price for a senior citizen is {ticketPrice * 0.75}.")
elif ageOfAPerson >= 18:
    print("You are an adult.")
elif ageOfAPerson <= 18:
    print("You are a minor.")
    print(f"The ticket price for a minor is {ticketPrice * 0.5}.")
elif ageOfAPerson <= -1:
    print("Seriously?")
else:
    print("...")

if doTheyHaveATicket:
    print("You have a ticket.")
else:
    print("You do not have a ticket.")



# LOGICAL OPERATORS
#=======================================================================================================================
# Logical operators allow us to evaluate multiple conditions (or, and, not).
# OR   :  At least one condition is true.
# AND  :  Both conditions must be true.
# NOT  :  Inverts the condition.

localTemp = 25
isRaining = False

if localTemp >= 25 and isRaining:
    print("The temperature is too high, and it is currently raining.")
else:
    print("The weather is just fair.")



# WHILE LOOPS
#=======================================================================================================================
# A while loop is used to repeat a block of code as long as the condition is true.

#condition = 1
#
#while condition == 1:
#    print("I am stuck in a loop")
#    PRINTS the print statement repeatably without no end. This is not recommended.

thisIsYetAnotherName = input("Enter your name: ")

while thisIsYetAnotherName == "":
    print("Sorry, your name is invalid.")
    thisIsYetAnotherName = input("Please enter your name: ")
print(f"Hello, {thisIsYetAnotherName}!")

thisIsYetAnotherAge = int(input("Enter your age: "))

while thisIsYetAnotherAge < 0 or thisIsYetAnotherAge > 150:
    print("Sorry, your age is invalid.")
    thisIsYetAnotherAge = int(input("Please enter your age: "))
print(f"You are {thisIsYetAnotherAge} years old.")



# FOR LOOPS
#=======================================================================================================================
# A for loop is used to reiterate over a sequence such as a string, list, tuple, or set. It repeats a block of code an
# exact amount of time.

for i in range(10):
    print(i)
# PRINTS from 0 to 9, containing the 10 elements within the set index.

for a in range(1, 20):
    print(a)
# PRINTS from 1 to 19. The first number is inclusive, the second number is exclusive; the loop will begin counting from
# the inclusive number, ending with at the range before the exclusive number.

for x in range(0, 11, 2):
    print(x)
# PRINTS from 0 to 10. However, the index is incremented by 2.

nameOfAPerson = "Integral Calculus"

for everyLetter in nameOfAPerson:
    print(everyLetter)
# PRINTS every letter on a new line.

nameOfASecondPerson = "Differential Calculus"

for everyLetter in nameOfASecondPerson:
    print(everyLetter, end=" ")
# PRINTS every letter with a space.

print("")

# COUNTDOWN SIMULATION

import time
for counter in range(10, 0, -1):
    print(counter)
    time.sleep(1) # seconds
print("Happy New Year!")



# LIST, TUPLES, SETS
#=======================================================================================================================
# Lists, tuples, and sets are all similar to arrays. However, in Python, there three different varieties with each
# their own benefits.

#   LIST []  =  Mutable, refelxive
#   TUPLE () =  immutable, fast
#   SET {}   =  mutable (can add or remove), unordered, no dupplications, best for membership testing

# List
# Index           0         1        2         3
IHaveAFruit = ["Banana", "Mango", "Papaya", "Orange"]
print(IHaveAFruit)
# It prints out the entire list, including the brackets.
# To access one of the elements within the list, an index pointer operator is used.

print(IHaveAFruit[3])
# PRINTS "Papaya"
# If an attempt is made to access an element that doesn't exist, an error will occur. Index will be out of range.

# In order to change one of the elements at a given index, an index operator is used once more by reassigning the value
# within the variable itself.

IHaveAFruit[1] = "Coconut"
print(IHaveAFruit)
# Mango now becomes Coconut.

IHaveAFruit.append("Guava")
print(IHaveAFruit)
# Adds Guava at the end of the list.
# push()

IHaveAFruit.remove("Banana")
print(IHaveAFruit)
# Removes the Banana from the list.
# delete()

IHaveAFruit.pop("Orange")
# Pops the Banana from the list.
# pop()

IHaveAFruit.clear()
# Removes the elements from the list.


# Tuples
IHaveAFruit = ("Banana", "Mango", "Papaya", "Orange")
# This list can't be changed whatsoever.

# Sets
IHaveAFruit = {"Banana", "Mango", "Papaya", "Orange"}
print(IHaveAFruit)
# Elements could be added or removed, but can never be replaced or modified.
# Whenever a set is printed, the order of elements will be printed at random.
# Sets do not support item assignment.
# An element can be added by using the .add() function.
# An element can be removed by using the .remove() function.
# An element can be popped by using the .pop() function.

# Simple Search Example Using a Set

missingPerson = {"Erodeus", "Chermainia", "Ignacious", "Rutherford", "Mark", "Christina", "Arubeus", "Maximus"}
personName = input(f"Enter the name of the victim: ")

if personName in missingPerson:
    print(f"Sorry, {personName} is among the list of victims.")
else:
    print(f"Apologies, {personName} is not among the list of victims.")