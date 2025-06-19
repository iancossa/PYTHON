'''
#Exception handling in Python 
a=str(input("Enter a string: "))
b=int(input("Enter a number: "))
c=a*b
print(c)#ValueError if you insert a unexpected data type
#c=a/b#If you insert 0 will give you ZeroDivisionError & if you use str will give you TypeError,
#  you can't divide str,you can't multiple str with str:TypeErrors

Common built-in Excepetion Error
ValueError , ZeroDivisionError, NameError, TypeError, IndexError, FileNotFoundError, AttributeError


try:
    x=10/0
except ZeroDivisionError:
    print("You can't divide by zero")
'''
try:
    num = int(input("Enter a number:"))
    result= 10/ num
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Success:",result)

#Creating my own Exception
age= int(input("Enter your age: "))
if age<18:
    raise ValueError("Age must be 18 or older")
else:
    print("Access granted.")


