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
# PRINTS "My friends ate some slices. I now have have a total of 9 pie slices."

pie_slices *= 3
print(f"Luckily my mom bought some more. Now I have {pie_slices} pie slices.")
# PRINTS "Luckily my mom bought some more. Now I have 27 pie slices."