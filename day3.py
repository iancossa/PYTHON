'''
#returning functions
#types of arguments
#positional arguments
def greet(trainer,student="Melo"): #default parameter will get overwritten by argument
    print(f"Hello {trainer} sir")
    print(f"welcome {student}")

greet("Cossa") #keyword argument

#variable length arguments -> *args. *kwargs
def bye(*args): 
    print(args)
bye(3,4,5)
def welcome(*args):
    for i in args:
        print(f"Welcome {i}")
welcome("Ian","Rafael","Elias","Cossa")

def hi(**kwargs):
    print(kwargs)
hi(trainer="Arjun",student="Mabunda")

def greet(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

    for k in kwargs.keys():
        print(f"{k}")
    for v in kwargs.values():
        print(f"welcome{v}")
    

greet(trainer=" Enzo",student=" Militao",dean=" Vipul")

'''

print("---MODULES---")
import math
'''
a=114
print(math.sqrt(a))
print(math.log(5))
print(math.pow(4,5))
print(math.ceil(7.3))
print(math.floor(9.9))

import random
print("Guess an number between 1 and 20")
guess = random.randint(1,20)
while True:
    answer = int(input())
    if(answer>guess):
        print("your answer is higher,try again")
    elif(answer<guess):
        print("Your answer is lower")
    else:
        print("Congrats you won")    
        break
'''

#MOD
def greet(name):
    print(name)

def add(a,b):
    print(a+b)