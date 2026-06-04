# TRY AND EXCEPT EXCEPTION HANDLING
# In python, Try and Except are used for exception handling.
# This allows the program to continue running even if an error occurs.

# PROGRAM WITHOUT A TRY-EXCEPT
#======================================================================
# Go ahead and input a character instead.

''' num = int(input("Enter a number: "))
 print(10/num)'''
from sys import exec_prefix
from typing import final

#======================================================================
# This will create an error:

# Traceback (most recent call last):
#   File "C:\Users\User\OneDrive\Documents\Programming\Python_Projects\My_First_PyCharm_Program\try_except.py", line 9, in <module>
#     num = int(input("Enter a number: "))
# ValueError: invalid literal for int() with base 10: 'aasdf'

# PROGRAM WITH A TRY-EXCEPT
#======================================================================
# Go ahead and input a character instead.

'''try:
    num = int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("Only integers are allowed")'''

#======================================================================
# This will create an error, but a message will be displayed:
# |Only integers are allowed|

'''
COMMON EXCEPTIONS IN PYTHON
=======================================================================
ValueError - Invalid value entered.
ZeroDivisionError - Any operation divided by zero
TypeError - Invalid data type entered.
NameError - Variable used is undefined.
IndexError - Invalid list index entered.
KeyError - Invalid key entered.
FileNotFoundError - Searching for a File that Doesn't Exist.
PermissionError - Permission denied entered.
'''

# PROGRAM WITH A TRY-EXCEPT-ELSE
#======================================================================

'''
try:
    num = int(input("Enter a number: "))
    result = (10/num)
except ValueError:
    print("Only integers are allowed")
except ZeroDivisionError:
    print("Cannot be divided by zero")")
else:
    print(f"Result: {result}")
'''

# PROGRAM WITH A TRY-EXCEPT-FINALLY
# If an error occurs along the program, the FINALLY keyword will always be executed,
# depending on the statement that you are pertaining to.
# And even though a correct outcome occurs throughout thr program, the program will still run the
# FINALLY keyword.
#======================================================================

'''
try:
    num = int(input("Enter a number: "))
    result = (10/num)
    print(result)
except ValueError:
    print("Only integers are allowed")
except ZeroDivisionError:
    print("Cannot be divided by zero")")
finally:
    print("Program is Finished")
'''

# FILE HANDLING TRY-EXCEPT
#======================================================================

'''
try:
    file = open("C:/Users/Public/Documents/testDocumentText.txt")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program is Finished")
'''

# MENU PROGRAM EXAMPLE
#======================================================================

'''
while True:
    try:
        num1 = int(input("Enter the first Integer: "))
        num2 = int(input("Enter the second Integer: "))
        answer = num1 / num2
        print(answer)
    except ZeroDivisionError:
        print("Cannot be divided by zero")
    except ValueError:
        print("Only integers are allowed")
    finally:
        print("Program is Finished")

    choice = input("Would you like to continue? (Y/N): ")
    if choice.lower() == "n":
        break
'''

# CUSTOM USER EXCEPTION USING RAISE
#======================================================================
'''
age = int(input("Enter your age: "))
if age <= 0:
    print("Your age must be greater than zero")
    raise AgeError("Age cannot be negative.")
else:
    print(age)
'''