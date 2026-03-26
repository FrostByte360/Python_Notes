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
print(f"I finally finished the whole pie. I now have a total of {pie_slices} pie slices. Since there's nothing left anymore.")
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